#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.20: Make a complete module
# Author: Bruno N. Conti

import sys


def C2F(C):
    return C*9/5 + 32


def F2C(F):
    return (F - 32)*5/9


def C2K(C):
    return C + 273.15


def K2C(K):
    return K - 273.15


def F2K(F):
    return (F + 459.67)*5/9


def K2F(K):
    return K*9/5 - 459.67

__all__ = ['C2F', 'F2C', 'C2K', 'K2C', 'F2K', 'K2F']
_filename = sys.argv[0]
_usage = """
Module for converting between temperature scales -- Celsius, Kelvin and Fahrenheit.
Input the value to convert and the scale. Usage examples:

python 20_convert_temp.py 100 K
100.0K => -173.1C or -279.7F

python 20_convert_temp.py 20 C
20.0C => 68.0F or 293.1K
"""


def test_conversion():
    F=100; C=18; K=320

    def float_eq(t1, t2, e=1E-4):
        return abs(t1-t2) < e

    success = \
        float_eq(C2F(F2C(F)), F) and \
        float_eq(K2F(F2K(F)), F) and \
        float_eq(F2C(C2F(C)), C) and \
        float_eq(K2C(C2K(C)), C) and \
        float_eq(C2K(K2C(K)), K) and \
        float_eq(F2K(K2F(K)), K)

    msg_error = """Computations failed. Results:
    C2F(F2C(F)) = {}({})
    K2F(F2K(F)) = {}({})
    F2C(C2F(C)) = {}({})
    K2C(C2K(C)) = {}({})
    C2K(K2C(K)) = {}({})
    F2K(K2F(K)) = {}({})
    """.format(K2F(F2K(F)), F, K2F(F2K(F)), F, F2C(C2F(C)), C, K2C(C2K(C))
               , C, C2K(K2C(K)), K, F2K(K2F(K)), K)

    assert success, msg_error
    return


def convert_input(value, scale):
    if scale.capitalize() == 'C':
        print("""{:.1f}C => {:.1f}F or {:.1f}K""".format(value, C2F(value), C2K(value)))
    elif scale.capitalize() == 'F':
        print("""{:.1f}F => {:.1f}C or {:.1f}K""".format(value, F2C(value), F2K(value)))
    elif scale.capitalize() == 'K':
        print("""{:.1f}K => {:.1f}C or {:.1f}F""".format(value, K2C(value), K2F(value)))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(_usage)
        exit(1)

    try:
        if sys.argv[1] == 'verify':
            test_conversion()
            exit(1)
    except:
        pass

    try:
        value = float(sys.argv[1])
        scale = sys.argv[2]
        if scale not in ('C', 'F', 'K'):
            print("Invalid scale! Available options are 'C', 'F' and 'K'.")
            exit(1)
        convert_input(value, scale)
    except ValueError:
        print("Not valid input found!")
    except IndexError:
        print("Missing input!")

