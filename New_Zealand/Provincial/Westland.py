__author__ = 'shane'
'''
Westland	Hokitika, Greymouth	1 December	Monday nearest to the actual day (Greymouth)
Varies (outside Greymouth)
'''
from datetime import date
import stat_helper


def get_holiday(year):
    return stat_helper.get_nearest_monday(get_actual(year))


def get_actual(year):
    DECEMBER = 12
    return date(year, DECEMBER, 1)