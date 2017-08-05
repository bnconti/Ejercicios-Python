#!/usr/bin/env python
# -*- coding: utf-8 -*-

# I can't import files that start with a number so I had to create this one for some exercises.
# Author: Bruno N. Conti

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
            t = float(alpha_i) * T
            value_aprox = sinesum.S(t, n_i)
            exact_value = sinesum.f(t)
            row_list.append(abs(exact_value - value_aprox))
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