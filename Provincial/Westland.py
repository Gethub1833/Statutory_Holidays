__author__ = 'shane'
'''
Westland	Hokitika, Greymouth	1 December	Monday nearest to the actual day (Greymouth)
Varies (outside Greymouth)
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
    DECEMBER=12
    return date(year,DECEMBER,1)