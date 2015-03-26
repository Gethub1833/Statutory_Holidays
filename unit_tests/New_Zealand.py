__author__ = 'shane'
import ANZAC, Boxing_day, Christmas, Day_After_New_Years, Easter_Monday, \
    Easter_Sunday, Good_Friday, Labour_day, New_Years_day, Queens_Birthday, \
    Waitangi
from datetime import date

############
# Waitangi #
############
assert Waitangi.get_holiday(2001) == date(2001, 2, 6)
assert Waitangi.get_actual(2001) == date(2001, 2, 6)
assert Waitangi.get_holiday(2015) == date(2015, 2, 6)
assert Waitangi.get_actual(2015) == date(2015, 2, 6)
assert Waitangi.get_holiday(2016) == date(2016, 2, 8)
assert Waitangi.get_actual(2016) == date(2016, 2, 6)
#########
# ANZAC #
#########
assert ANZAC.get_holiday(2001) == date(2001, 4, 25)
assert ANZAC.get_actual(2001) == date(2001, 4, 25)
assert ANZAC.get_holiday(2012) == date(2012, 4, 25)
assert ANZAC.get_actual(2012) == date(2012, 4, 25)
assert ANZAC.get_holiday(2015) == date(2015, 4, 27)
assert ANZAC.get_actual(2015) == date(2015, 4, 25)
############
# Good Friday #
############
############
# Easter Monday #
############
############
# Easter Sunday #
############
############
# Queens Birthday #
############
############
# Labour Day #
############
##############
# Boxing Day #
##############
#################
# Christmas Day #
#################
#######################
# Day After New Years #
#######################
#############
# New Years #
#############