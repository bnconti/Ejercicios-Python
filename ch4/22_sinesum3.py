#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.22: Read options and values from the command line
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 22_sinesum3.py --n 1 10 100 500 10000 --a 0.0001 0.01 0.1  0.5 --T 6.28

ERROR     0.0001     0.01       0.1        0.5

    1    1.0e+00    9.2e-01    2.5e-01    1.0e+00

   10    9.9e-01    2.5e-01    7.3e-01    9.8e-01

  100    9.2e-01    3.0e-02    7.5e-01    8.0e-01

  500    6.1e-01    7.0e-02    7.5e-01    1.2e-01

10000    4.9e-02    8.0e-02    7.5e-01    1.6e-02

"""

import argparse
from math import pi
from importlib import import_module
sinesum = import_module('_sinesum2')

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, nargs='+', default=[1, 5, 50, 1000], help="range of values")
parser.add_argument("--a", type=float, nargs='+', default=[0.001, 0.01, 0.5, 0.25, 0.50], help="increment")
parser.add_argument("--T", type=float, default=pi*2, help="period")

args = parser.parse_args()
n_values = args.n
alpha_values = args.a
T = args.T

sinesum.table(n_values, alpha_values, T)
