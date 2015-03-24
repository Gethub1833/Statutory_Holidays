__author__ = 'shane'
from datetime import date, timedelta

import stat_helper


def get_holiday(year):
    MARCH = 3
    weekday = get_actual(year).weekday()
    import Easter_Sunday
    # This holiday varies if easter falls on the same weekend
    easter_sunday = Easter_Sunday.get_actual(year)
    if easter_sunday.month == MARCH and easter_sunday.day in range(20, 28):
        # Easter and Otago anniversary collide
        return stat_helper.get_nearest_monday(get_actual(year))-timedelta(days=7)
    else:
        return stat_helper.get_nearest_monday(get_actual(year))


def get_actual(year):
    MARCH=3
    return date(year,MARCH,23)

