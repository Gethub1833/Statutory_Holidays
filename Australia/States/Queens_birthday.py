__author__ = 'shane'
'''Second Monday in June, except for Western Australia which uses Fourth Monday in September'''
from datetime import date, timedelta


def get_holiday(year):
    return date(year, 6, 1) + timedelta(days=7-date(year, 6, 1).weekday())

def get_actual(year):
    return get_holiday(year)