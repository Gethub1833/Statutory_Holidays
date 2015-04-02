__author__ = 'shane'
'''
The Holidays Act 1910 provides for the third Monday in May to be a public
holiday. Since 2006 this public holiday has been observed on the second Monday
in March through the issuing of a special Proclamation by the Governor.
'''
from datetime import date, timedelta


def get_holiday(year):
    weekday = date(year, 3, 1).weekday()
    if year < 2006:
        # Third Monday March
        correction = 21
    else:
        correction = 14
    if weekday == 0:
        weekday =7
    return date(year, 3, 1) + timedelta(days=correction-weekday)

def get_actual(year):
    return get_holiday(year)
