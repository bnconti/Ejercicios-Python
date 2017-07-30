#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.11: Use exceptions to handle wrong input
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 11_ball_cml_qa.py
Missing 't' argument! Input t = 1
Missing 'v0' argument! Input v0 = 120
115.095
"""

import sys

def input_t():
    try:
        t = float(sys.argv[1])
    except IndexError:
        print("Missing 't' argument!", end='')
        t = float(input(" Input t = "))
    return t

def input_v0():
    try:
        v0 = float(sys.argv[2])
    except IndexError:
        print("Missing 'v0' argument!", end='')
        v0 = float(input(" Input v0 = "))
    return v0

t = input_t(); v0 = input_v0(); g = 9.81
y = v0*t - 0.5*g*t**2
print(y)
