# Exercise 3.17: Compute the length of a path

from math import sqrt


def pathlenght(x, y):
    L = 0
    values = [(xi, yi) for (xi, yi) in zip (x,y)]
    for point1, point2 in zip(values[1:], values):
        L += sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return L


def test_pathlenght():
    tol = 1E-10
    expected = sqrt(9**2 + 14**2)
    computed = pathlenght([1, 10], [1, 15])
    success = abs(expected - computed) < tol
    msg = ("COMPUTED AREA: {:.3f}. EXPECTED: {:.3f}".format(computed, expected))
    assert success, msg

test_pathlenght()