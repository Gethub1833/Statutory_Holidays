import datetime

'''Waitangi day is celebrated on the 6th of February, each year.
From 1 January 2014 the public holiday for ANZAC Day and Waitangi Day will be Mondayised if they fall on a Saturday or Sunday.

This means, if Waitangi Day or ANZAC Day fall on a Saturday or Sunday:

For employees who would not otherwise work on that Saturday or Sunday, the public holiday must be treated as falling on the following Monday.
For employees who would otherwise work on that Saturday or Sunday, the public holiday must be treated as falling on that day.
'''

def get_holiday(year):
    '''
    Calculate the observed date of Christmas_and_New_Year for the given year
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    FEBRUARY = 2

    day_of_week = datetime.date(year, FEBRUARY, 6).weekday()
    if year >= 2014:
        # Mondayise if Waitangi day falls on the weekend
        if day_of_week == 6:
            # Waitangi day fell on a Sunday
            return datetime.date(year, FEBRUARY, 7)
        elif day_of_week == 5:
            # Saturday
            return datetime.date(year, FEBRUARY, 8)
        else:
            return datetime.date(year, FEBRUARY, 6)
    else:
        return datetime.date(year, FEBRUARY, 6)

def get_actual(year):
    '''
    Waitangi is always celebrated on the 6th of February
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    FEBRUARY = 2

    return datetime.date(year, FEBRUARY, 6)
