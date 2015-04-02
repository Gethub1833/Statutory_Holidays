__author__ = 'shane'
'''
Family & Community Day was celebrated on the first Tuesday of November in 2007, 2008 and 2009, coinciding with the Melbourne Cup. This public holiday was declared in 2007 under section 3(1)(b) of the Holidays Act 1953 (ACT). It was announced in 2008 that it would continue on Melbourne Cup Day in 2008 and 2009. Mr. Andrew Barr, the ACT Minister for Industrial Relations stated the purpose of the new public holiday was:

"...to enable workers to take a break from their hectic working lives and to spend some quality time with their family and friends. ... Australians do work the longest hours of any country in the western world. We do deserve a break."[1]

The ACT's Minister for Industrial Relations John Hargreaves announced in August 2009 that the territory's Family and Community Day would move to a different date from 2010 onwards.

Hargreaves announced that Family and Community Day would be on the first Monday of the September/October
school holidays in 2010 (Monday, September 27, 2010).
"However, in future years where the first Monday of the school holidays falls on the currently designated
Labour Day public holiday, such as will occur in 2011 and 2012, the Family and Community Day will be moved to the
second Monday of the term break".

The Family and Community Day public holiday will fall on the following dates in the next few years:

2010 - Monday, 26 September

2011 - Monday, 10 October

2012 - Monday, 8 October

2013 - Monday, 30 September

2014 - Monday, 29 September

2015 - Monday, 28 September

2016 - Monday 26 September
'''
from datetime import date, timedelta
import warnings


def get_holiday(year):
    if year in (2007, 2008, 2009):
        # First Tuesday in November
        weekday = date(year, 11, 1).weekday()
        if weekday in (0, 1):
            weekday += 8
        return date(year, 11, 1)+timedelta(days=8-weekday)
    elif year in (2011, 2012):
        # Second monday in October
        weekday = date(year, 10, 1).weekday()
        if weekday in (0):
            return date(year, 10, 1) + timedelta(days=7)
        else:
            return date(year, 10, 1,) + timedelta(days=7-weekday+7)
    else:
        # Need to know the school holiday algorithm
        warnings.warn("This information may be incorrect as there is no documented algorithm for this holiday")
        # returning the 4th Monday in September
        return date(year, 9, 1) + timedelta(days=28-date(year, 9, 1).weekday())

def get_actual(year):
    return get_holiday(year)