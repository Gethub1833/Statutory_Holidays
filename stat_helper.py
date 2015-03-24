__author__ = 'shane'
from datetime import timedelta


def get_nearest_monday(holiday):
    weekday = holiday.weekday()
    if weekday == 0:
        # Sunday
        return holiday + timedelta(days=1)
    elif weekday in (1,2,3,4):
        # Monday, Tuesday, Wednesday, Thursday
        return holiday - timedelta(days=weekday-1)
    else:
        # Friday, Saturday
        return holiday + timedelta(days=8-weekday)