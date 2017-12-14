# Problem description: Given my birthday and the current date, calculate my age in days.
# Rules: Compensate for leap days.

# Inputs: birthday (by, bm, bd), current date (cy, cm, cd)
# Outputs: age in days (integer)


def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 2:
        return months[month]
    else:
        if isLeapYear(year):
            return 29
        else:
            return months[month]

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 ==  month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    year = year1
    month = month1
    day = day1
    while dateIsBefore(year, month, day, year2, month2, day2):
        days += 1
        year, month, day = nextDay(year, month, day)
    return days

def test():
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2013, 12, 31) == (2014, 1, 1)
    assert nextDay(2012, 2, 28) == (2012, 2, 29)
    assert nextDay(2012, 2, 29) == (2012, 3, 1)
    print daysBetweenDates(2012, 1, 1, 2013, 1, 1)
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
    print "Tests finished."
    
test()