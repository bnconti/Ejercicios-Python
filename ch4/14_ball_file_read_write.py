#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.14: Evaluate a formula for data in a file
# Author: Bruno N. Conti

"""
SAMPLE RUN:
        t       f(t)
---------  ---------
0.042      0.117348
0.0519085  0.142509
0.102623   0.256211
0.1117     0.273901
0.15592    0.348514
0.173839   0.373288
0.209429   0.413152
0.213426   0.416852
0.213859   0.417243
0.27       0.452425
0.28075    0.455635
0.29584    0.458228
0.346481   0.450602
0.35       0.449137
0.368079   0.439697
0.372985   0.436582
0.393252   0.421211
0.5062     0.26175
0.528      0.216564
0.53012    0.211922
0.576815   0.0984752
0.57983    0.090416
"""

import sys
from tabulate import tabulate

def extract_data(data):
    infile = open(data, 'r')
    t_data = []; v0 = None
    line = infile.readline()
    words = line.split()
    for word in words:
        try:
            v0 = float(word)
        except ValueError:
            pass
    line = infile.readline()
    for line in infile:
        words = line.split()
        for word in words:
            try:
                t_data.append(float(word))
            except ValueError:
                pass
    infile.close()
    if len(t_data) == 0 or v0 is None:
        raise ValueError("Not valid input found")
    return v0, t_data

def test_data():
    try:
        v0, t_data = extract_data('14_ball.dat')
        return v0, t_data
    except Exception as e:
        print(e)
        sys.exit(1)

v0, t_data = test_data()

result_table = []
g = 9.81
for t in t_data:
    result_table.append((t, v0*t - 0.5*g*t**2))

result_table.sort(key = lambda tup: tup[0])

outfile = open("14_ball_output.txt", "w")
outfile.write(tabulate(result_table, headers=['t', 'f(t)'], tablefmt="simple"))
outfile.close()
