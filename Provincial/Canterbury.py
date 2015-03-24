__author__ = 'shane'
'''
Canterbury	Christchurch, Ashburton	16 December	Christchurch Show Day (Northern Canterbury)
Christchurch Show Day (Central Canterbury)
Second Friday after the first Tuesday in November (Christchurch City) — to coincide with the Agricultural and Pastoral Show.
'''
from datetime import timedelta, date

def get_holiday(year):
    NOVEMBER = 11
    # First Tuesday in NOVEMBER
    weekday = date(year, NOVEMBER, 1).weekday()
    # 0 +1
    if weekday in (0,1):
        weekday += 2-weekday
    #
    elif weekday == 2:
        pass
    # 9 - weekday
    else:
        weekday = (9 - weekday)
    # return second Friday after first Tuesday
    return date(year, NOVEMBER, weekday)+timedelta(days=10)


def get_actual(year):
    DECEMBER = 12
    return date(year, DECEMBER, 16)
