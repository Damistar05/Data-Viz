#!/usr/bin/env python
# coding: utf-8

# In[2]:



from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
from app import app

# In[ ]:


# Load the customer shopping data
df = pd.read_csv("cleaned_customer_shopping_data.csv")


# Define the app layout
layout = html.Div([
    html.H1("Total Revenue Across Shopping Malls"),
    dcc.Dropdown(
        id="mall-dropdown",
        options=[{"label": mall, "value": mall} for mall in df["shopping_mall"].unique()],
        value=df["shopping_mall"].unique()[0]
    ),
    dcc.Graph(id="revenue-graph"),
])

# Define the app callback
@app.callback(
    Output("revenue-graph", "figure"),
    [Input("mall-dropdown", "value")]
)
def update_revenue_graph(mall):
    # Filter the data by mall
    mall_data = df[df["shopping_mall"] == mall]

    # Calculate the total revenue for the selected mall
    total_revenue = mall_data["Revenue"].sum()

    # Create the bar chart
    fig = {
        "data": [
            {
                "x": [mall],
                "y": [total_revenue],
                "type": "bar"
            }
        ],
        "layout": {
            "title": "Total Revenue for {}".format(mall),
            "yaxis": {"title": "Revenue"}
        }
    }

    return fig


