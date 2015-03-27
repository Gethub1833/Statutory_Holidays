__author__ = 'shane'
from datetime import timedelta

from Easter import Easter_Sunday


def get_holiday(year):
    # Return the friday before Easter Sunday
    return Easter_Sunday.get_holiday(year)-timedelta(days=2)


def get_actual(year):
    return get_holiday(year)