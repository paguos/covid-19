from pytest import fixture
from unittest.mock import Mock
from unittest.mock import patch

from api.covid import CovidAPI


@fixture
def mocked_get():
    data = [
        {
            "Country": "Test",
            "CountryCode": "TS",
            "Lat": "0.0",
            "Lon": "0.0",
            "Cases": 0,
            "Status": "confirmed",
            "Date": "2020-03-01T00:00:00Z",
        },
        {
            "Country": "Test",
            "CountryCode": "TS",
            "Lat": "0.0",
            "Lon": "0.0",
            "Cases": 1,
            "Status": "confirmed",
            "Date": "2020-03-02T00:00:00Z",
        },
        {
            "Country": "Test",
            "CountryCode": "TS",
            "Lat": "0.0",
            "Lon": "0.0",
            "Cases": 1,
            "Status": "confirmed",
            "Date": "2020-03-02T01:00:00Z",
        },
        {
            "Country": "Test",
            "CountryCode": "TS",
            "Lat": "0.0",
            "Lon": "0.0",
            "Cases": 3,
            "Status": "confirmed",
            "Date": "2020-03-03T00:00:00Z",
        },
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = data
        yield mock_get


def test_by_country(mocked_get):
    api = CovidAPI("2020-03-01", "2020-03-03")
    result = api.by_country("test")

    mocked_get.assert_called_with(
        "https://api.covid19api.com/country/test/status/confirmed",
        params={"from": "2020-03-01T00:00:00Z", "to": "2020-03-03T00:00:00Z"},
    )

    expected = {
        "x": ["2020-03-01", "2020-03-02", "2020-03-03"],
        "y": [0, 2, 3],
        "type": "lines",
        "name": "test",
    }

    assert result == expected
