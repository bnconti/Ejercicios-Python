# Exercise 3.21: Approximate a function by a sum of sines

"""
SAMPLE RUN:
==================================================
|      ||                alpha                   |
--------------------------------------------------
|   n  ||      0.01        0.25        0.49      |
--------------------------------------------------
|   1  ||    0.920053   -0.273240    0.920053    |
|   3  ||    0.760578   -1.122066    0.760578    |
|   5  ||    0.604442   -1.194822    0.604442    |
|  10  ||    0.249157   -1.308500    0.249157    |
|  30  ||   -0.236327   -1.284212   -0.236327    |
| 100  ||   -0.030255   -1.276455   -0.030255    |
==================================================
"""

from math import sin, pi

__all__ = ['S', 'f']

def S(t, n, T=2*pi):
    s = 0
    for i in range(n):
        s += (1/(2*i-1)) * sin((2*(2*i-1)*pi*t)/T)
    return 4/pi*s


def f(t, T=2*pi):
    if 0 < t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2 < t < T:
        return -1

if __name__ == '__main__':
    n = [1, 3, 5, 10, 30, 100]
    T = 2*pi
    alpha = [0.01, 0.25, 0.49]
    # t = alpha*T

    approximations = []
    for n_i in n:
        row_list = []
        for alpha_i in alpha:
            t = alpha_i*T
            row_list.append(f(t) - S(t, n_i))
        approximations.append(row_list)


    print("{}".format("="*50))
    print("|      || {:>20}{:>20}".format("alpha", "|"))
    print("{}".format("-"*50))
    print("|   n  || {:>9} {:>11} {:>11} {:>6}".format(alpha[0], alpha[1], alpha[2], '|'))
    print("{}".format("-"*50))
    for n_i, row in zip(n, approximations):
        print("| {:>3} {:>3}".format(n_i, '||'), end='')
        for elem in row:
            print("{:>12.6f}".format(elem,), end='')
        print("{:>5}".format("|"))
    print("{}".format("="*50))