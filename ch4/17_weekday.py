#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.17: Look up calendar functionality
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 17_weekday.py 2017 7 31
The day that corresponds to that date is: Monday
"""

import calendar, sys


def input_year():
    try:
        return int(sys.argv[1])
    except IndexError:
        print("Missing 'year' input.")
        sys.exit(1)
    except ValueError:
        print("Wrong 'year' input.")
        sys.exit(1)
    except:
        print("Unexpected error.")
        sys.exit(1)


def input_month():
    try:
        return int(sys.argv[2])
    except IndexError:
        print("Missing 'month' input.")
        sys.exit(1)
    except ValueError:
        print("Wrong 'month' input.")
        sys.exit(1)
    except:
        print("Unexpected error.")
        sys.exit(1)


def input_day():
    try:
        return int(sys.argv[3])
    except IndexError:
        print("Missing 'day' input.")
        sys.exit(1)
    except ValueError:
        print("Wrong 'day' input.")
        sys.exit(1)
    except:
        print("Unexpected error.")
        sys.exit(1)

if __name__ == '__main__':
    year = input_year()
    month = input_month()
    day = input_day()

    week = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    day_number = calendar.weekday(year, month, day)
    print("The day that corresponds to that date is: {}".format(week[day_number]))
