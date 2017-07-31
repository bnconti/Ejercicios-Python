#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.18: Use the StringFunction tool
# Author: Bruno N. Conti

# Using Python 2.7 because compatibility issues with SciTools and my IDE wasn't
# able to find the scitools package, but I was able to run the program from the
# console after creating a virtual enviroment with Anaconda.

"""
SAMPLE RUN:
python 18_integrate2.py "x**2+4" 0 5
Integral of x**2+4 on [0, 5] with n=200: 61.6664
"""

from scitools.StringFunction import StringFunction
from math import *
import sys


def midpoint_integration(f, a, b, n=100):
    h = (b - a)/float(n)
    I = 0
    for i in range(n):
        I += f(a + i*h + 0.5*h)
    return h*I

def test_midpoint_integracion():
    functions = [StringFunction("x**3"), StringFunction("2*x - 7"), StringFunction("3*x**2 - 5*x")]
    exact_values = [2500, 30, 750]
    tol = 1E-2
    a = 0; b = 10; n = 500
    for f, A_exact in zip(functions, exact_values):
        A = midpoint_integration(f, a, b, n)
        assert abs(A - A_exact) < tol, "Computation failed: %f, expected %f" % (A, A_exact)

test_midpoint_integracion()

if __name__ == '__main__' :
    f_formula = StringFunction(sys.argv[1])
    a = eval(sys.argv[2])
    b = eval(sys.argv[3])
    if len(sys.argv) >= 5:
        n = int(sys.argv[4])
    else:
        n = 200
    I = midpoint_integration(f_formula, a, b, n)
    print('Integral of %s on [%g, %g] with n=%d: %g' %
          (f_formula, a, b, n, I))
