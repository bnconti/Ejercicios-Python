#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Apply a function to a vector
# Author: Bruno N. Conti

"""
[ 23.7781122   88.25661077  -0.36787944]
"""

import numpy as np


def f(x):
    return np.power(x, 3) + x*np.exp(x) + 1

if __name__ == '__main__':
    v = (2, 3, -1)
    print(f(v))
