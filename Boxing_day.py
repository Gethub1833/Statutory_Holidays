import datetime
import astropy

'''Boxing day is celebrated on the 26th of December, each year.
If Boxing day falls on the weekend it is moved to the following Monday or Tuesday
Boxing Day is observed on the 28th if the 26th falls on a Saturday or Sunday
'''

def get_holiday(year):
    '''
    Calculate the observed date of Boxing day for the given year
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    DECEMBER = 12

    if datetime.date(year, DECEMBER, 26).weekday() in (5,6):
        # Christmas falls on the weekend
        return datetime.date(year, DECEMBER, 28)
    else:
        return datetime.date(year, DECEMBER, 26)

def get_actual(year):
    '''
    Boxing Day is always celebrated on the 26th of December
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    DECEMBER = 12

    return datetime.date(year, DECEMBER, 26)
