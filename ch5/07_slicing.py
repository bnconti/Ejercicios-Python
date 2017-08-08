#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.7: Demonstrate array slicing
# Author: Bruno N. Conti

import numpy as np

if __name__ == '__main__':
    w = np.arange(0, 3.1, 0.1)
    print(w[:])  # Prints all the array, the ':' by itself has no effect.
    print(w[:-2])  # Prints the array, excluding the last two elements.
    print(w[::5])  # Prints the array, but jumping 5 indices each time.
    print(w[2:-2:6])  # Prints from the third element, excluding the last two and jumping 6 indices.
