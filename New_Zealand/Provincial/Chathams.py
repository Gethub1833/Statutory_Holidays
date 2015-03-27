__author__ = 'shane'
'''
Chatham Islands	30 November	Monday nearest to the actual day
'''
from datetime import date
import stat_helper


def get_holiday(year):
    return stat_helper.get_nearest_monday(get_actual(year))


def get_actual(year):
    NOVEMBER = 11
    return date(year, NOVEMBER, 30)