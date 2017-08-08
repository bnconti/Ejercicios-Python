#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.1: Fill lists with function values
# Author: Bruno N. Conti

from math import pi, sqrt, exp


def h(x):
    return (1 / sqrt(2*pi)) *  exp(-0.5 * x**2)

if __name__ == "__main__":
    n = 41; a = -4; b = 4  # 40 uniformly spaced x values between -4 and 4.
    dx = (b-a) / (n-1)  # Increment
    xlist = [-4 + i*dx for i in range(n)]
    hlist = [h(x) for x in xlist]
