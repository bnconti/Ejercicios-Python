# Exercise 3.15: Debug a given test function


def triple(x):
    return x + x*2


def test_triple():
    assert triple(3) == 9
    assert abs(0.3 - triple(0.1)) < 1E-10
    assert triple([1, 2]) == [1, 2, 1, 2, 1, 2]
    assert triple("hello ") == "hello hello hello "

test_triple()