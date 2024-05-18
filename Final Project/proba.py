#  First: => pip install matplotlib


import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
try:
    # try to connect to BD
    conn = psycopg2.connect(dbname='sqlfree-5', user='netology', password='NetoSQL2019', host='84.201.152.11', port='19001')
except:
    # if the connection fails, a message will be output
    print('Can`t establish connection to database')

# mycursor = conn.cursor()

# mycursor.execute("select c.category  category, sum(p.price) price_cat,  sum(sum(p.price)) over () total_sum,\
#                   round(sum(p.price)*100 / sum(sum(p.price)) over () ,3) procent \
#                 from work.product p \
#                 join work.category c on c.category_id = p.category_id \
#                 group by p.category_id, c.category \
#                 order by 4 desc")

# rows = mycursor.fetchall()

# for row in rows:
#         print(row)

data = pd.read_sql('SELECT * FROM work.product', conn)
print(data.head(100))

# sql = "select o.order_id , c.city \
#        from work.orders o \
#        join work.delivery d on o.delivery_id = d.delivery_id \
#        join work.address a on a.address_id = o.delivery_id \
#        join work.city c on c.city_id = a.city_id "


# --Найдите категорию товара, у которой наибольшее процентное отношение цены 
# --товаров в таблице Product от общего стоимости всех товаров.
# -- Какова будет процентная доля у этой категории?

# sql = "select c.category, sum(p.price) price_cat,  sum(sum(p.price)) over () total_sum,\
#     round(sum(p.price)*100 / sum(sum(p.price)) over () ,3) procent\
#     from work.product p\
#     join work.category c on c.category_id = p.category_id \
#     group by p.category_id, c.category \
#     order by 4 desc"

# -- получить накопительную сумму платежей по каждому покупателю
# sql = "select o.order_id , o.customer_id , o.amount ,\
#     sum(o.amount) over (partition by o.customer_id order by o.order_id) \
#     from work.orders o"

# -- получить общую сумму и количество заказов по каждому покупателю  !!!!!!!
# sql = "select o.customer_id , concat(c.first_name,' ',c.last_name) as name, sum(amount) as total_sum,\
#     count(order_id) as num_of_orders \
#     from work.orders o \
#     join work.customer c on o.customer_id = c.customer_id \
#     group by o.customer_id,  c.first_name, c.last_name \
#     order by 3 desc"

# -- общая сумма заказов мин, макс и средняя сумма по месяцам
sql = "select date_trunc('MONTH', o.created_date) as date, sum(amount) as suma, min(amount), max(amount), round(avg(amount),2) \
    from work.orders o \
    group by date_trunc('MONTH', o.created_date)\
    order by 1"
data = pd.read_sql(sql,conn)
print(data.head())
x=[]
x=[x.append(i.strftime("%B")) for i in data['date']]
y = data['suma']
# Graph
# plt.plot(x, y, color='blue', marker='o', markersize=7)
# plt.xlabel('2023') #Подпись для оси х
# plt.ylabel('Amount of orders') #Подпись для оси y
# plt.title('Sum pe month') #Название
# plt.show()

# Round diagram:

plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Distribution of orders by month")
plt.show()



#-- numbers of products in the each category
sql = "select c.category , count(*) maximum \
    from work.product p \
    join work.category c ON p.category_id = c.category_id\
    group by c.category_id"
    #   \
    # order by count(p.category_id)"

data = pd.read_sql(sql,conn)
print(data.head(15))

x = data['category']
y = data['maximum']
# plt.plot(y, x, color='green', marker='o', markersize=7)
# plt.xlabel('Products') # Title for X
# plt.ylabel('Category') # Title for Y
# plt.title('Products in the category') #Название
# plt.show()

plt.bar(x, y, label='Numbers of item', color='green') # The label parameter allows to specify the name of the value for the legend
plt.xlabel('Category')
plt.xticks(rotation=90)
plt.ylabel('Products')
plt.title('Example of stolb diagrams')
plt.legend()
plt.show()

# mycursor.close()

# print(mycursor.execute(sql))
cursor = conn.cursor() 

request_to_read_data = "select category_id as num,category as category  from work.category order by category_id asc"

cursor.execute(request_to_read_data)

data = cursor.fetchall()
dict1={}
        
for i in range(len(data)):
    for j in range(len(data[i])-1):
        dict1[i] = ({'num':data[i][j], 'category':data[i][j+1]})

for value in dict1.values():
     print(value)


class Categorys:
    def __init__(self):
        self._categories ={}
                   
    # count = 1
    def add_category(self, categ):
        # self._categories[self.count] = categ
        self._categories.update([categ])

        # self.count += 1
    def print_categ(self):
        for value in self._categories.values():
            print(value)
    def print_num_categ(self):
        for key,value in self._categories.items():
            print(key, value)   
category_table = Categorys()
for i in data:
    category_table.add_category(i)
# category_table.print_categ()   
category_table.print_num_categ()  

conn.close()
