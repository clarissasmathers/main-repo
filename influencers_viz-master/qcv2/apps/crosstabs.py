import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from db_creds import *
from plotly import graph_objs as go


import config
from app import app
import utils

# GENERATE DROPDOWNS:

schema_dropdown = dcc.Dropdown(
	id = 'crosstab_schema_dropdown',
	options = [
		{'label': 'Development', 'value': 'influencers_dev'},
		{'label': 'Production', 'value': 'influencers'}
	],
	value='influencers',
	)

universe_dropdown_influencers = utils.table_dropdown(
	id = 'crosstab_union_influencers_dropdown',
	schema = 'influencers',
	table = 'union_[0-9]{8}',
	suppressions_list = [
		"NOT(table_name ilike '%uhg%') -- TEMPORARY",
		"NOT(table_name ilike '%xtab%') -- TEMPORARY",
		"NOT(table_name ilike '%030%') -- TEMPORARY]",
	],
	default_value=-1)

universe_dropdown_influencers_dev = utils.table_dropdown(
	id = 'crosstab_union_influencers_dev_dropdown',
	schema = 'influencers_dev',
	table = 'union_[0-9]{8}',
	suppressions_list = [
		"NOT(table_name ilike '%uhg%') -- TEMPORARY",
		"NOT(table_name ilike '%xtab%') -- TEMPORARY",
		"NOT(table_name ilike '%030%') -- TEMPORARY]",
	],
	default_value=-1)

basetable_dropdown_influencers = utils.table_dropdown(
	id = 'crosstab_basetable_influencers_dropdown',
	schema = 'influencers',
	table = 'sum_of_scores_%_[0-9]{8}',
	suppressions_list=["TRUE"],
	default_value=-1
	)

basetable_dropdown_influencers_dev = utils.table_dropdown(
	id = 'crosstab_basetable_influencers_dev_dropdown',
	schema = 'influencers_dev',
	table = 'sum_of_scores_%_[0-9]{8}',
	suppressions_list=["TRUE"],
	default_value=-1
	)

var_selection_dropdown = dcc.Dropdown(
	id = 'group_selection_dropdown',
	value = ["COUNT(*) AS count", "AVG(influence) AS avg_influence_score"],
	options = [{'label': x, 'value': y} for x,y in config.xtab_group_options.items()],
	multi = True,
	)

group_selection_dropdown = dcc.Dropdown(
	id = 'var_selection_dropdown',
	value = [],
	options = [{'label': x, 'value': x} for x in config.xtab_var_options],
	multi = True,
	)

# CATEGORY TO FILTER DROPDOWN

filter_dropdown = dcc.Dropdown(
	id = 'filter_dropdown',
	value = [], 
	options = [{'label': k, 'value': k} for k in config.filter_options.keys()],
	multi = True,
	)

# CHECKING THE NUMBER OF CATEGORICAL SELECTIONS

@app.callback(
    Output('display_num_cats', 'children'),
    [Input('filter_dropdown', 'value')])
def display_num_cats(selected_filter):
	global cat_num
	cat_num = len(selected_filter)


# FIRST FOCUSED FILTER DROPDOWN

@app.callback(
    Output('first_focused_filter_dropdown', 'options'),
    [Input('filter_dropdown', 'value')])
def set_filter_options(selected_filter):
    return [{'label': i, 'value': i} for i in config.filter_options[selected_filter[0]]]

first_focused_filter_dropdown = dcc.Dropdown(
	id = 'first_focused_filter_dropdown')

# SAVING THE CATEGORICAL AND FIRST FOCUSED FILTER CHOICES

@app.callback(
    Output('first-display-selected-values', 'children'),
    [Input('filter_dropdown', 'value'),
    Input('first_focused_filter_dropdown', 'value')])
def set_display_children(selected_filter, selected_focus):
    text =  u'{} is a something in {}'.format(
        selected_focus, selected_filter,
    )
    global first, second
    (first, a, b, c, d, second) = text.split(maxsplit=6)

# SECOND FOCUSED FILTER DROPDOWN

@app.callback(
    Output('second_focused_filter_dropdown', 'options'),
    [Input('filter_dropdown', 'value')])
def set_filter_options_two(selected_filter):
    return [{'label': i, 'value': i} for i in config.filter_options[selected_filter[1]]]

second_focused_filter_dropdown = dcc.Dropdown(
	id = 'second_focused_filter_dropdown')

# SAVING THE CATEGORICAL AND SECOND FOCUSED FILTER CHOICES

