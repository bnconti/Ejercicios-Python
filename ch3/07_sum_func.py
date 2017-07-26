# Exercise 3.7: Evaluate a sum and write a test function


def sum_1k(M):
    s = 0
    for k in range(1, M+1):
        s += 1/k
    return s


def test_sum_1k():
    k = 3
    success = (sum_1k(k)-11/6) < 1E-10
    msg = ("sum_1k({}) is incorrect".format(k))
    assert success, msg

test_sum_1k()