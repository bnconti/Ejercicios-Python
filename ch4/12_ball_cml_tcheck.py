#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.12: Test validity of input data
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 12_ball_cml_tcheck.py -1 100
Wrong input! 't' must be between 0 and 2*v0/g
"""

import sys

v0 = float(sys.argv[2])
g = 9.81
t = float(sys.argv[1])
if not(0 <= t <= 2*v0/g):
    print("Wrong input! 't' must be between 0 and 2*v0/g")
    sys.exit(1)

y = v0*t - 0.5*g*t**2
print(y)
