import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from db_creds import *
from plotly import graph_objs as go


import config
import utils
from app import app

def get_influence_data(schema='influencers', table='generic_federal_basetable_20180423'):
	granularity = 100
	lists = exec_query("""
		SELECT column_name FROM information_schema.columns
		WHERE table_schema = '{schema}' AND table_name = '{table}'
		AND column_name ilike '%_list'
		ORDER BY 1
		""".format(schema=schema, table=utils.get_latest_union()), verbose=True).column_name.as_matrix()

	query = """
		SELECT
		CEIL(influence_rank * {granularity}) as influence_pctile,
		{lists}
		FROM {schema}.{union}
		JOIN (SELECT *, percent_rank() OVER(ORDER BY influence ASC) as influence_rank FROM {schema}.{table} WHERE influence > 0)
		USING(voterbase_id)
		GROUP BY 1
		ORDER BY 1
	""".format(
		schema = schema,
		table = table,
		lists = ", \n".join(["SUM({list}) as {list}".format(list=l) for l in lists]),
		granularity = granularity,
		union = utils.get_latest_union(schema)
		)

	raw_data = exec_query(query, verbose=True)

	return raw_data

def transform_data(raw_data, min=0, max=100):

	## Transpose:
	data = raw_data.transpose()
	print(data.columns)
	print(data.index)
	data = data.drop('influence_pctile', axis=0)
	counts = data.copy()
	data = data.divide(data.sum(axis=1), axis=0)
	# Sort:
	sort = data * data.columns.values

	data['list'] = data.index
	counts['list'] = counts.index
	data.index = (sort.sum(axis=1))
	counts.index = (sort.sum(axis=1))
	data = data.sort_index()
	counts = counts.sort_index()
	data.index = data['list'].str.replace("_list", "")
	counts.index = counts['list'].str.replace("_list", "")
	data = data.drop('list', axis=1)
	counts = counts.drop('list', axis=1)

	return data, counts

def influence_heatmap(data, counts):
	tooltip = counts.copy()
	tooltip = tooltip.applymap(lambda x: "{}".format(int(x))) + "VB IDs; " + data.copy().applymap(lambda x: "{0:.1f}".format(x * 100)) + "% of list"


	trace = go.Heatmap(
		z = (data.as_matrix() ** (1/3)),
		x = data.columns.values,
		y = data.index,
		text = tooltip.as_matrix(),
		colorscale='Blues',
		hoverinfo='x+y+text',
		showscale=False,
		reversescale=True,
		)

	data = [trace]

	title = "Influence Distribution by List"

	layout = go.Layout(
		title=title,
		margin = {
			'l': 200
		},
		showlegend = False,
		)

	fig = go.Figure(data=data, layout=layout)

	return fig

influence_table_dropdown_influencers = utils.table_dropdown(
	id = 'influence_table_dropdown_influencers',
	schema = 'influencers',
	table = 'sum_of_scores_%_[0-9]{8}',
	suppressions_list=["TRUE"],
	default_value=0
	)

influence_table_dropdown_influencers_dev = utils.table_dropdown(
	id = 'influence_table_dropdown_influencers_dev',
	schema = 'influencers_dev',
	table = 'sum_of_scores_%_[0-9]{8}',
	suppressions_list=["TRUE"],
	default_value=0
	)

layout = html.Div([

	# Configuration:
	html.Div([
		dcc.Dropdown(
			id = 'influence_schema_dropdown',
			options = [
				{'label': 'Development', 'value': 'influencers_dev'},
				{'label': 'Production', 'value': 'influencers'}
			],
			value='influencers'
			),
		html.Div([
			html.Div(influence_table_dropdown_influencers, id = 'influence_table_dropdown_influencers_div', style = {'display': 'block',}),
			html.Div(influence_table_dropdown_influencers_dev, id = 'influence_table_dropdown_influencers_dev_div', style = {'display': 'none',}),
			# html.Button(id='influence_drop_table', children='DROP TABLE', type='submit'),
			],
			id = 'influence_drop_table_row'
		),

	]),
	# Visualization:
	dcc.Graph(
		id = 'influence_figure',
		style = {
			'height': '2200px'
		}
	)
])


# GET TABLES FROM SCHEMA:
@app.callback(
	Output('influence_table_dropdown_influencers_div', 'style'),
	[Input('influence_schema_dropdown', 'value')]
	)
def update_influence_table_dropdown_influencers(value):
	print(value)
	if value == 'influencers':
		return {'display': 'block'}
	return {'display': 'none'}

@app.callback(
	Output('influence_table_dropdown_influencers_dev_div', 'style'),
	[Input('influence_schema_dropdown', 'value')]
	)
def update_influence_table_dropdown_influencers_dev(value):
	print(value)
	if value == 'influencers_dev':
		return {'display': 'block'}
	return {'display': 'none'}




# UPDATE THE INFLUENCE DISTRIBUTION LIST:
@app.callback(
	Output('influence_figure', 'figure'),
	[Input('influence_table_dropdown_influencers', 'value'),
	Input('influence_table_dropdown_influencers_dev', 'value')],
	[State('influence_schema_dropdown', 'value')]
)
def update_heatmap(table_schema1, table_schema2, schema):
	print("Updating Heatmap!")

	if schema == 'influencers':
		table = table_schema1
	elif schema == 'influencers_dev':
		table = table_schema2

	raw_data = get_influence_data(schema, table)
	data, counts = transform_data(raw_data)
	return influence_heatmap(data, counts)



