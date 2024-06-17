import dash
from dash import html



dash.register_page(__name__, path="/ABC_XYZ_Analysis" , name="ABC XYZ Analysis")

layout = html.Div(children=[
        html.Div(children=[
            html.H2("ABC XYZ Analysis"),
         "Invetory Management",
        html.Br(), html.Br(),
    ])
])
