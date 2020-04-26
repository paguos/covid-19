import datetime


def slider_time_range(
    start_date: datetime.date, end_date=datetime.datetime.now().date()
):
    dates = []
    while start_date < end_date:
        dates.append(start_date)
        start_date = start_date + datetime.timedelta(days=7)

    return [datetime.datetime.strftime(date, "%Y-%m-%d") for date in dates]
