from datetime import date

'''ANZAC day is celebrated on the 25th of APRIL, each year.
Starting from 2014 ANZAC day was Mondayised, that is, if ANZAC day falls on the weekend,
the holiday is moved to the following Monday.
ANZAC is observed on the 27th if the 25th falls on a Saturday, 26th if it falls on a Sunday
'''

def get_holiday(year):
    '''
    Calculate the holiday date of ANZAC for the given year
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    APRIL = 4

    day_of_week = date(year, APRIL, 25).weekday()
    if year >= 2014:
        if day_of_week == 6:
            # ANZAC day fell on a Sunday
            return date(year, APRIL, 26)
        elif day_of_week == 5:
            # Saturday
            return date(year, APRIL, 27)
        else:
            return date(year, APRIL, 25)
    else:
        return date(year, APRIL, 25)

def get_actual(year):
    '''
    ANZAC day is always celebrated on the 25th of APRIL
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    APRIL = 4

    return date(year, APRIL, 25)
