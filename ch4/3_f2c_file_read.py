#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.3: Read a number from a file
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Convert from Fahrenheit to Celsius.
67.2 °F => 19.6 °C
"""

def extract_data(data):
    infile = open(data, 'r')
    values = []
    for line in infile:
        words = line.split()
        for word in words:
            try:
                values.append(float(word))
            except ValueError:
                pass
    infile.close()
    return values

print("Convert from Fahrenheit to Celsius.")
F = extract_data('3_data.txt')
for value in F:
    print("{:.1f} °F => {:.1f} °C".format(value, (F[0] - 32) / 1.8))