@app.callback(
    Output('second-display-selected-values', 'children'),
    [Input('filter_dropdown', 'value'),
    Input('second_focused_filter_dropdown', 'value')])
def set_display_children(selected_filter, selected_focus):
    text =  u'{} is a something in {}'.format(
        selected_focus, selected_filter,
    )
    global third, fourth
    (third, a, b, c, d, fourth) = text.split(maxsplit=6)


# GENERATE XTABS:

def write_one_var(table, universe, where_clause='TRUE', var_name=None, output='COUNT(*)', verbose=False):
    '''Write a single sql statement for an xtab
    args:
    table (str): The schema.table of that you want to inspect
    universe (str): A string to name the universe
    kwargs:
    var_name (str): A string, an xtabs variable like age, gender...
    None returns the topline statement
    output (str): The SELECT statement, without SELECT
    where_clause (str): A string that produces each universe
    that goes after a WHERE sql statement
    verbose (bool) = print sql to screen
    returns:
    sql string
    '''
    if var_name is None:
        sql = 'SELECT \'Topline\' AS Variable\n, \'Topline\' AS Level\n, {output} \nFROM {table} \nWHERE {where_clause} \nGROUP BY 1,2'.format(output=output, table=table, where_clause=where_clause, universe=universe)
    else:
        sql = 'SELECT \'{var_name}\' AS Variable\n, {var_name}::VARCHAR AS Level\n, {output} \nFROM {table} \nWHERE {where_clause} \nGROUP BY 1,2'.format(var_name=var_name, output=output, table=table, where_clause=where_clause, universe=universe)
    if verbose:
        print(sql)
    return sql

def write_all_vars(table, universe_list, where_clause_list, var_list, output='COUNT(*)', persistent=False, local=False, table_name='xtabs', verbose=False):
    '''Create a complete document of xtabs for a data set
    args:
    table (str): The schema.table of that you want to inspect
    universe_list (list): A list of strings to name each universe,
    must be ordered the same as where_clause_list and same number
    where_clause_list (list): A list of strings that produce each universe
    that go after a WHERE sql statement
    var_list (list): List of strings, xtabs variables like age, gender...
    kwargs:
    output (str): The SELECT statement, without SELECT
    fname (str): Where to save the xtabs
    persistent (bool): Write create table statement
    local (bool): Write create local temporary table
    table_name (str) = table name of persistent/local table
    verbose (bool) = print sql to screen
    returns:
    saved file
    '''
    sql_list = []
    for unv, where in zip(universe_list, where_clause_list):
        for var in var_list:
            sql_list.append(write_one_var(table, unv, var_name=var, output=output, where_clause=where))
    sql = '\n\nUNION ALL\n\n'.join(sql_list)
    sql = sql + '\nORDER BY 1,2,3;'
    if persistent:
        sql = 'DROP TABLE IF EXISTS {table};\nCREATE TABLE {table} AS\n'.format(table=table_name) + sql
    if local:
        sql = 'DROP TABLE IF EXISTS {table};\nCREATE LOCAL TEMPORARY TABLE {table} AS\n'.format(table=table_name) + sql
    if verbose:
        print(sql)
    return sql


layout = html.Div([
	# Options Menu:
	html.H3("Crosstabs"),
	html.Div([
		html.Div([
			html.Label("Schema:"),
			schema_dropdown,
			html.Label("Select Groups:"),
			group_selection_dropdown,
			], className = 'crosstabRow'),
		html.Div([
			html.Label("Universe:"),
			html.Div(universe_dropdown_influencers, id = "crosstab_union_influencers_dropdown_div"),
			html.Div(universe_dropdown_influencers_dev, id = "crosstab_union_influencers_dev_dropdown_div", style={'display': 'none'}),
			html.Label("Select Variables:"),
			var_selection_dropdown,
			], className = 'crosstabRow'),
		html.Div([
			html.Label("Basetable:"),
			html.Div(basetable_dropdown_influencers, id = "crosstab_basetable_influencers_dropdown_div"),
			html.Div(basetable_dropdown_influencers_dev, id = "crosstab_basetable_influencers_dev_dropdown_div", style={'display': 'none'}),
			html.Label("Filter On:"),
			filter_dropdown,
			], className = 'crosstabRow'),
		html.Div([
			html.Label("First Filter Selection:"),
			first_focused_filter_dropdown,
			html.Label("Second Filter Selection:"),
			second_focused_filter_dropdown,
			], className = 'crosstabRow'),
		html.Div([
			html.Div(id ='first-display-selected-values'),
			html.Div(id ='second-display-selected-values'),
			html.Div(id = 'display_num_cats')
		],
		className = 'crosstabOptions'
		),
	html.Br(),
	html.Button(
		id = 'crosstab_run',
		children = 'Run Crosstabs',
		type= 'submit'
		),
	html.Br(),
	html.Div(
		id='crosstab_results'
		),
	],
	style= {
        'display': 'flex',
        'flex-direction': 'column',
        'justify-content': 'center',
        'align-items': 'center',
        'resize': 'both',
        # 'overflow': 'auto',
    }
)])


