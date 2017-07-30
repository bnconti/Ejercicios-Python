#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.10: Read parameters in a formula from the command line
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 10_ball_cml.py 10 1000
9509.5
"""

import sys

t = float(sys.argv[1])
v0 = float(sys.argv[2])

g = 9.81
y = v0*t - 0.5*g*t**2
print(y)
