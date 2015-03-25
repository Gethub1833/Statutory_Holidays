__author__ = 'shane'
from datetime import date
import stat_helper

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
    return stat_helper.get_nearest_monday(get_actual(year))


def get_actual(year):
    JANUARY = 1
    return date(year, JANUARY, 29)