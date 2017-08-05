#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.23: Check if mathematical identities hold
# Author: Bruno N. Conti

"""
SAMPLE RUN:
ERROR                            FUNCTIONS                                          RANGE
 0.0%                           a-b == -(b-a)                                      (1, 2)
 0.0%                           a-b == -(b-a)                                    (1, 100)
25.9%                           a/b == 1/(b/a)                                     (1, 2)
24.5%                           a/b == 1/(b/a)                                   (1, 100)
71.1%                      (a*b)**4 == a**4*b**4                                   (1, 2)
73.4%                      (a*b)**4 == a**4*b**4                                 (1, 100)
45.0%                      (a+b)**2 == a**2 + 2*a*b + b**2                         (1, 2)
54.7%                      (a+b)**2 == a**2 + 2*a*b + b**2                       (1, 100)
67.9%                   (a+b)*(a-b) == a**2 - b**2                                 (1, 2)
51.1%                   (a+b)*(a-b) == a**2 - b**2                               (1, 100)
58.0%                      exp(a+b) == exp(a)*exp(b)                               (1, 2)
78.4%                      exp(a+b) == exp(a)*exp(b)                             (1, 100)
55.0%                     log(a**b) == b*log(a)                                    (1, 2)
25.7%                     log(a**b) == b*log(a)                                  (1, 100)
43.9%                      log(a*b) == log(a) + log(b)                             (1, 2)
24.7%                      log(a*b) == log(a) + log(b)                           (1, 100)
29.4%                           a*b == exp(log(a)+log(b))                          (1, 2)
86.5%                           a*b == exp(log(a)+log(b))                        (1, 100)
46.3%                 1/(1/a + 1/b) == a*b/(a+b)                                   (1, 2)
46.3%                 1/(1/a + 1/b) == a*b/(a+b)                                 (1, 100)
26.6%     a*(sin(b)**2 + cos(b)**2) == a                                           (1, 2)
19.9%     a*(sin(b)**2 + cos(b)**2) == a                                         (1, 100)
56.0%                     sinh(a+b) == (exp(a)*exp(b) - exp(-a)*exp(-b))/2         (1, 2)
77.3%                     sinh(a+b) == (exp(a)*exp(b) - exp(-a)*exp(-b))/2       (1, 100)
31.3%                      tan(a+b) == sin(a+b)/cos(a+b)                           (1, 2)
32.4%                      tan(a+b) == sin(a+b)/cos(a+b)                         (1, 100)
68.2%                      sin(a+b) == sin(a)*cos(b) + sin(b)*cos(a)               (1, 2)
82.8%                      sin(a+b) == sin(a)*cos(b) + sin(b)*cos(a)             (1, 100)
"""

from math import exp, log, sin, cos, sinh, tan

import random

def power3_identity(A=-100, B=100, n=1000):
    fail = 0
    for i in range(0, n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        if (a*b)**3 != a**3 * b**3:
            fail += 1
    return fail/n, fail


def equal(expr1, expr2, A=-100, B=100, n=1000):
    fail, i = 0, 0
    while i < n:
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        try:
            if eval(expr1) != eval(expr2):
                fail += 1
            i +=1
        except TypeError:
            continue
        except ValueError:
            continue
    return fail*100/n

equivalent_functions = [
    ('a-b', '-(b-a)'),
    ('a/b', '1/(b/a)'),
    ('(a*b)**4', 'a**4*b**4'),
    ('(a+b)**2', 'a**2 + 2*a*b + b**2'),
    ('(a+b)*(a-b)', 'a**2 - b**2'),
    ('exp(a+b)', 'exp(a)*exp(b)'),
    ('log(a**b)', 'b*log(a)'),
    ('log(a*b)', 'log(a) + log(b)'),
    ('a*b', 'exp(log(a)+log(b))'),
    ('1/(1/a + 1/b)', 'a*b/(a+b)'),
    ('a*(sin(b)**2 + cos(b)**2)', 'a'),
    ('sinh(a+b)', '(exp(a)*exp(b) - exp(-a)*exp(-b))/2'),
    ('tan(a+b)', 'sin(a+b)/cos(a+b)'),
    ('sin(a+b)', 'sin(a)*cos(b) + sin(b)*cos(a)')
]

with open('23_output.txt', 'w') as outfile:
    outfile.write("{:<20}{:^35}{:>34}\n".format("ERROR", "FUNCTIONS", "RANGE"))
    range1 = (1,2); range2 = (1,100)
    for f in equivalent_functions:
        error = equal(f[0], f[1], A=range1[0], B=range1[1])
        outfile.write("{:>4.1f}%{:>30} == {:<40}{:>10}\n".format(error, f[0], f[1], str(range1)))
        error = equal(f[0], f[1], A=range2[0], B=range2[1])
        outfile.write("{:>4.1f}%{:>30} == {:<40}{:>10}\n".format(error, f[0], f[1], str(range2)))

"""
Only in some functions the values of A and B seem to affect the quantity of errors.
"""