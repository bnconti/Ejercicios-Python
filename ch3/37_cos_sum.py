# Exercise 3.37: Make a table for approximations of cos x
# Author: Bruno N. Conti
# Date: 7/27/17
# Run pytest 37_cos_sum.py for testing

"""
SAMPLE RUN:
Difference between cos(x) implemented with sums and cos(x) from the math module.
------------------------------------------------------------------------------------------
               n = 5          n = 25         n = 50         n = 100        n = 200
------------------------------------------------------------------------------------------
x = 12.5664    1.61470e+04    1.44998e-11    2.43783e-12    2.43783e-12    2.43783e-12
------------------------------------------------------------------------------------------
x = 18.8496    1.22239e+06    2.27931e-02    2.34180e-10    2.34180e-10    2.34180e-10
------------------------------------------------------------------------------------------
x = 25.1327    2.40955e+07    6.57914e+04    2.40499e-08    2.40499e-08    2.40499e-08
------------------------------------------------------------------------------------------
x = 31.4159    2.35831e+08    6.52140e+09    1.20338e-04    1.20337e-04    1.20337e-04
------------------------------------------------------------------------------------------
"""

from math import pi, cos


def C(x, n):
    term = 1
    s = term
    for j in range(1, n+1):
        term *= -x**2 / (2*j*(2*j-1))
        s += term
    return s


def table_C():
    print("Difference between cos(x) implemented with sums and cos(x) from the math module.")
    input_values = [4*pi, 6*pi, 8*pi, 10*pi]
    range_values = [5, 25, 50, 100, 200]
    print("{}".format("-" * 90))
    print("               ", end='')
    for n in range_values:
        print("n = {:<11}".format(n), end='')
    print("\n{}".format("-" * 90))
    for x in input_values:
        print("x = {:.4f}".format(x), end='')
        for n in range_values:
            print("{:>15.5e}".format(abs(C(x, n)-cos(x))), end='')
        print("\n{}".format("-"*90))


table_C()
