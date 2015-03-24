__author__ = 'shane'
from datetime import date, timedelta

'''
Auckland Anniversary Day is a public holiday observed in the northern half of
the North Island of New Zealand, being the area's provincial anniversary day.

It is observed throughout the historic Auckland Province, even though the
provinces of New Zealand were abolished in 1876. The modern area of observation
includes all of Auckland, the Northland (where it is known instead as Northland
Day), Waikato, Bay of Plenty and Gisborne Regions, as well as some parts of the
Manawatu-Wanganui and Hawke's Bay regions north of the 39th parallel.

The holiday usually falls on the Monday closest to 29 January, the anniversary
of the arrival of William Hobson, later the first Governor of New Zealand, in
the Bay of Islands in 1840.[1]

Auckland Anniversary Day was established by Governor Hobson's direction, over
Willoughby Shortland's signature, in 1842. The New Zealand Government Gazette
of 26 January 1842 (Volume 2, 4th Edition) carried a notice stating,

Saturday, the 29th instant, being the SECOND ANNIVERSARY of the establishment
of the Colony, His Excellency the Governor has been pleased to direct that day
to be held a GENERAL HOLIDAY, on which occasion the Public Offices will be
closed.
'''


def get_holiday(year):
    weekday = get_actual(year).weekday()
    if weekday == 0:
        # Sunday
        return get_actual(year) + timedelta(days=1)
    elif weekday in (1,2,3,4):
        # Monday, Tuesday, Wednesday, Thursday
        return get_actual(year) - timedelta(days=weekday-1)
    else:
        # Friday, Saturday
        return get_actual(year) + timedelta(days=8-weekday)

def get_actual(year):
    JANUARY=1
    return date(year,JANUARY,29)


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