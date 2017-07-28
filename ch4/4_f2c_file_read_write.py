#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.4: Read and write several numbers from and to file
# Author: Bruno N. Conti

"""
SAMPLE RUN:
4_output.txt
67.2	19.555555555555557
66.0	18.88888888888889
78.9	26.055555555555557
102.1	38.94444444444444
32.0	0.0
87.8	30.999999999999996
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

F_values = extract_data('4_Fdeg.dat')
outfile = open('4_output.txt', 'w')
for F in F_values:
    C = (F - 32) / 1.8
    outfile.write("{:.1f} \t {:.1f} \n".format(F, C))

outfile.close()

