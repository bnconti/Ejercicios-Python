#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.4: Plot a function
# Author: Bruno N. Conti

import numpy as np
from matplotlib.pyplot import *


def h(x):
    return (1 / np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2)

if __name__ == "__main__":
    xlist = np.linspace(-4, 4, 41)
    hlist = h(xlist)
    plot(xlist, hlist, '-')
    xlabel('x')
    ylabel('y')
    legend(['1/sqrt(2*pi) * e^(-1/2*x^2)'])
    axis([-4, 4, -0.1, 0.5])
    title('Gaussian')
    show()
