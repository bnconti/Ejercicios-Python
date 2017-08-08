#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.2: Fill arrays; loop version
# Author: Bruno N. Conti

import numpy as np
import math


def h(x):
    return (1 / math.sqrt(2*math.pi)) * math.exp(-0.5 * x**2)

if __name__ == "__main__":
    n = 41; a = -4; b = 4
    dx = (b-a) / (n-1)
    xlist, hlist = np.zeros(n), np.zeros(n)
    for i in range(n):
        xlist[i] = -4 + i*dx
        hlist[i] = h(xlist[i])
