__author__ = 'shane'
from datetime import date, timedelta


def get_holiday(year):
    import Easter_Monday
    return Easter_Monday.get_holiday(year) + timedelta(days=1)

def get_actual(year):
    MARCH=3
    return date(year,MARCH,25)
