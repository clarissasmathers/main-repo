import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import config

from app import app

layout = html.Div([
	html.Div([
        html.H3('Influenza'),
        html.H5('Catch all the Bugs'),
        dcc.Link('Inspect Lists', href='/insepect-lists'),
        dcc.Link('Inspect Influence Scores', href='/influence-scores'),
        dcc.Link('Universe Crosstabs', href='/crosstabs'),
		],
	id='main-content',
    style={
        'display': 'flex',
        'flex-direction': 'column',
        'justify-content': 'center',
        'align-items': 'center',
    })
    ],
    style= {
        'display': 'flex',
        'flex-direction': 'column',
        'justify-content': 'center',
        'align-items': 'center',
        'resize': 'both',
        'overflow': 'auto',
    }
)

