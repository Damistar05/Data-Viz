#!/usr/bin/env python
# coding: utf-8

# In[ ]:




from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from app import app

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/Damistar05/CA2DV/main/cleaned_customer_shopping_data.csv")

# Define layout
app.layout = html.Div([
    html.H1('Shopping Data Table'),
    dcc.Graph(id='data-table', figure={
        'data': [
            go.Table(
                header=dict(values=list(df.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[df[col] for col in df.columns],
                           fill_color='lavender',
                           align='left')
            )
        ],
        'layout': go.Layout(
            title='Shopping Data Table'
        )
    }),
    html.Div(id='table_out')
])

# Define callbacks
@app.callback(
    Output('table_out', 'children'), 
    Input('data-table', 'clickData'))
def update_graphs(click_data):
    if click_data:
        row = click_data['points'][0]['row']
        col = click_data['points'][0]['x']
        cell_data = df.iloc[row][col]
        return f"Data: \"{cell_data}\" from table cell: ({row}, {col})"
    return "Click the table"



