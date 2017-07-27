# File name: 32_piecewise_constant1
# Author: Bruno N. Conti
# Date: 7/26/17


def piecewise(x, data):
    # data = [pair_1, pair_2, ..., pair_n]
    # pair_i = (vi, xi)
    # Return vi if x belongs to the interval [xi, xi+1)
    for pair_1, pair_2 in zip(data, data[1:]):
        if pair_1[1] <= x < pair_2[1]:
            return pair_1[0]
    print("ERROR: {} is not on the given interval.".format(x))


def test_piecewise():
    assert piecewise(0.5, [(-1, -10), (1, 0), (2, 10)]) is 1
    assert piecewise(-5, [(-1, -10), (1, 0), (2, 10)]) is -1
    assert piecewise(1, [(2, 0), (3, 100), (4, 1000), (5, 10000)]) is 2
    assert piecewise(-10, [(2, 0), (3, 100), (4, 1000), (5, 10000)]) is None
