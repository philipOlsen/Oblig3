import oblig2

def test_checks_if_var_intYear_is_leap_year_if_divisible_by_four_but_not_hundred_or_if_divisible_by_fourhundred():
    assert (isLeapYear(intYear))


def test_checks_if_var_intYear_is_not_leap_year_by_returning_false_using_isLeapYear_function():
    assert not (isLeapYear(intYear))
