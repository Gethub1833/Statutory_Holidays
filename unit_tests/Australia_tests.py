__author__ = 'shane'
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Australia import Australia_day, Easter_Saturday, ANZAC
from Christmas_and_New_Year import New_Years_day, Christmas, Boxing_day
from Easter import Good_Friday, Easter_Monday
from datetime import date


#############
# Australia #
#############
assert Australia_day.get_holiday(2015) == date(2015, 1, 26)

###################
# Easter Saturday #
###################
assert Easter_Saturday.get_holiday(2015) == date(2015, 4, 4)


#############
# ANZAC Day #
#############
assert ANZAC.get_actual(2015) == date(2015, 4, 25)
assert ANZAC.get_holiday(2015) == date(2015, 4, 27)

# Christmas, Boxing Day, and New Years day, and Easter are well tested, so all
# we need to test is that we can call them properly

#############
# New Years #
#############
assert New_Years_day.get_holiday(2015) == date(2015, 1, 1)
assert New_Years_day.get_actual(2015) == date(2015, 1, 1)

#############
# Christmas #
#############
assert Christmas.get_holiday(2015) == date(2015, 12, 25)
assert Christmas.get_actual(2015) == date(2015, 12, 25)

##############
# Boxing Day #
##############
# AKA Proclamation day
assert Boxing_day.get_holiday(2015) == date(2015, 12, 28)
assert Boxing_day.get_actual(2015) == date(2015, 12, 26)

###############
# Good Friday #
###############
assert Good_Friday.get_actual(2015) == date(2015, 4, 3)
assert Good_Friday.get_holiday(2015) == date(2015, 4, 3)

#################
# Easter Monday #
#################
assert Easter_Monday.get_actual(2015) == date(2015, 4, 6)
assert Easter_Monday.get_holiday(2015) == date(2015, 4, 6)
'''
National Public Holidays 2015

Our National Public Holidays are New Year's Day, Australia Day, Good Friday, Easter Monday, Anzac Day, Christmas_and_New_Year Day and Boxing Day. All other public holidays such as Queen's Birthday and Labour Day are individually declared by the state and territory governments.

Thursday 1 January: New Year's Day
Monday 26 January: Australia Day
Friday 3 April: Good Friday
Saturday 4 April: Easter Saturday
Monday 6 April: Easter Monday
Saturday 25 April: Anzac Day
Friday 25: December Christmas Day
Monday 28 December**: Boxing Day

**Substitute for Boxing Day 26 December 2015.
'''
