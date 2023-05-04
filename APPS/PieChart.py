#!/usr/bin/env python
# coding: utf-8

# In[8]:

import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/Damistar05/CA2DV/main/cleaned_customer_shopping_data.csv")

# Calculate total revenue
total_revenue = df['Revenue'].sum()

# Create donut chart
fig = px.pie(df, values='Revenue', names='category', hole=.5, color_discrete_sequence=px.colors.qualitative.Dark24)

# Add revenue to hover information
fig.update_traces(hovertemplate='Category: %{label}<br>Revenue: %{value:$,.2f}')

# Create app layout
layout = html.Div([
    html.H1(children='Revenue by Category', style={'textAlign': 'center'}),
    dcc.Graph(id='donut-chart', figure=fig),
    html.H2(f'Total Revenue: ${total_revenue:,.2f}', style={'textAlign': 'center'})

])


# Create callback to capture click data
@app.callback(
    Output('donut-chart', 'figure'),
    Input('donut-chart', 'clickData'))
def display_click_data(clickData):
    if clickData is not None:
        category = clickData['points'][0]['label']
        df_filtered = df[df['Category'] == category]
        fig = px.pie(df_filtered, values='Revenue', names='PaymentMethod', hole=.5, color_discrete_sequence=px.colors.qualitative.Dark24)
        fig.update_traces(hovertemplate='Payment Method: %{label}<br>Revenue: %{value:$,.2f}')
        return fig
    else:
        return fig






# In[ ]:




