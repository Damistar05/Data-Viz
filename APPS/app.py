#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Required Libraries
import dash
import dash_bootstrap_components as dbc


#https://bootswatch.com/#
#Use of one of the dbc themes from bootswatch
external_stylesheets = [dbc.themes.SKETCHY]

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]

               )

#Running the app on the server
server = app.server

