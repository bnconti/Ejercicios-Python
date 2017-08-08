#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.9: Plot a formula
# Author: Bruno N. Conti

import numpy as np
from matplotlib import pyplot as plt

v0 = 10; g = 9.81


def y(t):
    global v0, g
    return v0*t - 0.5*g*t**2

if __name__ == '__main__':
    t = np.linspace(0, 2*v0/g, 500)
    m = y(t)
    plt.plot(t, m, '-', label="v0*t - 0.5*g*t^2")
    plt.legend()

    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.title('Trajectory of a ball')
    plt.show()
