# Exercise 3.22: Implement a Gaussian function

"""
SAMPLE RUN:
  x         f(x)
---  -----------
-24  3.3427e-126
-23  5.3706e-116
-22  3.1743e-106
-21  6.9020e-97
-20  5.5209e-88
-19  1.6246e-79
-18  1.7587e-71
-17  7.0042e-64
-16  1.0262e-56
-15  5.5307e-50
-14  1.0966e-43
-13  7.9988e-38
-12  2.1464e-32
-11  2.1188e-27
-10  7.6946e-23
 -9  1.0280e-18
 -8  5.0523e-15
 -7  9.1347e-12
 -6  6.0759e-09
 -5  1.4867e-06
 -4  1.3383e-04
 -3  4.4318e-03
 -2  5.3991e-02
 -1  2.4197e-01
  0  3.9894e-01
  1  2.4197e-01
  2  5.3991e-02
  3  4.4318e-03
  4  1.3383e-04
  5  1.4867e-06
  6  6.0759e-09
  7  9.1347e-12
  8  5.0523e-15
  9  1.0280e-18
 10  7.6946e-23
 11  2.1188e-27
 12  2.1464e-32
 13  7.9988e-38
 14  1.0966e-43
 15  5.5307e-50
 16  1.0262e-56
 17  7.0042e-64
 18  1.7587e-71
 19  1.6246e-79
 20  5.5209e-88
 21  6.9020e-97
 22  3.1743e-106
 23  5.3706e-116
 24  3.3427e-126
 25  7.6539e-137
"""

from math import exp, pi, sqrt
from tabulate import tabulate


def gauss(x, m=0, s=1):
    return (1/sqrt(2*pi)*s)*exp((-0.5*((x-m)/s)**2))

m = 1
s = 5
n = 1
values = [y for y in range(m-5*s, m+5*s, n)]
data = [gauss(x) for x in values]

table = [[x, y] for x, y in zip(values, data)]

print(tabulate(table, headers=["x", "f(x)"], tablefmt="simple", floatfmt=".4e"))