# Exercise 3.29: Implement the Heaviside function
# File name: 29_Heaviside
# Author: Bruno N. Conti
# Date: 7/26/17


def H(x):
    return 1 if x >= 0 else 0


def test_H():
    assert H(-10) == 0
    assert H(-10**-15) == 0
    assert H(0) == 1
    assert H(10**-15) == 1
    assert H(10) == 1

test_H()
