from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Step 3: Initialize Flask and Dash Apps
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Step 4: Sample Data
data_x = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
bar_values = [5, 10, 15, 20, 25]
line_values = [15, 23, 5, 10, 35]

# Step 5: Create Bar Chart and Line Chart Using Plotly
bar_chart = go.Figure(go.Bar(x=data_x, y=bar_values, name='Bar Chart'))
line_chart = go.Figure(go.Scatter(x=data_x, y=line_values, mode='lines+markers', name='Line Chart'))

# Step 6: Dash Layout for Graphs and KPIs
app.layout = html.Div([
    dbc.Container([
        html.H1("Dashboard with Bar and Line Graphs"),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Total Sales"),
                    html.H2("1,234")
                ], className="kpi-card"),
            ], width=4),
            dbc.Col([
                html.Div([
                    html.H5("New Customers"),
                    html.H2("567")
                ], className="kpi-card"),
            ], width=4),
            dbc.Col([
                html.Div([
                    html.H5("Revenue"),
                    html.H2("$8,910")
                ], className="kpi-card"),
            ], width=4),
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=bar_chart), width=6),
            dbc.Col(dcc.Graph(figure=line_chart), width=6),
        ]),
    ])
])

# Step 7: Flask Route
@server.route('/')
def index():
    return render_template('index.html')

# Step 8: Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
