__author__ = 'shane'
import datetime


def get_holiday(year):
    weekday = get_actual(year).weekday()
    if weekday == 0:
        # Sunday
        return get_actual(year)+datetime.timedelta(days=1)
    elif weekday in (1,2,3,4):
        # Monday, Tuesday, Wednesday, Thursday
        return get_actual(year)-datetime.timedelta(days=weekday-1)
    else:
        # Friday, Saturday
        return get_actual(year)+datetime.timedelta(days=8-weekday)

def get_actual(year):
    FEBRUARY=2
    return datetime.date(year,FEBRUARY,1)

