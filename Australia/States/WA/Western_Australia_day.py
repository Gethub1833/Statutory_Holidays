__author__ = 'shane'
'''First Monday in June'''
from datetime import date, timedelta


def get_holiday(year):
    weekday = date(year, 11, 1).weekday()
    correction = 7
    if weekday == 0:
        weekday =7
    return date(year, 11, 1) + timedelta(days=correction-weekday)

def get_actual(year):
    return get_holiday(year)
