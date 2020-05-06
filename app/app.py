import dash
import flask
import yaml

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import date

from api.covid import CovidAPI
from helpers.colors import colors
from helpers.dash import slider_time_range
from helpers.graph import covid_graph

server = flask.Flask(__name__)  # define flask app.server
app = dash.Dash(__name__, server=server)
slider_dates = slider_time_range(date(2020, 2, 6))


app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    className="main",
    children=[
        html.H1(
            children="COVID Dash",
            style={"textAlign": "center", "color": colors["title"]},
        ),
        html.Div(
            children="A web application to navigate threw the covid-19 data.",
            style={"textAlign": "center", "color": colors["text"]},
            className="container",
        ),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Confirmed", "value": "confirmed"},
                {"label": "Recovered", "value": "recovered"},
                {"label": "Deaths", "value": "deaths"},
            ],
            value="confirmed",
            style={
                "textAlign": "left",
                "backgroundColor": colors["background"],
            },
            className="dropdown",
        ),
        dcc.Graph(
            id="covid-graph",
            style={"backgroundColor": colors["background"]},
            figure={"layout": covid_graph(colors)},
        ),
        dcc.RangeSlider(
            id="date-slider",
            min=0,
            max=len(slider_dates),
            value=[0, len(slider_dates)],
            marks={i: slider_dates[i] for i in range(0, len(slider_dates))},
            step=None,
        ),
    ],
)


@app.callback(
    Output(component_id="covid-graph", component_property="figure"),
    [
        Input(component_id="dropdown", component_property="value"),
        Input(component_id="date-slider", component_property="value"),
    ],
)
def update_output_div(input_value, slider):
    api = CovidAPI(slider_dates[slider[0]], slider_dates[slider[1] - 1])

    with open("configs/countries.yml") as file:
        countries = yaml.full_load(file)["countries"]

    return {
        "data": [
            api.by_country(country, status=input_value)
            for country in countries
        ],
        "layout": covid_graph(colors),
    }


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
