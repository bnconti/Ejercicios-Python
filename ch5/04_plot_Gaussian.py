#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.4: Plot a function
# Author: Bruno N. Conti

import numpy as np
from matplotlib import pyplot as plt


def h(x):
    return (1 / np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2)

if __name__ == "__main__":
    xlist = np.linspace(-4, 4, 200)
    hlist = h(xlist)
    plt.plot(xlist, hlist, '-', label='1/sqrt(2*pi) * e^(-1/2*x^2)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gaussian')
    plt.legend()
    plt.show()
