import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px


def hor_bar_chart(df, x_value, y_value):
    return px.bar(df, x=x_value, y=y_value)

hor_bar_chart(Sales, "Store", "SalesDollars")    

dash.register_page(__name__, path="/overview" , name="Overview")


layout = html.Div(children=[
        html.Br(),
        dcc.Graph(id = 'bar')
])


@callback(
    Output('bar', 'figure'),  # Output is the 'figure' property of the component with id 'bar'
    Input('bar', 'id')  # This is a dummy input for simplicity; adapt as needed for real applications
)
def update_graph(dummy):
    # Call your chart function with the necessary parameters
    return hor_bar_chart(Sales, "Store", "SalesDollars")