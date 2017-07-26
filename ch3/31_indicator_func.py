# Exercise 3.31: Implement an indicator function
# File name: 31_indicator_func
# Author: Bruno N. Conti
# Date: 7/26/17

L = 0
R = 10


def indicator_direct(x, L, R):
    return 1 if L <= x <= R else 0


def H(x):
    return 1 if x >= 0 else 0


def indicator_heaviside(x, L, R):
    return 1 if H(x-L)*H(R-x) == 1 else 0


def test_indicator_direct():
    assert indicator_direct(-1, L, R) == 0
    assert indicator_direct(L, L, R) == 1
    assert indicator_direct((L+R)/2, L, R) == 1
    assert indicator_direct(R, L, R) == 1
    assert indicator_direct(11, L, R) == 0


def test_indicator_heaviside():
    assert indicator_heaviside(-1, L, R) == 0
    assert indicator_heaviside(L, L, R) == 1
    assert indicator_heaviside((L+R)/2, L, R) == 1
    assert indicator_heaviside(R, L, R) == 1
    assert indicator_heaviside(11, L, R) == 0

test_indicator_direct()
test_indicator_heaviside()