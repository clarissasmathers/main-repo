import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
from flask import send_from_directory


from app import app
from apps import welcome, influence, crosstabs
import config
import utils
import db_creds

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Link(
        rel='stylesheet',
        href='/static/stylesheet.css'),

    html.Div(id='page-content')
    ])




@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
    )
def display_page(pathname):
    if pathname == '/':
        return welcome.layout
    elif pathname == '/influence-scores':
        return influence.layout
    elif pathname == '/crosstabs':
        return crosstabs.layout
    else:
        return "Page Not Found!"


# Get local stylesheet
@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

# css_url = "https://codepen.io/chriddyp/pen/bWLwgP.css"
# app.css.append_css({
#     "external_url": css_url
# })

if __name__ == '__main__':
    pass
    app.run_server(debug=True, host='0.0.0.0', port=8000)

