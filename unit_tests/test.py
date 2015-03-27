from Easter import Easter_Sunday
# Christmas_and_New_Year tests

# get actual should produce a datetime object for
#
# year = random.randint(1, 5000)
# print "Christmas_and_New_Year tests done using:", year,"year"
# print "Get Actual"
# sut = Christmas_and_New_Year.get_actual(year)
# print sut.year == year
# print sut.month == 12
# print sut.day == 25
# print "Get Observed"
# sut = Christmas_and_New_Year.get_holiday(year)
# print sut.year == year
# print sut.month == 12
# print sut.day == 25
#
#
# year = random.randint(1, 5000)
# print "Boxing day tests done using:", year,"year"
# sut = Boxing_day.get_actual(year)
# print sut.year == year
# print sut.month == 12
# print sut.day == 26
# print "Get Observed"
# sut = Boxing_day.get_holiday(year)
# print sut.year == year
# print sut.month == 12
# print sut.day == 26
#
# # year = random.randint(-1000, 0)
# # print "Tests done using:", year,"year"
# # sut = Christmas_and_New_Year.get_actual(year)
# # print sut.year == year
# # print sut.month == 12
# # print sut.day == 25
#
# # ANZAC day falls on the weekend in 2015, this will be the first Mondayised  ANZAC day
#
# # Queens Birthday
# print "Queen's Birthday"
# for year in range(2000,2020):
#     print "Get Actual", year
#     sut = Queens_Birthday.get_actual(year)
#     print sut.year == year
#     print sut.month == 6
#     print sut.day
#     print "Get Observed"
#     sut = Queens_Birthday.get_holiday(year)
#     print sut.year == year
#     print sut.month == 6
#     print sut.day
#
# # Labour day
# print "Labour day"
# for year in range(2000,2020):
#     print "Get Actual", year
#     sut = Labour_day.get_actual(year)
#     print sut.year == year
#     print sut.month == 10
#     print sut.day
#     print "Get Observed"
#     sut = Labour_day.get_holiday(year)
#     print sut.year == year
#     print sut.month == 10
#     print sut.day


# Easter Sunday
print "Easter Sunday"
for year in range(2000,2020):
    print "Get Actual", year
    sut = Easter_Sunday.get_actual(year)
    print sut.year == year
    print sut.month
    print sut.day
    print "Get Observed"
    sut = Easter_Sunday.get_holiday(year)
    print sut.year == year
    print sut.month
    print sut.day

'''
Test Data, from Wikipedia
Year	Western	Eastern
1995	April 16	April 23
1996	April 7	April 14
1997	March 30	April 27
1998	April 12	April 19
1999	April 4	April 11
2000	April 23	April 30
2001	April 15
2002	March 31	May 5
2003	April 20	April 27
2004	April 11
2005	March 27	May 1
2006	April 16	April 23
2007	April 8
2008	March 23	April 27
2009	April 12	April 19
2010	April 4
2011	April 24
2012	April 8	April 15
2013	March 31	May 5
2014	April 20
2015	April 5	April 12
2016	March 27	May 1
2017	April 16
2018	April 1	April 8
2019	April 21	April 28
2020	April 12	April 19
2021	April 4	May 2
2022	April 17	April 24
2023	April 9	April 16
2024	March 31	May 5
2025	April 20
2026	April 5	April 12
2027	March 28	May 2
2028	April 16
2029	April 1	April 8
2030	April 21	April 28
2031	April 13
2032	March 28	May 2
2033	April 17	April 24
2034	April 9
2035	March 25	April 29
'''