#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.13: Raise an exception in case of wrong input
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 13_ball_cml_ValueError.py -1 100
Wrong input! 't' must be between 0 and 2*v0/g
"""

import sys

def input_t():
    t = float(sys.argv[1])
    if 0 <= t <= 2 * v0 / g:
        pass
    else:
        raise ValueError("Wrong input! 't' must be between 0 and 2*v0/g")

v0 = float(sys.argv[2])
g = 9.81

try:
    t = input_t()
except Exception as e:
    print(e)
    sys.exit(1)

y = v0*t - 0.5*g*t**2
print(y)
