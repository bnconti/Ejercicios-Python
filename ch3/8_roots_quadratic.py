# Exercise 3.8: Write a function for solving ax**2 + bx + c = 0
from numpy.lib.scimath import *


def roots(a, b, c):
    solutions = (((-b) + sqrt(b**2 - 4*a*c))/2*a,
    ((-b) - sqrt(b**2 - 4*a*c))/2*a)
    return solutions


def test_quadratic():
    c1 = roots(1, 2, 2)
    c2 = roots(1, 4, 3)
    assert c1 == ((-1+1j),(-1-1j))
    assert c2 == (-1.0, -3.0)