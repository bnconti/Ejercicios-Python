#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.1: Make an interactive program
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Convert from Fahrenheit to Celsius.
Input F = 0
-17.8 °C
"""

"""
Make a program that asks the user for a temperature in Fahrenheit
degrees and reads the number; 
computes the corresponding temperature in Celsius degrees; 
and prints out the temperature in the Celsius scale.
"""

print("Convert from Fahrenheit to Celsius.")
F = float(input("Input F = "))
C = (F - 32) / 1.8
print("{:.1f} °C".format(C))
