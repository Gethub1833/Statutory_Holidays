import datetime
import astropy

'''Day After New Years day is celebrated on the 2nd of January, each year.
However if the 2nd falls on the weekend then the holiday will be on the following Monday or Tuesday.
Day After New Years Day is observed on the 4th if the 2nd falls on a Saturday or Sunday
'''

def get_holiday(year):
    '''
    Calculate the observed date of New Years day for the given year
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    JANUARY = 1

    if datetime.date(year, JANUARY, 2).weekday() in (5,6):
        # New Years falls on the weekend
        return datetime.date(year, JANUARY, 4)
    else:
        return datetime.date(year, JANUARY, 1)

def get_actual(year):
    '''
    Day after New Years Day is always celebrated on the 1st of January
    :param year: int
    :return: datetime object set for the observed date
    '''

    if year < 1:
        raise ValueError("Year must be > 1")

    JANUARY = 1

    return datetime.date(year, JANUARY, 2)
