__author__ = 'shane'
'''
Marlborough	Blenheim, Picton	1 November	First Monday after Labour Day
'''
from datetime import date, timedelta
import Labour_day

def get_holiday(year):
    return Labour_day.get_holiday(year) + timedelta(days=7)

def get_actual(year):
    NOVEMBER=11
    return date(year, NOVEMBER, 1)
