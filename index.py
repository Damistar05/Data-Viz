#!/usr/bin/env python
# coding: utf-8

# In[13]:


from dash import dcc
from dash import html
from dash.dependencies import Input, Output
# In[ ]:


# Connect to main app.py file
from APPS import app
from app import server

server = app.server

# Connect to your app pages
from APPS import TableChart, SingleBar,PieChart,DonutChart



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Table Chart ', href='/APPS/TableChart'),
        dcc.Link('Revenue Across Shopping Malls ', href='/APPS/SingleBar'),
        dcc.Link('Pie Chart', href='/APPS/PieChart'),
        dcc.Link('Donut Chart', href='/APPS/DonutChart'),
    ], className="row"),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/APPS/TableChart':
        return TableChart.layout
    if pathname == '/APPS/SingleBar':
        return SingleBar.layout
    if pathname == '/APPS/PieChart':
        return PieChart.layout
    if pathname == '/APPS/DonutChart':
        return DonutChart.layout
    else:
        return "404 Page Error!"


if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




