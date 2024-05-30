import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc, html
import plotly.express as px
import pandas as pd
import psycopg2
import warnings
import plotly.graph_objects as go

warnings.filterwarnings('ignore')

try:
    # try to connect to BD
    conn = psycopg2.connect(dbname='sqlfree-5', user='netology', password='NetoSQL2019', host='84.201.152.11', port='19001')
except:
    # if the connection fails, a message will be output
    print('Can`t establish connection to database')

# # Create the app

app = dash.Dash(__name__)

app_title= html.H1(children='Welcome to the Orders Analysis Dashboard!',
                 style={"display": "flex", "justify-content": "center"},)

sql = "select o.customer_id , concat(c.first_name,' ',c.last_name) as name, sum(amount) as total_sum,\
    count(order_id) as num_of_orders \
    from work.orders o \
    join work.customer c on o.customer_id = c.customer_id \
    group by o.customer_id,  c.first_name, c.last_name \
    order by 3 desc"
# Load dataset
data = pd.read_sql(sql,conn)

title_font_templ = dict(family="Courier New",
                        size= 20,
                        weight = 'bold',
                        # style ="italic",
                        color="Black",
                        # variant="small-caps",
                        )

scatter = px.scatter(
   x = data['total_sum'],
   y = data['num_of_orders'],
   color_discrete_sequence=['cornflowerblue'],
   # color="size",
   title="Distribution of orders by customers",
   width=800,
   height=400,
).update_layout(xaxis_title="Total sum of orders by customers", yaxis_title="Number of orders", title_x=0.5,
                title_font=title_font_templ)


#-- numbers of products in the each category
sql = "select c.category , count(*) maximum\
    from work.product p \
    join work.category c ON p.category_id = c.category_id\
    group by c.category_id"
    # limit 10"
    #   \
    # order by count(p.category_id)"

data = pd.read_sql(sql,conn)

x = data['category']
y = data['maximum']

round = px.pie(labels = x, values= y, names= x, title="Percentage products by category")
round.update_layout(title_x = 0.5,
                    title_font = title_font_templ)



sql = "select date_trunc('MONTH', o.created_date) as date, sum(amount) as suma, min(amount), max(amount), round(avg(amount),2) \
    from work.orders o \
    group by date_trunc('MONTH', o.created_date)\
    order by 1"
data = pd.read_sql(sql,conn)
x =[]
for i in data['date']:
    x.append(i.strftime("%B"))
y = data['suma']
histogram = px.histogram(
   x= x,
   y= y,
   title="Amount of orders per year",
   width=600,
   height=400,
).update_layout(xaxis_title="2023 ", yaxis_title="Sales",title_x=0.5,
                title_font=title_font_templ)


sql = "select c1.city as city , count(o.order_id) numbers\
    from work.customer c \
    join work.orders o on o.customer_id = c.customer_id \
    join work.address a on a.address_id =c.address_id \
    join work.city c1 on c1.city_id  = a.city_id \
    group by c1.city \
    order by 2 desc "

df = pd.read_sql(sql,conn)

fig = go.Figure(data=[go.Table(
    columnwidth = [60,40],
    header=dict(values= ['City','Number of orders'],
                # fill_color='paleturquoise',
                line_color='darkslategray',
                fill_color='royalblue',
                align=['left','center'],
                font=dict(color='white', size=14),
                height=40 
                ),
    cells=dict(values=[df.city, df.numbers],
             fill_color='lavender',
            line_color='darkslategray',
            # fill=dict(color=['paleturquoise', 'white']),
            align=['left', 'center'],
            font_size=14,
            height=30
               ))
])
fig.update_layout(title_text='Cities where orders from:', title_x=0.5,
                   title_font=title_font_templ)


left_fig1 = html.Div(children=dcc.Graph(figure=scatter))
# right_fig = html.Div(children=dcc.Graph(figure=round))
right_fig1 = html.Div(children=dcc.Graph(figure=histogram))
upper_div = html.Div([left_fig1, right_fig1], style={"display": "flex"})

left_fig2 = html.Div(
   children=dcc.Graph(figure=round),
    #  children=dcc.Graph(figure=violin),
#    style={"display": "flex"},
)
right_fig2 = html.Div(
   children=dcc.Graph(figure=fig),
)

# Status delivery

sql = "select o.amount , d.status \
    from work.delivery d \
    join work.orders o on o.delivery_id = d.delivery_id \
    group by d.status, o.amount \
    order by 2 "
data = pd.read_sql(sql,conn)

violin = px.violin(
  
   x = data['status'],
   y = data['amount'],
   title="Delivery",
   width=600,
   height=400,
).update_layout(xaxis_title="Order status", yaxis_title="Sum of order ($)",title_text='Delivery status', title_x=0.5,
                   title_font=title_font_templ)
lower_div = html.Div([left_fig2, right_fig2], style={"display": "flex"})

central_div = html.Div(
   children=dcc.Graph(figure=violin),
   style={"display": "flex", "justify-content": "center"},
)

app.layout = html.Div([app_title, upper_div, lower_div,central_div])

cursor = conn.cursor() 

request_to_read_data = "select category_id as num,category as category  from work.category order by category_id asc"

cursor.execute(request_to_read_data)

data = cursor.fetchall()
dict1={}
        
for i in range(len(data)):
    for j in range(len(data[i])-1):
        dict1[i] = ({'num':data[i][j], 'category':data[i][j+1]})
print("Dictionary Categories:")
for value in dict1.values():
     print(value)

# 10 maximum sales by cities

request_to_read_data ="select c1.city , count(o.order_id) numbers \
from customer c \
join orders o on o.customer_id = c.customer_id \
join address a on a.address_id =c.address_id \
join city c1 on c1.city_id  = a.city_id \
group by c1.city \
order by 2 desc \
limit 10"

cursor.execute(request_to_read_data)
data = cursor.fetchall()

# Create class for  dictionary with data from tables BD and functions for output data

class TableBD:
    def __init__(self):
        self._categories ={}
                   
    # count = 1
    def add_row(self, categ):
        # self._categories[self.count] = categ
        self._categories.update([categ])

        # self.count += 1
    def print_values(self):
        for value in self._categories.values():
            print(value)
    def print_name(self):
        for key,value in self._categories.items():
            print(key, value)   


city_table = TableBD()

for i in data:
    city_table.add_row(i)

# city_table.print_values()

city_table.print_name()  

if __name__ == "__main__":
   app.run_server(debug=True)
conn.close()
