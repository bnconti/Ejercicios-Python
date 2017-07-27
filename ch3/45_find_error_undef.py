# Exercise 3.45: Find an error in a program
# Author: Bruno N. Conti


"""
def f(x, m, n, r, s):
    return expsin(x, r, m) + expsin(x, s, n)

x = 2.5
print(f(x, 0.1, 0.2, 1, 1))

from math import exp, sin

def expsin(x, p, q):
    return exp(p*x)*sin(q*x)

# >>> NameError: global name ’expsin’ is not defined
"""

# The problem is that the function 'expsin' needs to be positioned before any code
# that will uses it, in this case the call to the function f. This alto applies to the
# imports from math.

from math import exp, sin


def expsin(x, p, q):
    return exp(p*x)*sin(q*x)


def f(x, m, n, r, s):
    return expsin(x, r, m) + expsin(x, s, n)

x = 2.5
print(f(x, 0.1, 0.2, 1, 1))
