from datetime import date

from helpers.dash import slider_time_range


def test_slider_time_range():
    result = slider_time_range(date(2020, 2, 3), date(2020, 2, 28))
    expected = ["2020-02-03", "2020-02-10", "2020-02-17", "2020-02-24"]

    assert expected == result