# SWITCH BETWEEN DROPDOWNS BASED ON SCHEMA:
@app.callback(
	Output('crosstab_union_influencers_dropdown_div', 'style'),
	[Input('crosstab_schema_dropdown', 'value')]
	)
def update_crosstab_union_influencers_dropdown(value):
	if value == 'influencers':
		return {'display': 'block'}
	return {'display': 'none'}


@app.callback(
	Output('crosstab_union_influencers_dev_dropdown_div', 'style'),
	[Input('crosstab_schema_dropdown', 'value')]
	)
def update_crosstab_union_influencers_dropdown(value):
	if value == 'influencers_dev':
		return {'display': 'block'}
	return {'display': 'none'}


@app.callback(
	Output('crosstab_basetable_influencers_dropdown_div', 'style'),
	[Input('crosstab_schema_dropdown', 'value')]
	)
def update_crosstab_basetable_influencers_dropdown(value):
	if value == 'influencers':
		return {'display': 'block'}
	return {'display': 'none'}


@app.callback(
	Output('crosstab_basetable_influencers_dev_dropdown_div', 'style'),
	[Input('crosstab_schema_dropdown', 'value')]
	)
def update_crosstab_basetable_influencers_dropdown(value):
	if value == 'influencers_dev':
		return {'display': 'block'}
	return {'display': 'none'}

# GENERATE CROSSTABLE:
@app.callback(
	Output('crosstab_results', 'children'),
	[Input('crosstab_run', 'n_clicks')],
	[State('crosstab_schema_dropdown', 'value'),
	State('crosstab_union_influencers_dropdown', 'value'),
	State('crosstab_union_influencers_dev_dropdown', 'value'),
	State('crosstab_basetable_influencers_dropdown', 'value'),
	State('crosstab_basetable_influencers_dev_dropdown', 'value'),
	State('group_selection_dropdown', 'value'),
	State('var_selection_dropdown', 'value'),
	State('filter_dropdown', 'value'),
	State('first_focused_filter_dropdown', 'value'),
	State('second_focused_filter_dropdown', 'value')
	#State('')
	]
	)


def run_crosstabs(n_clicks, schema, union1, union2, basetable1, basetable2, groups, vars, filters, focused_filter, second_focused_filter):

	if n_clicks is None:
		return None

	if schema == 'influencers':
		union = union1
		basetable = basetable1
	elif schema == 'influencers_dev':
		union = union2
		basetable = basetable2
	else:
		return None

	where_clause_list = [True]
	output = groups
	output = ', '.join(output) 
	if cat_num == 0:
		table = "(SELECT a.*, b.* FROM {schema}.{union} a JOIN {schema}.{basetable} b USING (voterbase_id) WHERE influence > 0)".format(schema=schema, union=union, basetable=basetable)
	elif cat_num == 1:
		table = "(SELECT a.*, b.* FROM {schema}.{union} a JOIN {schema}.{basetable} b USING (voterbase_id) WHERE (influence > 0 AND {first[0]} = '{second}'))".format(schema=schema, union=union, basetable=basetable, first=filters, second=focused_filter)
	else:
		table = "(SELECT a.*, b.* FROM {schema}.{union} a JOIN {schema}.{basetable} b USING (voterbase_id) WHERE (influence > 0 AND {first[0]} = '{second}' AND {first[1]} = '{fourth}'))".format(schema=schema, union=union, basetable=basetable, first=filters, second=focused_filter, fourth=second_focused_filter)
	xtab_sql = write_all_vars(table, basetable, where_clause_list, [None] + vars, output=output)
	# try:
	xtabs = exec_query(xtab_sql, verbose=True)
	print(xtabs)
	# except:
		# return "There was an error fetching xtabs, make sure that the column is available in the universe you're using."

	return utils.get_table_from_df(xtabs)
		






