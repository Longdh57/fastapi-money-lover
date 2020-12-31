from datetime import datetime, timedelta


def get_from_date_and_to_date(month: int = datetime.today().month, year: int = datetime.today().year):
    if month and year:
        from_month = month-1 if month != 1 else 12
        from_year = year if month != 1 else (year-1)
        from_date = datetime.today().replace(day=25, month=from_month, year=from_year).date()
        to_date = datetime.today().replace(day=24, month=month, year=year).date()
        return from_date, to_date

    if datetime.today().day >= 25:
        from_date = datetime.today().replace(day=25).date()
        to_date = (datetime.today().replace(day=1) + timedelta(days=32)).replace(day=24).date()
    else:
        from_date = (datetime.today().replace(day=1) - timedelta(days=1)).replace(day=25).date()
        to_date = datetime.today().replace(day=24).date()
    return from_date, to_date
