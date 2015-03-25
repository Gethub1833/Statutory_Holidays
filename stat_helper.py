__author__ = 'shane'
from datetime import timedelta


def get_nearest_monday(holiday):
    weekday = holiday.weekday()
    if weekday in (0,1,2,3):
        # Monday, Tuesday, Wednesday, Thursday
        return holiday - timedelta(days=weekday)
    else:
        # Friday, Saturday
        return holiday + timedelta(days=7-weekday)