__author__ = 'shane'
import datetime
import stat_helper


def get_holiday(year):
    return stat_helper.get_nearest_monday(get_actual(year))


def get_actual(year):
    FEBRUARY=2
    return datetime.date(year,FEBRUARY,1)

