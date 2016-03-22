__author__ = 'shane'
from datetime import date
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from New_Zealand import ANZAC, Labour_day, Queens_Birthday, Waitangi
from Christmas_and_New_Year import Christmas, Boxing_day, New_Years_day, Day_After_New_Years
from Easter import Easter_Monday, Good_Friday


############
# Waitangi #
############
'''
Waitangi Day	6 February	Sunday 6 February	Monday 6 Feb	Wednesday 6 February	Thursday 6 February
'''
assert Waitangi.get_holiday(2001) == date(2001, 2, 6)
assert Waitangi.get_actual(2001) == date(2001, 2, 6)
assert Waitangi.get_holiday(2015) == date(2015, 2, 6)
assert Waitangi.get_actual(2015) == date(2015, 2, 6)
assert Waitangi.get_holiday(2016) == date(2016, 2, 8)
assert Waitangi.get_actual(2016) == date(2016, 2, 6)
#########
# ANZAC #
#########
'''
ANZAC Day	25 April	Monday 25 April	Wednesday 25 April	Thursday 25 April	Friday 25 April
'''
assert ANZAC.get_holiday(2001) == date(2001, 4, 25)
assert ANZAC.get_actual(2001) == date(2001, 4, 25)
assert ANZAC.get_holiday(2012) == date(2012, 4, 25)
assert ANZAC.get_actual(2012) == date(2012, 4, 25)
assert ANZAC.get_holiday(2015) == date(2015, 4, 27)
assert ANZAC.get_actual(2015) == date(2015, 4, 25)

###############
# Good Friday #
###############
'''Good Friday	varies	Friday 22 April	Friday 6 April	Friday 29 March	Friday 18 April'''
assert Good_Friday.get_holiday(2011) == date(2011, 4, 22)
assert Good_Friday.get_actual(2011) == date(2011, 4, 22)
# March Easter
assert Good_Friday.get_holiday(2013) == date(2013, 3, 29)
assert Good_Friday.get_actual(2013) == date(2013, 3, 29)
# April Easter
assert Good_Friday.get_holiday(2014) == date(2014, 4, 18)
assert Good_Friday.get_actual(2014) == date(2014, 4, 18)

#################
# Easter Monday #
#################
'''
Easter Monday	varies	Monday 25 April	Monday 9 April	Monday 1 April	Monday 21 April
'''
assert Easter_Monday.get_holiday(2011) == date(2011, 4, 25)
assert Easter_Monday.get_actual(2011) == date(2011, 4, 25)
# Sunday is in March
assert Easter_Monday.get_holiday(2013) == date(2013, 4, 1)
assert Easter_Monday.get_actual(2013) == date(2013, 4, 1)
assert Easter_Monday.get_holiday(2014) == date(2014, 4, 21)
assert Easter_Monday.get_actual(2014) == date(2014, 4, 21)

#################
# Easter Sunday #
#################
###################
# Queens Birthday #
###################
'''
Queen's Birthday	1st Monday in June	Monday 6 June	Monday 4 June	Monday 3 June	Monday 2 June
'''
assert Queens_Birthday.get_holiday(2011) == date(2011, 6, 6)
assert Queens_Birthday.get_actual(2011) == date(2011, 6, 6)
assert Queens_Birthday.get_holiday(2012) == date(2012, 6, 4)
assert Queens_Birthday.get_actual(2012) == date(2012, 6, 4)
assert Queens_Birthday.get_holiday(2015) == date(2015, 6, 2)
assert Queens_Birthday.get_actual(2015) == date(2015, 6, 2)

##############
# Labour Day #
##############
'''
Labour Day	4th Monday in October	Monday 24 October	Monday 22 October	Monday 28 October	Monday 27 October
'''
assert Labour_day.get_holiday(2011) == date(2011, 10, 24)
assert Labour_day.get_actual(2011) == date(2011, 10, 24)
assert Labour_day.get_holiday(2012) == date(2012, 10, 22)
assert Labour_day.get_actual(2012) == date(2012, 10, 22)
assert Labour_day.get_holiday(2015) == date(2015, 10, 26)
assert Labour_day.get_actual(2015) == date(2015, 10, 26)

##############
# Boxing Day #
##############
'''
Boxing Day	26 December	Monday 26 December	Wednesday 26 December	Thursday 26 December	Friday 26 December
'''
assert Boxing_day.get_holiday(2011) == date(2011, 12, 26)
assert Boxing_day.get_actual(2011) == date(2011, 12, 26)
assert Boxing_day.get_holiday(2012) == date(2012, 12, 26)
assert Boxing_day.get_actual(2012) == date(2012, 12, 26)
assert Boxing_day.get_holiday(2015) == date(2015, 12, 28)
assert Boxing_day.get_actual(2015) == date(2015, 12, 26)

#################
# Christmas_and_New_Year Day #
#################
'''
Christmas_and_New_Year Day	25 December	Sunday 25 December or Tuesday 27 December	Tuesday 25 December	Wednesday 25 December	Thursday 25 December
'''
assert Christmas.get_holiday(2011) == date(2011, 12, 27)
assert Christmas.get_actual(2011) == date(2011, 12, 25)
assert Christmas.get_holiday(2012) == date(2012, 12, 25)
assert Christmas.get_actual(2012) == date(2012, 12, 25)
assert Christmas.get_holiday(2015) == date(2015, 12, 25)
assert Christmas.get_actual(2015) == date(2015, 12, 25)

#######################
# Day After New Years #
#######################
'''
Day after New Year's Day	2 January	Sunday 2 January or Tuesday 4 January	Monday 2 Jan	Wednesday 2 January	Thursday 2 January
'''
assert Day_After_New_Years.get_holiday(2011) == date(2011, 1, 4)
assert Day_After_New_Years.get_actual(2011) == date(2011, 1, 2)
assert Day_After_New_Years.get_holiday(2012) == date(2012, 1, 2)
assert Day_After_New_Years.get_actual(2012) == date(2012, 1, 2)
assert Day_After_New_Years.get_holiday(2015) == date(2015, 1, 2)
assert Day_After_New_Years.get_actual(2015) == date(2015, 1, 2)

#############
# New Years #
#############
'''
New Year's Day	1 January	Saturday 1 January or Monday 3 January	Sunday 1 January or Tuesday 3 January	Tuesday 1 January	Wednesday 1 January
'''
assert New_Years_day.get_holiday(2011) == date(2011, 1, 3)
assert New_Years_day.get_actual(2011) == date(2011, 1, 1)
assert New_Years_day.get_holiday(2012) == date(2012, 1, 3)
assert New_Years_day.get_actual(2012) == date(2012, 1, 1)
assert New_Years_day.get_holiday(2015) == date(2015, 1, 1)
assert New_Years_day.get_actual(2015) == date(2015, 1, 1)
