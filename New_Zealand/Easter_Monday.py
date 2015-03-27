__author__ = 'shane'
import Easter_Sunday
from datetime import timedelta

def get_holiday(year):
    # Return the Monday after Easter Sunday
    return Easter_Sunday.get_holiday(year)+timedelta(days=1)


def get_actual(year):
    return get_holiday(year)