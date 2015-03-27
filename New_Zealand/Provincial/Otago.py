__author__ = 'shane'
from datetime import date, timedelta

import stat_helper


def get_holiday(year):
    MARCH = 3
    weekday = get_actual(year).weekday()
    import Easter_Sunday
    # This holiday varies if easter falls on the same weekend
    easter_sunday = Easter_Sunday.get_actual(year)
    if easter_sunday.month == MARCH and easter_sunday.day in range(22, 26):
        # Easter and Otago anniversary collide
        '''
        For the first time in nearly 100 years Easter is coming at its earliest
        on Sunday, March 23, 2008. The last time Easter Sunday fell on March 23
        was in 1913. However, Easter can occur earlier than March 23. The
        earliest Easter ever recorded in the Gregorian calendar from 1753
        onwards was on March 22, both in 1761 and 1818.

        The next time Easter occurs on March 23 will not be until 2160, and a
        March 22 Easter will not happen until the year 2285. The Easter date is
        set around the time of the vernal, or spring, equinox, when the length
        of day and night is nearly equal in every part of the world. Easter
        Sunday celebrates the resurrection of Jesus, according to Christian
        belief.
        '''
        return stat_helper.get_nearest_monday(get_actual(year))+timedelta(days=1)
    else:
        return stat_helper.get_nearest_monday(get_actual(year))


def get_actual(year):
    MARCH=3
    return date(year,MARCH,23)

