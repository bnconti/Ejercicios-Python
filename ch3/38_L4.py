# Exercise 3.38: Use None in keyword arguments
# Author: Bruno N. Conti
# Date: 7/27/17

def L2(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    value_of_sum = s
    first_neglected_term = (1.0/(n+1))*(x/(1.0+x))**(n+1)
    from math import log
    exact_error = log(1+x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error


def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i


def L4(x, n=None, epsilon=None, return_n=False):
    assert n is not None and epsilon is not None, "You can only choose one method!"
    assert n is None and epsilon is None, "You can't choose both methods!"
    if n is not None:
        return L2(x, n)
    if epsilon is not None:
        if return_n is not None:
            return L3(x, epsilon)
        else:
            s = L3(x, epsilon)
            return s

print(L4(10, n=5, epsilon=1E-10))
print(L4(3))