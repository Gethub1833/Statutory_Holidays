__author__ = 'shane'
from New_Zealand import ANZAC, Labour_day, Queens_Birthday, Waitangi
from Christmas_and_New_Year import Boxing_day, Christmas, New_Years_day, Day_After_New_Years
from Easter import Easter_Monday, Good_Friday


def get_national_holidays(year):
    '''Get all of the National holidays for the given year

        Return: dictionary of holiday dates
    '''

    return {'ANZAC Day': ANZAC.get_holiday(year),
            'Boxing Day': Boxing_day.get_holiday(year),
            'Christmas': Christmas.get_holiday(year),
            'Day After New Years': Day_After_New_Years.get_holiday(year),
            'Easter Monday': Easter_Monday.get_holiday(year),
            'Good Friday': Good_Friday.get_holiday(year),
            'Labour Day': Labour_day.get_holiday(year),
            'New Years Day': New_Years_day.get_holiday(year),
            'Queens Birthday': Queens_Birthday.get_holiday(year),
            'Waitangi Day': Waitangi.get_holiday(year)
            }