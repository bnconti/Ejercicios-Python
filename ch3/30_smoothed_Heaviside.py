# Exercise 3.30: Implement a smoothed Heaviside function
# File name: 30_smoothed_Heaviside
# Author: Bruno N. Conti
# Date: 7/26/17

from math import pi, sin


def H_eps(x, eps=0.01):
    if x < -eps:
        return 0
    elif -eps <= x <= eps:
        return 0.5 + x/2*eps + 0.5*pi*sin(pi*x/eps)
    elif x > eps:
        return 1


def test_H_eps():
    eps = 0.01
    assert H_eps(-1) == 0
    assert H_eps(-0.01) == 0.5 + -0.01/2*eps + 0.5*pi*sin(pi*-0.01/eps)
    assert H_eps(0) == 0.5 + 0/2*eps + 0.5*pi*sin(pi*0/eps)
    assert H_eps(0.01) == 0.5 + 0.01/2*eps + 0.5*pi*sin(pi*0.01/eps)
    assert H_eps(1) == 1

test_H_eps()