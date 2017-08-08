#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.11: Specify the extent of the axes in a plot
# Author: Bruno N. Conti

import numpy as np
from matplotlib import pyplot as plt
import argparse

g = 9.81


def y(t, v0):
    global g
    return v0*t - 0.5*g*t**2

if __name__ == '__main__':
    # USAGE: python 10_plot_ball2.py --v0 3 5 8
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--v0", type=int, nargs='+', help="list of v0 values")
        args = parser.parse_args()
        v0_data = args.v0

        xmin, xmax, ymin, ymax = 0, 0, 0, 0
        for v0 in v0_data:
            t = np.linspace(0, 2*v0/g, 200)
            m = y(t, v0)

            if np.min(t) < xmin:
                xmin = np.min(t)
            if np.max(t) > xmax:
                xmax = np.max(t)
            if np.min(m) < ymin:
                ymin = np.min(m)
            if np.max(m) > ymax:
                ymax = np.max(m)

            plt.plot(t, m, '-', label="v0 = {}".format(v0))


        plt.legend()
        plt.xlabel('Time (s)')
        plt.ylabel('Height (m)')
        plt.title('Trajectory of a ball - v0*t - 0.5*g*t^2')
        plt.xlim(xmin - 0.1, xmax + 0.1)
        plt.ylim(ymin - 0.1, ymax + 0.1)
        plt.show()
    except IndexError:
        print("Missing input!")
    except:
        print("Unknown error!")