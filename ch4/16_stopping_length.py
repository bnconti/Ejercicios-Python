#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.16: Compute the distance it takes to stop a car
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 16_stopping_length.py 40
Distance needed to break at 40.0 km/h: 21.0 m

python 16_stopping_length.py 60
Distance needed to break at 60.0 km/h: 47.2 m

python 16_stopping_length.py 110
Distance needed to break at 110.0 km/h: 158.6 m
"""

import sys


def distance(v0, mu=0.3, g=9.81):
    """
    :param v0: velocity of the car
    :param mu: friction coefficient
    :param g: gravity
    :return: d = braking distance needed
    """
    v0 /= 3.6   # conversion from km/h to m/s
    d = 0.5 * v0**2/(mu*g)
    return d


def input_v0():
    try:
        v0 = float(sys.argv[1])
        return v0
    except Exception as e:
        print(e)
        sys.exit(1)

v0 = input_v0()
print("Distance needed to break at {:.1f} km/h: {:.1f} m".format(v0, distance(v0)))
