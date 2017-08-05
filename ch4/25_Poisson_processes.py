#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.25: Compute probabilities with the Poisson distribution
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Taxis problem - 5 per hour.
Prob. of getting 0 taxis after waiting 30 minutes: 8.21%
Prob. of having to wait 2 hour for 1 taxi: 0.05%
Prob. of 2 taxis arriving in a period of 20 minutes: 26.23%
=====
Earthquakes problem - 10 per 50 years.
Prob. of experiencing 3 earthquakes over a period of 10 years: 18.04%
Prob. that a visitor does not experience any earthquake in a period of 1 week: 99.62%
=====
Missprints problem - 6 per page.
Prob. of a reader of finding 0 missprints in 6 pages: 0.00000000000002320%
"""

import sys
from math import exp
from math import factorial as f

def Poisson(x, t, v):
    """
    :param x: amount of events
    :param t: given time
    :param v: events per time unit
    :return: probability
    """
    return (((v * t) ** x) / f(x)) * exp(-v * t)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            x = float(sys.argv[1])
            t = float(sys.argv[2])
            nu = float(sys.argv[3])
        except IndexError:
            print("Missing input!")
            exit(1)
        except ValueError:
            print("Invalid input!")
            exit(1)
        except:
            print("Unknown error!")
            exit(1)
    else:
        print("Taxis problem - 5 per hour.")
        print("Prob. of getting 0 taxis after waiting 30 minutes: {:.2%}"
              .format(Poisson(0, 1/2, 5)))
        print("Prob. of having to wait 2 hour for 1 taxi: {:.2%}"
              .format(Poisson(1, 2, 5)))
        print("Prob. of 2 taxis arriving in a period of 20 minutes: {:.2%}"
              .format(Poisson(2, 1/3, 5)))
        print("=====")
        print("Earthquakes problem - 10 per 50 years.")
        print("Prob. of experiencing 3 earthquakes over a period of 10 years: {:.2%}"
              .format(Poisson(3, 10, 0.2)))
        print("Prob. that a visitor does not experience any earthquake in a period of 1 week: {:.2%}"
              .format(Poisson(0, 1/52, 0.2)))
        print("=====")
        print("Missprints problem - 6 per page.")
        print("Prob. of a reader of finding 0 missprints in 6 pages: {:.17%}"
              .format(Poisson(0, 6, 6)))

