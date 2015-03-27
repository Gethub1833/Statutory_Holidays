__author__ = 'shane'
from datetime import date, timedelta


def get_holiday(year):
    MARCH=3
    # Second Monday in March, to avoid Easter
    weekday = date(year, MARCH, 1).weekday()
    # 0 +1
    if weekday == 0:
        day = 7
    else:
        day = 8 - weekday
    return date(year, MARCH, day) + timedelta(days=7)

def get_actual(year):
    MARCH=3
    return date(year, MARCH, 31)
