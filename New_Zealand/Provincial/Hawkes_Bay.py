__author__ = 'shane'
'''
Hawke's Bay	Napier, Hastings	1 November	Friday before Labour Day
'''
from datetime import date, timedelta
import Labour_day

def get_holiday(year):
    return Labour_day.get_holiday(year) - timedelta(days=3)

def get_actual(year):
    NOVEMBER=11
    return date(year, NOVEMBER, 1)
