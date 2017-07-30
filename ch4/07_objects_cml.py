#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.7: Read input from the command line
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 07_objects_cml.py 11
The input is of type 'int' and its value is '11'

python 07_objects_cml.py 0.1
The input is of type 'float' and its value is '0.1'

python 07_objects_cml.py "[2, 4, 6, 8, 10]"
The input is of type 'list' and its value is '[2, 4, 6, 8, 10]'

python 07_objects_cml.py "(1, 1)"
The input is of type 'tuple' and its value is '(1, 1)'

python 07_objects_cml.py '"this is a string"'
The input is of type 'str' and its value is 'this is a string'
"""

"""
a) Let a program store the result of applying the eval function to the first
command-line argument. Print out the resulting object and its type.
b) Run the program with different input: an integer, a real number, a list, and
a tuple.
c) Try the string "this is a string" as a command-line argument. Why does
this string cause problems and what is the remedy?
"""

# We need to use double quotes when using strings, otherwise
# the console will interpret the input as variables.

import sys

i = eval(sys.argv[1])
print("The input is of type '{}' and its value is '{}'".format(type(i).__name__, i))
