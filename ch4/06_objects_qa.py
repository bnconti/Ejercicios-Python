#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.6: Read input from the keyboard
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Input something! 8
The input is of type 'int' and its value is '8'

Input something! 7.4
The input is of type 'float' and its value is '7.4'

Input something! 0+3j
The input is of type 'complex' and its value is '3j'

Input something! [-5, 0, 1, 10]
The input is of type 'list' and its value is '[-5, 0, 1, 10]'

Input something! (1, 3)
The input is of type 'tuple' and its value is '(1, 3)'
"""

"""
Make a program that asks for input from the user, applies eval to this input, and
prints out the type of the resulting object and its value. Test the program by pro-
viding five types of input: an integer, a real number, a complex number, a list, and
a tuple.
"""

i = eval(input("Input something! "))
print("The input is of type '{}' and its value is '{}'".format(type(i).__name__, i))
