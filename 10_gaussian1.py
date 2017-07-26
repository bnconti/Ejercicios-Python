"""
Exercise 1.10: Evaluate a Gaussian function
The bell-shaped Gaussian function,

f(x) = (1/(sqrt(2pi)s))^(-1/2*((x-m)/s)^2)

is one of the most widely used functions in science
and technology. The parameters m and s > 0 are
prescribed real numbers. Make a program for evaluating
this function when m = 0, s = 2, and x = 1. Verify the
program’s result by comparing with hand calculations
on a calculator.
"""

from math import pi, sqrt, exp

m = 0
s = 2
x = 1

r = float((1/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s))**2)

print("Resultado: {:.4f}".format(r))