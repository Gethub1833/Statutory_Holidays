__author__ = 'shane'
from datetime import date, timedelta


def get_holiday(year):
    MARCH = 3
    weekday = get_actual(year).weekday()
    import Easter_Sunday
    # This holiday varies if easter falls on the same weekend
    easter_sunday = Easter_Sunday.get_actual(year)
    if easter_sunday.month == MARCH:
        pass

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
    MARCH=3
    return date(year,MARCH,23)

