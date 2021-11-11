"""
Write a function that returns the number of calendar days in a given year and month. Hint: see the calendar module in the standard library.
number_of_days(year,month)

Write a function to find the number of leap-years between (including both endpoints) two given years.
number_of_leap_years(year1,year2)

Write a function to find the string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year.
get_day_of_week(year,month,day)
"""
import calendar


def number_of_days(year: int, month: int) -> int:
    """
    Gets the number of days in a given year and month
    :param year:
    :type year:
    :param month:
    :type month:
    :return:
    :rtype:
    """
    assert isinstance(year, int) and 0 <= year
    assert isinstance(month, int) and 0 < month <= 12

    c = calendar.Calendar()
    days = c.itermonthdays(year, month)
    days = set(days)
    days.remove(0)

    return len(days)


def number_of_leap_years(y1: int, y2: int) -> int:
    """
    Gets the number of leaps years (inclusive) in between two years
    :param y1:
    :type y1:
    :param y2:
    :type y2:
    :return:
    :rtype:
    """
    for year in (y1, y2):
        assert isinstance(year, int) and 0 <= year

    return abs(calendar.leapdays(y1, y2+1))


def get_day_of_week(year: int, month: int, day: int) -> str:
    """
    gets the string day of the week for a given year, month and day
    :param year:
    :type year:
    :param month:
    :type month:
    :param day:
    :type day:
    :return:
    :rtype:
    """
    assert isinstance(year, int) and 0 <= year
    assert isinstance(month, int) and 0 < month <= 12
    assert isinstance(day, int) and 0 < day <= number_of_days(year, month)

    day = calendar.weekday(year, month, day)
    return calendar.day_name[day]


if __name__ == '__main__':
    print(number_of_days(1995, 2))
    print(number_of_leap_years(2009, 2000))
    print(get_day_of_week(2021, 10, 21))