# -*- coding: utf-8 -*-
__author__ = 'shane'
'''
Canterbury Christchurch, Ashburton 16 December Christchurch Show Day (Northern Canterbury)
Christchurch Show Day (Central Canterbury)
Second Friday after the first Tuesday in November (Christchurch City) - to coincide with
the Agricultural and Pastoral Show.
'''
from datetime import timedelta, date

def get_holiday(year):
    NOVEMBER = 11
    # First Tuesday in NOVEMBER
    weekday = date(year, NOVEMBER, 1).weekday()
    # 0 +1
    if weekday in (0, 1):
        # Monday and Tuesday
        correction = weekday + 1-weekday
    else:
        # Wednesday, Thursday, Friday, Saturday, Sunday
        correction = weekday + (6 - weekday)
    # return second Friday after first Tuesday
    return date(year, NOVEMBER, 1)+timedelta(days=correction+10)


def get_actual(year):
    DECEMBER = 12
    return date(year, DECEMBER, 16)
