# Exercise 3.25: Implement the factorial function

"""
SAMPLE RUN:
3628800
"""

def fact(n):
    f = 1
    while n>1:
        f *= n
        n -= 1
    return f


def test_fact():
    # Check an arbitrary case
    n = 4
    expected = 4*3*2*1
    computed = fact(n)
    assert computed == expected
    # Check the special cases
    assert fact(0) == 1
    assert fact(1) == 1

test_fact()
print(fact(10))
