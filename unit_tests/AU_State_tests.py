__author__ = 'shane'
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Australia.States.ACT import Canberra, Community
from Australia.States import Queens_birthday, Labour
from Australia.States.NT import May_Day, Picnic_Day
from Australia.States.NSW import Bank_Holiday
from Australia.States.SA import March_public_holiday
from Australia.States.Victoria import Queens_Birthday as Victoria.Queens_birthday
from datetime import date


#######
# ACT #
#######
'''
Australian Capital Territory Public Holidays 2015

Monday 9 March: Canberra Day
Monday 8 June: Queen's Birthday
Monday 28 September: Family & Community Day
Monday 5 October: Labour Day

New South Wales Public Holidays 2015
Monday 8 June: Queen's Birthday
Monday 3 August: Bank Holiday
Monday 5 October: Labour Day
'''
# Canberra Day
assert Canberra.get_actual(2005) == date(2005, 3, 12)
assert Canberra.get_holiday(2005) == date(2005, 3, 21)
# Post 2007
assert Canberra.get_actual(2015) == date(2015, 3, 12)
assert Canberra.get_holiday(2015) == date(2015, 3, 9)

# Queen's Birthday
assert Queens_birthday.get_actual(2015) == date(2015, 6, 8)
assert Queens_birthday.get_holiday(2015) == date(2015, 6, 8)

# Family and Community Day (Should generate a warning)
assert Community.get_actual(2015) == date(2015, 9, 28)
assert Community.get_holiday(2015) == date(2015, 9, 28)

# Labour Day
assert Labour.get_actual(2015) == date(2015, 10, 5)
assert Labour.get_holiday(2015) == date(2015, 10, 5)

######################
# Northern Territory #
######################
'''
Northern Territory Public Holidays 2015

Monday 4 May: May Day
Monday 8 June: Queen's Birthday
Monday 3 August: Picnic Day

The Northern Territory also has a number of show days' which are observed as public holidays in local regional areas.

Friday 26 June: Borroloola Show Day
Friday 3 July: Alice Springs Show Day
Friday 10 July: Tennant Creek Show Day
Friday 17 July: Katherine Show Day
Friday 24 July: Darwin Show Day
'''
# May Day
assert May_Day.get_actual(2015) == date(2015, 5, 4)
assert May_Day.get_holiday(2015) == date(2015, 5, 4)

# Picnic Day
assert Picnic_Day.get_actual(2015) == date(2015, 8, 3)
assert Picnic_Day.get_holiday(2015) == date(2015, 8, 3)

# Queens Birthday
assert Queens_birthday.get_actual(2015) == date(2015, 6, 8)
assert Queens_birthday.get_holiday(2015) == date(2015, 6, 8)

##############
# Queensland #
##############
'''
Queensland Public Holidays 2015

Monday 8 June: Queen's Birthday
Wednesday 12 August: Royal Queensland Show (Brisbane only)
Monday 5 October: Labour Day
South Australia Public Holidays 2015
'''
# Queens Birthday
assert Queens_birthday.get_actual(2015) == date(2015, 6, 8)
assert Queens_birthday.get_holiday(2015) == date(2015, 6, 8)

# Royal Queensland Show (Brisbane only)

# Labour Day
assert Labour.get_actual(2015) == date(2015, 10, 5)
assert Labour.get_holiday(2015) == date(2015, 10, 5)

###################
# South Australia #
###################
'''
Monday 9 March: March Public Holiday
Monday 8 June: Queen's Birthday
Monday 5 October: Labour Day
Thursday 24 December**: Christmas Eve**
Thursday 31 December***: New Year's Eve***

**Part-day public holiday from 7 pm to 12 midnight.
***Part-day public holiday from 7 pm to 12 midnight.
'''
# March Public Holiday
assert March_public_holiday.get_actual(2015) == date(2015, 3, 9)
assert March_public_holiday.get_holiday(2015) == date(2015, 3, 9)

# Queens Birthday
assert Queens_birthday.get_actual(2015) == date(2015, 6, 8)
assert Queens_birthday.get_holiday(2015) == date(2015, 6, 8)

# Labour Day
assert Labour.get_actual(2015) == date(2015, 10, 5)
assert Labour.get_holiday(2015) == date(2015, 10, 5)

############
# Tasmania #
############
'''
Tasmania Public Holidays 2015

Monday 9 March: Eight Hours Day
Tuesday 7 April*: Easter Tuesday
Monday 8 June: Queen's Birthday

*Restricted public holiday in Tasmania. Observed by some awards/agreements and the State Public Service.

Tasmania also has a number of public holidays and show days which are observed in local regional areas.

Wednesday 7 January: Devonport Cup
Monday 9 February: Royal Hobart Regatta
Wednesday 25 February: Launceston Cup
Tuesday 3 March: King Island Show
Friday 8 May: AGFEST Circular Head
Friday 2 October: Burnie Show
Thursday 8 October: Royal Launceston Show
Friday 16 October: Flinders Island Show
Thursday 22 October: Royal Hobart Show
Monday 2 November: Recreation Day Launceston (all parts of the state which do not observe Royal Hobart Regatta)
Friday 27 November: Devonport Show
'''
# Eight Hours Day

# Easter Tuesday

# Queens Birthday
assert Queens_birthday.get_actual(2015) == date(2015, 6, 8)
assert Queens_birthday.get_holiday(2015) == date(2015, 6, 8)

############
# Victoria #
############
'''
Victoria Public Holidays 2015

Monday 9 March: Labour Day
Monday 8 June: Queen's Birthday
Tuesday 3 November: Melbourne Cup Day
'''
# Labour Day

# Queens Birthday
assert Victoria.Queens_birthday.get_actual(2015) == date(2015, 6, 8)
assert Queens_birthday.get_holiday(2015) == date(2015, 6, 8)

# Melbourne Cup Day


#####################
# Western Australia #
#####################
'''
Western Australia Public Holidays 2015

Monday 2 March: Labour Day
Monday 1 June: Western Australia Day
Monday 28 September*: Queen's Birthday

* Regional areas in Western Australia may celebrate the Queen's Birthday Public Holiday on an alternative date.
'''
# Labour Day

# Western Australia Day

# Queens Birthday
