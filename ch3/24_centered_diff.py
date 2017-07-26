# Exercise 3.24: Write a function for numerical differentiation

"""
SAMPLE RUN:
| Function     |  Input  |  Approx.  |  Exact val.  |    Error    |
|--------------+---------+-----------+--------------+-------------|
| exp(x)       |    0    |  1.00002  |      1       | 1.66667e-05 |
| exp(-2*x**2) |    0    |     0     |      0       |      0      |
| cos(x)       | 6.28319 |     0     |      0       |      0      |
| log(x)       |    1    |  1.00003  |      1       | 3.33353e-05 |
"""


from math import sqrt, exp, cos, log, pi
from tabulate import tabulate


def diff(f, x, h=1E-5):
    return 1 / (2*h) * (f(x+h) - f(x-h))


def test_diff():
    tol = 1E-8
    functions = [lambda x: x**2, lambda x: x**3, lambda x: sqrt(x)]
    values = [3, 2, 4]
    approximations = []
    for f, x in zip(functions, values):
        approximations.append(diff(f, x))
    exact_results = [6, 12, 0.25]
    for y, e in zip(approximations, exact_results):
        assert abs(y-e) < tol, print("Expected {}, received {}".format(e, y))

test_diff()


def application():
    functions = [lambda x: exp(x), lambda x: exp(-2*x**2), lambda x: cos(x), lambda x: log(x)]
    input_values = [0, 0, 2*pi, 1]
    approximations = [diff(f, x, h=0.01) for f, x in zip(functions, input_values)]
    exact_values = [1, 0, 0, 1]
    functions_names = ["exp(x)", "exp(-2*x**2)", "cos(x)", "log(x)"]
    input_names = [str(x) for x in input_values]
    table = [(f, x, y1, y2, y1-y2) for f, x, y1, y2 in zip(functions_names, input_names, approximations, exact_values)]
    print(tabulate(table, headers=['Function', 'Input', 'Approx.', 'Exact val.', 'Error'], tablefmt="orgtbl", numalign="center"))

application()
