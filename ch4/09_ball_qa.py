#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.9: Prompt the user for input to a formula
# Author: Bruno N. Conti

"""
SAMPLE RUN:
t = 6
v0 = 100
423.41999999999996
"""

t = float(input("t = "))
v0 = float(input("v0 = "))

g = 9.81
y = v0*t - 0.5*g*t**2
print(y)
