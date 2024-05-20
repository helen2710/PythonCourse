import dash
import dash_core_components as dcc
import dash_html_components as html
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
# #app = dash.Dash(__name__)
# app = dash.Dash(name="my_first_dash_app")

# # Load dataset using Plotly
# tips = px.data.tips()

# fig = px.scatter(tips, x="total_bill", y="tip") # Create a scatterplot

# app.layout = html.Div(children=[
#    html.H1(children='Hello Dash'),  # Create a title with H1 tag

#    html.Div(children='''
#        Dash: A web application framework for your data.
#    '''),  # Display some text

#    dcc.Graph(
#        id='example-graph',
#        figure=fig
#    )  # Display the Plotly figure
# ])

# if __name__ == '__main__':
#    app.run_server(debug=True) # Run the Dash app



import seaborn as sns

app = dash.Dash(__name__)
sql = "select o.customer_id , concat(c.first_name,' ',c.last_name) as name, sum(amount) as total_sum,\
    count(order_id) as num_of_orders \
    from work.orders o \
    join work.customer c on o.customer_id = c.customer_id \
    group by o.customer_id,  c.first_name, c.last_name \
    order by 3 desc"
data = pd.read_sql(sql,conn)
# print(data.head())
# x=data['total_sum']
# y = data['num_of_orders']


scatter = px.scatter(
   x = data['total_sum'],
   y = data['num_of_orders'],
   color_discrete_sequence=['cornflowerblue'],
   # color="size",
   title="Distribution of orders by customers",
   width=800,
   height=400,
).update_layout(xaxis_title="Total sum of orders by customers", yaxis_title="Number of orders", title_x=0.5,
                title_font=dict(family="Courier New",
                            size= 20,
                            weight = 'bold',
                            # style ="italic",
                            color="Black",
                            # variant="small-caps",
                    ))

diamonds = sns.load_dataset("diamonds")


# scatter = px.scatter(
#    data_frame=diamonds,
#    x="price",
#    y="carat",
#    color="cut",
#    title="Carat vs. Price of Diamonds",
#    width=600,
#    height=400,
# )

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
round.update_layout(title_x=0.5,
                    title_font=dict(family="Courier New",
                            size= 20,
                            weight = 'bold',
                            # style ="italic",
                            color="Black",
                            # variant="small-caps",
                    ))



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
                title_font=dict(family="Courier New",
                            size= 20,
                            weight = 'bold',
                            # style ="italic",
                            color="Black",
                            # variant="small-caps",
                            ))


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
                   title_font=dict(family="Courier New",
                            size= 20,
                            weight = 'bold',
                            # style ="italic",
                            color="Black",
                            # variant="small-caps",
                            ))


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
violin = px.violin(
   data_frame=diamonds,
   x="cut",
   y="price",
   title="Violin Plot of Cut vs. Price",
   width=600,
   height=400,
)
lower_div = html.Div([left_fig2, right_fig2], style={"display": "flex"})

central_div = html.Div(
   children=dcc.Graph(figure=violin),
   style={"display": "flex", "justify-content": "center"},
)
app_tit= html.H1(children='Welcome to the Orders Analytics Dashboard!',
                 style={"display": "flex", "justify-content": "center"},)
app.layout = html.Div([app_tit, upper_div, lower_div,central_div])

if __name__ == "__main__":
   app.run_server(debug=True)
conn.close()
