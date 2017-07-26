# Exercise 3.22: Implement a Gaussian function

from math import exp, pi, sqrt
from tabulate import tabulate


def gauss(x, m=0, s=1):
    return (1/sqrt(2*pi)*s)*exp((-0.5*((x-m)/s)**2))

m = 1
s = 5
n = 1
values = [y for y in range(m-5*s, m+5*s, n)]
data = [gauss(x) for x in values]

table = [[x,y] for x,y in zip(values, data)]

print(tabulate(table, headers=["x", "f(x)"], tablefmt="simple", floatfmt=".4e"))