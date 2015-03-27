__author__ = 'shane'
from datetime import timedelta
from Easter import Easter_Sunday


def get_holiday(year):
    return get_actual(year)


def get_actual(year):
    return Easter_Sunday.get_actual(year)-timedelta(days=1)
