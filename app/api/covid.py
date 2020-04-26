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
        return {
            "x": [
                _simplify_date(entry["Date"])
                for entry in response_payload
                if "0001-01-01" not in entry["Date"]
            ],
            "y": [
                entry["Cases"]
                for entry in response_payload
                if "0001-01-01" not in entry["Date"]
            ],
            "type": chart_type,
            "name": country,
        }


def _format_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return datetime.strftime(date, "%Y-%m-%dT%H:%M:%SZ")


def _simplify_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    return datetime.strftime(date, "%Y-%m-%d")
