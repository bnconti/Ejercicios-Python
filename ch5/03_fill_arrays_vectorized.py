#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.3: Fill arrays; vectorized version
# Author: Bruno N. Conti

import numpy as np


def h(x):
    return (1 / np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2)

if __name__ == "__main__":
    xlist = np.linspace(-4, 4, 41)
    hlist = h(xlist)
