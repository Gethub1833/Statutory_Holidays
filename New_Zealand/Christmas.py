import datetime
import astropy

'''Christmas day is celebrated on the 25th of December, each year.
If Christmas day falls on the weekend then the holiday is the following Monday or Tuesday
Christmas is observed on the 27th if the 25th falls on a Saturday or Sunday
'''

def get_holiday(year):
    '''
    Calculate the observed date of Christmas for the given year
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    DECEMBER = 12

    if datetime.date(year, DECEMBER, 25).weekday() in (5,6):
        # Christmas falls on the weekend
        return datetime.date(year, DECEMBER, 27)
    else:
        return datetime.date(year, DECEMBER, 25)

def get_actual(year):
    '''
    Christmas is always celebrated on the 25th of December
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    DECEMBER = 12

    return datetime.date(year, DECEMBER, 25)
