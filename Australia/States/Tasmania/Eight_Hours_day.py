__author__ = 'shane'
'''Second Monday in March'''

from datetime import date, timedelta


def get_holiday(year):
    weekday = date(year, 3, 1).weekday()
    correction = 21
    if weekday == 0:
        weekday =7
    return date(year, 3, 1) + timedelta(days=correction-weekday)

def get_actual(year):
    return get_holiday(year)

