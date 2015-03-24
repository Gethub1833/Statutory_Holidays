__author__ = 'shane'
'''
Chatham Islands	30 November	Monday nearest to the actual day
'''
from datetime import date, timedelta

def get_holiday(year):
    weekday = get_actual(year).weekday()
    if weekday == 0:
        # Sunday
        return get_actual(year) + timedelta(days=1)
    elif weekday in (1,2,3,4):
        # Monday, Tuesday, Wednesday, Thursday
        return get_actual(year) - timedelta(days=weekday-1)
    else:
        # Friday, Saturday
        return get_actual(year) + timedelta(days=8-weekday)

def get_actual(year):
    NOVEMBER=11
    return date(year,NOVEMBER,30)