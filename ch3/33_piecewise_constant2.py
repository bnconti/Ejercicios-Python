# Exercise 3.33: Apply indicator functions
# Author: Bruno N. Conti
# Date: 7/26/17
# Run pytest 33_piecewise_constant2.py for testing


def indicator_direct(x, L, R):
    return 1 if L <= x < R else 0


def piecewise_indicator(x, data):
    S = 0
    for pair_1, pair_2 in zip(data, data[1:]):
        S += pair_1[0]*indicator_direct(x, pair_1[1], pair_2[1])
    return S


def test_piecewise():
    assert piecewise_indicator(0.5, [(-1, -10), (1, 0), (2, 10)]) is 1
    assert piecewise_indicator(-5, [(-1, -10), (1, 0), (2, 10)]) is -1
    assert piecewise_indicator(1, [(2, 0), (3, 100), (4, 1000), (5, 10000)]) is 2
    assert piecewise_indicator(100, [(2, 0), (3, 100), (4, 1000), (5, 10000)]) is 3
