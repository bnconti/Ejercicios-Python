#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.21: Organize a previous program as a module
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 21_sinesum2.py "[1, 3, 5, 10, 50, 1000, 10000]" "[0.0001, 0.005, 0.01, 0.25, 0.5]" "6.82"
ERROR     0.0001     0.005      0.01       0.25       0.5

    1    1.0e+00    9.6e-01    9.1e-01   -2.6e-01   -6.6e-01

    3    1.0e+00    8.7e-01    7.4e-01   -1.1e+00   -1.9e-02

    5    1.0e+00    7.8e-01    5.7e-01   -1.2e+00    4.0e-01

   10    9.9e-01    5.7e-01    1.9e-01   -1.2e+00    3.5e-01

   50    9.6e-01   -2.2e-01    2.8e-03   -1.3e+00    3.3e-01

 1000    2.2e-01   -3.8e-02   -8.9e-02   -1.3e+00    3.4e-01

10000    2.4e-02   -4.4e-02   -8.6e-02   -1.3e+00    3.4e-01

"""

import sys
from importlib import import_module
sinesum = import_module('_sinesum')


def table(n_values, alpha_values, T):
    def print_table(n_values, alpha_values, approximations):
        print("{:<10}".format('ERROR'), end='')
        for value in alpha_values:
            print("{:<11}".format(value), end='')
        print("\n")
        for n_i, row in zip(n_values, approximations):
            print("{:>5}".format(n_i), end='')
            for elem in row:
                print("{:>11.1e}".format(elem), end='')
            print("\n")

    approximations = []
    for n_i in n_values:
        row_list = []
        for alpha_i in alpha_values:
            t = alpha_i * T
            row_list.append(sinesum.f(t) - sinesum.S(t, n_i))
        approximations.append(row_list)

    print_table(n_values, alpha_values, approximations)


def test_table():
    try:
        table(eval(sys.argv[1]), eval(sys.argv[2]), float(sys.argv[3]))
    except IndexError:
        print("Missing input!")
    except ValueError:
        print("Invalid input!")

_usage = """
Generates a table with the margin of error from the approximation to the Fourier Series
given certain input values. 'n' is the quantity of sums, 'alpha' the interval and T the period.
Input the first two as lists between quotes or the program will not work. 
"""

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(_usage)
        sys.exit(1)
    test_table()