# Exercise 3.28: Find the max and min elements in a list

import random


def max(a):
    M = a[0]
    for v in a[1:]:
        if v > M:
            M = v
    return M


def min(a):
    m = a[0]
    for v in a[1:]:
        if v < m:
            m = v
    return m

a = random.sample(range(-10000, 10000), 20)
print(max(a))
print(min(a))
