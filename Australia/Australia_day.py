__author__ = 'shane'
from datetime import date, timedelta

def get_holiday(year):
    weekday = get_actual(year).weekday()
    if weekday in (5, 6):
        #Mondayise
        return get_actual(year)+timedelta(days=7-weekday)
    else:
        return get_actual(year)


def get_actual(year):
    return date(year, 1, 26)