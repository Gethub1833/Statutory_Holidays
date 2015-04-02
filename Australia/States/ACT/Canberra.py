__author__ = 'shane'
'''
Wikipedia
Canberra Day is a public holiday held annually on the second Monday in March
in the Australian Capital Territory (ACT) to celebrate the official naming of
Canberra. Canberra was named at a ceremony on 12 March 1913 by Lady Denman, the
wife of the then Governor-General Lord Denman. In 2012 Canberra Day falls on 12
March. In 2013 it falls on 11 March. On 3 March 2007, ACT Minister Andrew Barr
introduced a bill to change the day of Canberra Day to the second Monday in
March so it falls closer more often to the actual birthday of Canberra.[1]
Previously it had been held on the third Monday in March.
'''
from datetime import date, timedelta


def get_holiday(year):
    weekday = date(year, 3, 1).weekday()

    if weekday == 0:
        weekday = 7

    if year <= 2007:
        # Third Monday in March
        weekday = 21 - weekday

    else:
        # Second Monday in March
        weekday = 14 - weekday

    return date(year, 3, 1)+timedelta(days=weekday)

def get_actual(year):
    return date(year, 3, 12)