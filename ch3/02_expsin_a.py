# Exercise 3.2: Implement a simple mathematical function with a parameter

"""
SAMPLE RUN:
0.0
5.559887866514176e-21
"""

from math import sin, pi, e

a = 10


def h(t):
    r = (e**(-a*t))*sin(pi*t)
    return r

print(h(0))
print(h(1))