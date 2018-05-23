import dash_core_components as dcc
import dash_html_components as html

from db_creds import *
import config

# Custom Colored Strings:
def warn(string):
	print("\x1b[1;31m{}\x1b[0m".format(string))


# Helper Function for Table Dropdowns
def table_dropdown(
	id
	, schema
	, table
	, suppressions_list=["TRUE"]
	, default_value=0):

	suppressions_list = "AND ".join(suppressions_list)

	tables = exec_query("""
		SELECT table_name
		FROM information_schema.tables
		WHERE table_schema = '{schema}'
		AND table_name similar to '{table}'
		AND {suppressions_list}
	""".format(schema=schema, table=table, suppressions_list=suppressions_list)).table_name.as_matrix()

	try:
		return dcc.Dropdown(
			id = id,
			options = [
				{'label': table_name, 'value': table_name} for table_name in tables
			],
			value = tables[default_value]
			)
	except:
		warn("Failed to get {}".format(id))
		return dcc.Dropdown(id=id)



# Function that transforms a DF into an HTML Table

def get_table_from_df(df, max_rows = 500):
    # df = format_cols(df.head(max_rows))
    table = html.Table(
        [html.Tr([html.Th("Row Number")] + [html.Th(col) for col in df.columns])]
        +
        [html.Tr([html.Td(row+1)] + [html.Td(df.iloc[row][col]) for col in df.columns]) for row in range(df.shape[0])],
        id='myid',
        style={
            'height':'100%'
        }
    )
    print(table)
    return table


# Extract Table Info:
def get_latest_union(schema='influencers'):
	union = exec_query("SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema}' AND table_name similar to 'union_[0-9]{{8}}' ORDER BY 1 DESC LIMIT 1;".format(schema=schema))
	return union.iloc[0, 0]









