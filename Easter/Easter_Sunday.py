'''
This is a holiday, but its main purpose in life is providing us with a pathway
for finding Good Friday and Easter Monday (which is really Mondayised Easter Sunday
 but good luck telling the masses that)
'''

import datetime

def get_actual(year):
    a = year % 19
    b = year / 100
    c = year % 100
    d = b / 4
    e = b % 4
    f = (b + 8) / 25
    g = (b - f + 1) / 3
    h = (19 * a + b - d - g + 15) % 30
    i = c / 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) / 451
    n = (h + l - 7 * m + 114) / 31
    p = (h + l - 7 * m + 114) % 31
    return datetime.date(year, n, p+1)

def get_holiday(year):
    return get_actual(year)