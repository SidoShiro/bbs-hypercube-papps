# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, url_base_pathname=os.environ['PAPP_BASE_URL'])


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF', 'marker': {'color': 'red'}},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal', 'marker': {'color': 'green'}},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    import boto3
    sts = boto3.client('sts')
    print(sts.get_caller_identity())
    s3 = boto3.client('s3')
    print(f"Opening data file from {os.environ['DATA_BUCKET_NAME']}/{os.environ['DATA_FILE_PATH']} ...")
    result = s3.get_object(Bucket=os.environ['DATA_BUCKET_NAME'], Key=os.environ['DATA_FILE_PATH'])
    print(result)
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ['PAPP_LISTENING_PORT']))
