# Exercise 3.1: Implement a simple mathematical function

from math import pi, exp, sin

def g(t):
    r = exp(-t)*sin(pi*t)
    return r

print(g(0))
print(g(1))