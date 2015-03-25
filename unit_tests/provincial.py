__author__ = 'shane'
import pytest
from Provincial import Auckland, Canterbury, Chathams, Hawkes_Bay, \
    Marlborough, Nelson, Otago, South_Canterbury, Southland, Taranaki, Wellington, Westland

############
# AUCKLAND #
############

'''
Test Dates
Auckland Anniversary Day
Also called	Northland Anniversary Day (locally in the region)
Observed by	former Auckland Province, New Zealand
Date	Monday closest to 29 January
2014 date	27 January
2015 date	26 January
2016 date	1 February
2017 date	30 January
Frequency	annual
'''

# In 2016 the holiday falls in February
sut = Auckland.get_holiday(2016)
assert sut.year == 2016
assert sut.month == 2
assert sut.day == 1
assert sut.weekday() == 0

# But the actual day remains in January
sut = Auckland.get_actual(2016)
assert sut.year == 2016
assert sut.month == 1
assert sut.day == 29
assert sut.weekday() == 4

# In 2014 the holiday fell in January
sut = Auckland.get_holiday(2014)
assert sut.year == 2014
assert sut.month == 1
assert sut.day == 27
assert sut.weekday() == 0
# But the actual day remains in January
sut = Auckland.get_actual(2014)
assert sut.year == 2014
assert sut.month == 1
assert sut.day == 29
assert sut.weekday() == 2



##############
# Canterbury #
##############
'''
Friday 17 November	Friday 16 November	Friday 14 November	Friday 13 November	Friday 12 November
'''
sut = Canterbury.get_holiday(2006)
print sut
assert sut.year == 2006
assert sut.month == 11
assert sut.day == 17
assert sut.weekday() == 4
# But the actual day remains in January
sut = Canterbury.get_actual(2006)
assert sut.year == 2006
assert sut.month == 12
assert sut.day == 16
assert sut.weekday() == 3

###################
# Chatham Islands #
###################


###############
# Hawke's Bay #
###############


###############
# Marlborough #
###############


##########
# Nelson #
##########


#########
# Otago #
#########

# Easter clash

####################
# South Canterbury #
####################


#############
# Southland #
#############


############
# Taranaki #
############


##############
# Wellington #
##############


############
# Westland #
############