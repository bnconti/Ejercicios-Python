#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.6: Simulate by hand a vectorized expression
# Author: Bruno N. Conti

import numpy as np


def f(x, t):
    return np.cos(np.sin(x)) + np.exp(1/t)

if __name__ == '__main__':
    x = np.array([0, 2])
    t = np.array([1, 1.5])
    print(f(x, t))
