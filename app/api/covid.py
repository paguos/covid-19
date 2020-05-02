import requests

from datetime import datetime

API_ENDPOINT = "https://api.covid19api.com"


class CovidAPI:
    def __init__(self, from_date: str, to_date: str):
        self.from_date = from_date
        self.to_date = to_date

    def by_country(
        self, country, status="confirmed", chart_type="lines",
    ):
        payload = {
            "from": _format_date(self.from_date),
            "to": _format_date(self.to_date),
        }

        response = requests.get(
            f"{API_ENDPOINT}/country/{country}/status/{status}", params=payload
        )

        response_payload = response.json()
        aggregated_data = _aggregate_data(response_payload)

        return {
            "x": [
                date for date in aggregated_data.keys()
                if "0001-01-01" not in date
            ],
            "y": [
                cases
                for date, cases in aggregated_data.items()
                if "0001-01-01" not in date
            ],
            "type": chart_type,
            "name": country,
        }


def _aggregate_data(response_payload):
    aggregated_data = {}
    for entry in response_payload:
        date = _simplify_date(entry["Date"])
        if date in aggregated_data:
            aggregated_data[date] = aggregated_data[date] + entry["Cases"]
        else:
            aggregated_data[date] = entry["Cases"]
    return aggregated_data


def _format_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return datetime.strftime(date, "%Y-%m-%dT%H:%M:%SZ")


def _simplify_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    return datetime.strftime(date, "%Y-%m-%d")
