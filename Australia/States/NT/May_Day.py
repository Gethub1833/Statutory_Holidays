__author__ = 'shane'
''' First Monday in May '''
from datetime import date, timedelta


def get_holiday(year):
    return date(year, 5, 1) + timedelta(days=7-date(year, 5, 1).weekday())

def get_actual(year):
    return get_holiday(year)