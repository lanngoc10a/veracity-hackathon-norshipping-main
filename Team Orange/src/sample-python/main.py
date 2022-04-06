# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dashboard import Dashboard
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
df = pd.read_csv("result.csv")

external_stylesheets_ = [
    'https://cdn.jsdelivr.net/npm/@posten/hedwig@11.5.4/assets/fonts.css',
]

external_scripts_ = [
    'https://cdn.jsdelivr.net/npm/@posten/hedwig@11.5.4/dist/icons.min.js',
]

SMALL_SIZE = dict(width=400, height=300)
BIG_SIZE = dict(width=800, height=700)
MEDIUM_SIZE = dict(width=600, height=400)
WIDE_SIZE = dict(width=600, height=350)



app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Vessel Optimization'),
        html.Div(children='''
            Dashboard: predict.
        ''', className='subtitle bold'),
        ], className='header'),

    html.Div([
        html.Div([
            html.P(['Number of Rows: 15,855'], id='row-disp'),
            html.P(['Number of Columns: 19'], id='column-disp'),
            ], className='row'),
         ], id='status', className='center'),

        #   html.Div([
        #         dcc.Dropdown(
        #             id='t1-input',
        #             className='filter',
        #             value=None,
        #             options=[
        #                 {'label': t, 'value': t} for t in Dashboard.T1s
        #             ],
        #             placeholder='Select imo',
        #         ),
       
        #             ], className='center row'),
    
       
        ], className='section', id='sec-terminals')

if __name__ == '__main__':
    app.run_server(debug=True)