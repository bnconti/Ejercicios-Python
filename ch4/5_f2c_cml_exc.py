#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.5: Use exceptions to handle wrong input
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 5_f2c_cml_exc.py 0
Convert from Fahrenheit to Celsius.
0.0 °F => -17.8 °C

python 5_f2c_cml_exc.py
Missing argument!
"""

import sys

"""
Extend the program from Exercise 4.2 with a try-except block to handle the
potential error that the Fahrenheit temperature is missing on the command line.
"""

try:
    F = float(sys.argv[1])
    C = (F - 32) / 1.8
    print("Convert from Fahrenheit to Celsius.")
    print("{:.1f} °F => {:.1f} °C".format(F, C))
except IndexError:
    print("Missing argument!")
