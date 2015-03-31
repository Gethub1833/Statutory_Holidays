__author__ = 'shane'
'''First Monday in October'''
from datetime import date, timedelta


def get_holiday(year):
    weekday = date(year, 10, 1).weekday()
    if weekday == 0:
        weekday += 7

    return date(year, 10, 1) + timedelta(days= 7 - weekday)

def get_actual(year):
    return get_holiday(year)