# Exercise 3.1: Implement a simple mathematical function

"""
SAMPLE RUN:
0.0
4.505223801027239e-17
"""

from math import pi, exp, sin


def g(t):
    r = exp(-t)*sin(pi*t)
    return r

print(g(0))
print(g(1))