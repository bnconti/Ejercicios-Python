#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.24: Compute probabilities with the binomial distribution
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Probability of getting 2 heads when flipping a coin 5 times: 31.25%
Probability of getting 4 ones in a row when throwing a die 4 times: 0.08%
Probability of breaking your ski 1 time in 5 competitions: 4.10%
"""

from math import factorial as f

def binomial(x, n, p):
    """
    :param x: ammount of successes that we want (x <= n)
    :param n: amount of tests
    :param p: probability of success of each test
    :return: probability of success (x times)
    """
    return f(n) / (f(x)*(f(n-x))) * p**x * (1-p)**(n-x)

if __name__ == '__main__':
    print("Probability of getting 2 heads when flipping a coin 5 times: {:.2%}".format(binomial(2, 5, 0.5)))
    print("Probability of getting 4 ones in a row when throwing a die 4 times: {:.2%}".format(binomial(4, 4, 1/6)))
    print("Probability of breaking your ski 1 time in 5 competitions: {:.2%}".format(1 - binomial(0, 5, 1/120)))
