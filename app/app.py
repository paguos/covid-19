import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import date

from api.covid import CovidAPI
from helpers.dash import slider_time_range

app = dash.Dash(__name__)
slider_dates = slider_time_range(date(2020, 2, 6))


app.layout = html.Div(
    children=[
        html.H1(children="Covid Dash", style={"textAlign": "center"},),
        html.Div(
            children="A web application to navigate threw the covid-19 data.",
            style={"textAlign": "center"},
        ),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Confirmed", "value": "confirmed"},
                {"label": "Recovered", "value": "recovered"},
                {"label": "Deaths", "value": "deaths"},
            ],
            value="confirmed",
            style={"textAlign": "left"},
        ),
        dcc.Graph(id="covid-graph",),
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
    data = [
        api.by_country("Germany", status=input_value),
        api.by_country("Italy", status=input_value),
        api.by_country("Spain", status=input_value),
    ]
    return {
        "data": data,
        "layout": {"xaxis": {"tickformat": "%Y-%m-%d"}},
    }


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
