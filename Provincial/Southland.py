__author__ = 'shane'
from datetime import date, timedelta


def get_holiday(year):
    if year > 2011:
        import Easter_Monday
        return Easter_Monday.get_holiday(year) + timedelta(days=1)
    else:
        return get_actual(year)

def get_actual(year):
    JANUARY = 1
    return date(year, JANUARY, 17)
