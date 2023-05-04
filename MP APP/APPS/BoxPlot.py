#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load data from CSV
df = pd.read_csv('https://raw.githubusercontent.com/Damistar05/CA2DV/main/cleaned_customer_shopping_data.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1('Box Plot of Revenue by Shopping Mall'),
    dcc.Dropdown(
        id='shopping-mall-dropdown',
        options=[{'label': i, 'value': i} for i in df['shopping_mall'].unique()],
        value=df['shopping_mall'].unique()[0]
    ),
    dcc.Graph(id='box-plot')
])

# Define the app callback
@app.callback(
    Output('box-plot', 'figure'),
    Input('shopping-mall-dropdown', 'value')
)
def update_box_plot(shopping_mall):
    # Filter the data based on the selected shopping mall
    filtered_df = df[df['shopping_mall'] == shopping_mall]
    
    # Create the box plot with Plotly Express
    fig = px.box(filtered_df, x='payment_method', y='Revenue', color='payment_method')
    
    # Update the layout
    fig.update_layout(
        title=f"Box Plot of Revenue by Shopping Mall ({shopping_mall})",
        xaxis_title="Payment Method",
        yaxis_title="Revenue"
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

  


# In[ ]:




