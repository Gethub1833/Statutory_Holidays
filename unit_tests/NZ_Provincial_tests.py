__author__ = 'shane'
from New_Zealand.Provincial import Auckland, Canterbury, Chathams, Hawkes_Bay, \
     Marlborough, Nelson, Otago, South_Canterbury, Southland, Taranaki, Wellington, Westland
from datetime import date


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
assert Auckland.get_holiday(2016) == date(2016, 2, 1)

# But the actual day remains in January
assert Auckland.get_actual(2016) == date(2016, 1, 29)

# In 2014 the holiday fell in January
assert Auckland.get_holiday(2014) == date(2014, 1, 27)

# But the actual day remains in January
assert Auckland.get_actual(2014) == date(2014, 1, 29)

##############
# Canterbury #
##############
'''
Friday 17 November	Friday 16 November	Friday 14 November	Friday 13 November	Friday 12 November
'''
# 2006 was the 17th of November
assert Canterbury.get_holiday(2006) == date(2006, 11, 17)

# But the actual day remains in December
assert Canterbury.get_actual(2006) == date(2006, 12, 16)

assert Canterbury.get_holiday(2007) == date(2007, 11, 16)

# But the actual day remains in December
assert Canterbury.get_actual(2006) == date(2006, 12, 16)

###################
# Chatham Islands #
###################
'''Chatham Islands	30 November	Monday 28 November	Monday 3 December	Monday 2 December	Monday 1 December'''
assert Chathams.get_holiday(2011) == date(2011, 11, 28)

# But the actual day remains unchanged
assert Chathams.get_actual(2011) == date(2011, 11, 30)

assert Chathams.get_holiday(2014) == date(2014, 12, 1)

# But the actual day remains in November
assert Chathams.get_actual(2014) == date(2014, 11, 30)

###############
# Hawke's Bay #
###############
'''Hawke's Bay	1 November	Friday 21 October	Friday 19 October	Friday 25 October	Friday 24 October'''
assert Hawkes_Bay.get_holiday(2011) == date(2011, 10, 21)

# But the actual day remains in January
assert Hawkes_Bay.get_actual(2011) == date(2011, 11, 1)

assert Hawkes_Bay.get_holiday(2014) == date(2014, 10, 24)

# But the actual day remains in November
assert Hawkes_Bay.get_actual(2011) == date(2011, 11, 1)

###############
# Marlborough #
###############
'''Marlborough	1 November	Monday 31 October	Monday 29 October	Monday 4 November	Monday 3 November'''
assert Marlborough.get_holiday(2011) == date(2011, 10, 31)

# But the actual day remains in January
assert Marlborough.get_actual(2011) == date(2011, 11, 1)

assert Marlborough.get_holiday(2014) == date(2014, 11, 3)

# But the actual day remains in January
assert Marlborough.get_actual(2014) == date(2014, 11, 1)

##########
# Nelson #
##########
'''Nelson	1 February	Monday 31 January	Monday 30 January	Monday 4 February	Monday 3 February'''
assert Nelson.get_holiday(2011) == date(2011, 1, 31)

# But the actual day remains in January
assert Nelson.get_actual(2011) == date(2011, 2, 1)

assert Nelson.get_holiday(2014) == date(2014, 2, 3)

assert Nelson.get_actual(2014) == date(2014, 2, 1)

#########
# Otago #
#########
'''Otago	23 March	Monday 21 March	Monday 26 March	Monday 25 March	Monday 24 March'''
assert Otago.get_holiday(2011) == date(2011, 3, 21)
# But the actual day remains in January
assert Otago.get_actual(2011) == date(2011, 3, 23)

# Easter clash
assert Otago.get_holiday(2008) == date(2008, 3, 25)
# But the actual day remains in January
assert Otago.get_actual(2008) == date(2008, 3, 23)


####################
# South Canterbury #
####################
'''Canterbury (South)	16 December	Monday 26 September	Monday 24 September	Monday 23 September	Monday 22 September'''
assert South_Canterbury.get_holiday(2011) == date(2011, 9, 26)

assert South_Canterbury.get_actual(2011) == date(2011, 12, 16)

assert South_Canterbury.get_holiday(2014) == date(2014, 9, 22)

assert South_Canterbury.get_actual(2014) == date(2014, 12, 16)


#############
# Southland #
#############
'''Southland	17 January	Monday 17 January	Tuesday 10 April	Tuesday 2 April	Tuesday 22 April'''
assert Southland.get_holiday(2011) == date(2011, 1, 17)

assert Southland.get_actual(2011) == date(2011, 1, 17)

assert Southland.get_holiday(2012) == date(2012, 4, 10)

assert Southland.get_actual(2012) == date(2012, 1, 17)

############
# Taranaki #
############
'''Taranaki	31 March	Monday 14  March	Monday 12 March	Monday 11 March	Monday 10 March'''
assert Taranaki.get_holiday(2011) == date(2011, 3, 14)

assert Taranaki.get_actual(2011) == date(2011, 3, 31)

assert Taranaki.get_holiday(2014) == date(2014, 3, 10)

assert Taranaki.get_actual(2014) == date(2014, 3, 31)

##############
# Wellington #
##############
'''Wellington	22 January	Monday 24 January	Monday 23 January	Monday 21 January	Monday 20 January'''
assert Wellington.get_holiday(2011) == date(2011, 1, 24)

assert Wellington.get_actual(2011) == date(2011, 1, 22)

assert Wellington.get_holiday(2014) == date(2014, 1, 20)
# But the actual day remains in November
assert Wellington.get_actual(2014) == date(2014, 1, 22)

############
# Westland #
############
'''Westland	1 December	Monday 28 November	Monday 3 December	Monday 2 December	Monday 1 December'''
assert Westland.get_holiday(2011) == date(2011, 11, 28)
# But the actual day remains in January
assert Westland.get_actual(2014) == date(2014, 12, 1)

assert Westland.get_holiday(2014) == date(2014, 12, 1)
# But the actual day remains in November
assert Westland.get_actual(2014) == date(2014, 12, 1)