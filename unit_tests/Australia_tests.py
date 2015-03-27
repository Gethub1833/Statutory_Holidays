__author__ = 'shane'
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
'''
State and Territory Public Holidays 2015

Aside from the national public holidays each state and territory of Australia also declares its individual public holidays.

Australian Capital Territory Public Holidays 2015

Monday 9 March: Canberra Day
Monday 8 June: Queen's Birthday
Monday 28 September: Family & Community Day
Monday 5 October: Labour Day

New South Wales Public Holidays 2015
Monday 8 June: Queen's Birthday
Monday 3 August: Bank Holiday
Monday 5 October: Labour Day

Northern Territory Public Holidays 2015

Monday 4 May: May Day
Monday 8 June: Queen's Birthday
Monday 3 August: Picnic Day

The Northern Territory also has a number of ‘show days’ which are observed as public holidays in local regional areas.

Friday 26 June: Borroloola Show Day
Friday 3 July: Alice Springs Show Day
Friday 10 July: Tennant Creek Show Day
Friday 17 July: Katherine Show Day
Friday 24 July: Darwin Show Day

Queensland Public Holidays 2015

Monday 8 June: Queen's Birthday
Wednesday 12 August: Royal Queensland Show (Brisbane only)
Monday 5 October: Labour Day
South Australia Public Holidays 2015

Monday 9 March: March Public Holiday
Monday 8 June: Queen's Birthday
Monday 5 October: Labour Day
Thursday 24 December**: Christmas_and_New_Year Eve**
Thursday 31 December***: New Year's Eve***

**Part-day public holiday from 7 pm to 12 midnight.
***Part-day public holiday from 7 pm to 12 midnight.

Tasmania Public Holidays 2015

Monday 9 March: Eight Hours Day
Tuesday 7 April*: Easter Tuesday
Monday 8 June: Queen's Birthday

*Restricted public holiday in Tasmania. Observed by some awards/agreements and the State Public Service.

Tasmania also has a number of public holidays and ‘show days’ which are observed in local regional areas.

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

Victoria Public Holidays 2015

Monday 9 March: Labour Day
Monday 8 June: Queen's Birthday
Tuesday 3 November: Melbourne Cup Day

Western Australia Public Holidays 2015

Monday 2 March: Labour Day
Monday 1 June: Western Australia Day
Monday 28 September*: Queen's Birthday

* Regional areas in Western Australia may celebrate the Queen's Birthday Public Holiday on an alternative date.
'''