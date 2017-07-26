# Exercise 3.10: Compute a polynomial via a product


def poly(x, roots):
    t = 1
    for r in roots:
        t *= (x-r)
    return t


def test_poly():
    assert (poly(2, [1, 1, 1])) == 1
    assert (poly(5, [2, 2])) == 9
    assert (poly(3, [1, 2, 3])) == 0
    assert (poly(8, [2,4,6])) == 48

print(test_poly())

