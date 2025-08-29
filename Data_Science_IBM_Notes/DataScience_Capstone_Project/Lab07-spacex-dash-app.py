# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                 ],
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True),

    html.Br(),
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),

    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                    value=[min_payload, max_payload]),

    html.Br(),
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

# TASK 2: Add a callback function for pie chart
# Callback to update pie chart based on dropdown selection
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Pie chart showing total successful launches by launch site
        fig = px.pie(
            spacex_df[spacex_df['class'] == 1],  # Filter only successful launches
            names='Launch Site',
            title='Total Successful Launches by Site'
        )
        return fig
    else:
        # Filter the dataframe for the selected launch site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        print(filtered_df.shape)
        print(filtered_df['class'].value_counts())
        print("1", spacex_df['Launch Site'].unique())

        # Count success (1) and failure (0)
        class_counts = filtered_df['class'].value_counts().reset_index()
        class_counts.columns = ['Outcome', 'Count']
        class_counts['Outcome'] = class_counts['Outcome'].map({1: 'Success', 0: 'Failure'})
        print(class_counts)

        # Create pie chart for selected launch site
        fig = px.pie(
            class_counts,
            names='Outcome',
            values='Count',
            title=f'Success vs. Failure Launches for {entered_site}'
        )
        return fig

# TASK 4: Add a callback function for scatter plot
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id="payload-slider", component_property="value")]
)
def get_scatter_plot(entered_site, payload_range):
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                             (spacex_df['Payload Mass (kg)'] <= payload_range[1])]

    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title='Payload vs Outcome for All Sites')
    else:
        site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(site_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title=f'Payload vs Outcome for site {entered_site}')

    return fig

# Run the app
if __name__ == '__main__':
    app.run()
