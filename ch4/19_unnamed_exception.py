#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.19: Why we test for specific exception types
# Author: Bruno N. Conti

"""
SAMPLE RUN:
python 19_unnamed_exception.py
Missing input, C must be provided as command-line argument!

python 19_unnamed_exception.py "hi"
Invalid input, can't convert 'hi' to float!

python 19_unnamed_exception.py "help pelase"
Invalid input, can't convert 'help pelase' to float!
"""

import sys

try:
    C = float(sys.argv[1])
except IndexError:
    print("Missing input, C must be provided as command-line argument!")
    sys.exit(1)
except ValueError:
    print("Invalid input, can't convert '{}' to float!".format(sys.argv[1]))
    sys.exit(1)
except:
    print("Unknown error. Please check your input: '{}'".format(sys.argv[1]))
    sys.exit(1)
