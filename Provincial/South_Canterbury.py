__author__ = 'shane'
'''
South Canterbury	25 September	Fourth Monday in September — Dominion Day
'''
from datetime import date


def get_holiday(year):
    SEPTEMBER=9
    # Fourth Monday in SEPTEMBER
    weekday = date(year, SEPTEMBER, 1).weekday()
    # 0 +1
    if weekday == 0:
        day = weekday + 29
    # 1 = 1
    elif weekday == 1:
        day = weekday + 28
    #8 - weekday
    else:
        day = (8 - weekday) + 21
    return date(year, SEPTEMBER, day)

def get_actual(year):
    SEPTEMBER=9
    return date(year, SEPTEMBER, 25)
