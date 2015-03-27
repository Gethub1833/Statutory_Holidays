__author__ = 'shane'
'''
South Canterbury 25 September Fourth Monday in September - Dominion Day
'''
from datetime import date


def get_holiday(year):
    SEPTEMBER=9
    # Fourth Monday in SEPTEMBER
    weekday = date(year, SEPTEMBER, 1).weekday()
    if weekday == 0:
        weekday = 7
    day = (8 - weekday) + 21
    return date(year, SEPTEMBER, day)

def get_actual(year):
    DECEMBER=12
    return date(year, DECEMBER, 16)
