#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.2: Read a number from the command line
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 02_f2c_cml.py 0
Convert from Fahrenheit to Celsius.
-17.8 °C
"""

import sys

print("Convert from Fahrenheit to Celsius.")
F = float(sys.argv[1])
C = (F - 32) / 1.8
print("{:.1f} °C".format(C))
