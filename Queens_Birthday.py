# coding: latin-1
__author__ = 'shane'

import datetime

'''
Queens Birthday
In New Zealand, the holiday is the first Monday in June.
Celebrations are mainly official, including the Queen's Birthday Honours list
and military ceremonies. There have been proposals, with some political
support, to replace the holiday with Matariki (Māori New Year) as an official
holiday. The idea of renaming the Queen's birthday weekend to Hillary weekend,
after Sir Edmund Hillary, the first person to ascend Mount Everest, was raised
in 2009.
'''

def get_holiday(year):
    '''
    Calculate the holiday date of ANZAC for the given year
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    JUNE = 6

    day_of_week = datetime.date(year, JUNE, 1).weekday()
    # Find the first Monday in June
    if day_of_week == 0:
        # Sunday so add one to the date
        return datetime.date(year, JUNE, 1+1)
    elif day_of_week == 1:
        # Monday, so already the first Monday of the month
        return datetime.date(year, JUNE, 1)
    else:
        # All other days, 8 - day of the week
        return datetime.date(year, JUNE, 8 - day_of_week)

def get_actual(year):
    return get_holiday(year)

