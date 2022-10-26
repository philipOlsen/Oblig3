import pytest
#Innlevering 2 - Philip Ringen Olsen // Software Engineering og Testing // Rettet

#Function number one with test
#By using an If test with leap year calculations the code checks if the year is a leap year by either returning True or False
intYear = 2000
def isLeapYear(intYear):
    if ((intYear % 4 == 0) and
        (intYear % 100 != 0) or
            (intYear % 400 == 0)):
        return True
    else:
        return False

def test_checks_if_var_intYear_is_leap_year_if_divisible_by_four_but_not_hundred_or_if_divisible_by_fourhundred():
    assert (isLeapYear(intYear))

#Function number two with test
#Imports the calendar module and uses the .isLeap method that comes with it to check whether the result is True or False.
year = 20
def checkYear(year):
    import calendar
    return (calendar.isleap(year))

def test_checkYear_is_a_leap_year():
    if (checkYear(year)):
        assert True
    else:
        assert False









