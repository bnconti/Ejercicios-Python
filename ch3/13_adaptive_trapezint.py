# Exercise 3.13: Make an adaptive Trapezoidal rule

from math import sqrt, cos, pi, sin

functions = [(cos, 0, pi), (sin, 0, pi), (sin, 0, pi/2)]


def trapezint(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(1, int(n)):
        x1 = a + i*h
        x2 = a + ((i+1)*h)
        result += 0.5 * h * (f(x1) + f(x2))
    return result


def diff2(f, x, h=1E-6):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)


def adaptive_trapezint(f, a, b, eps=1E-5):
    ddf = []
    for i in range(101):
        x = a + i*(b - a)/100
        ddf.append(abs(diff2(f, x)))
    max_ddf = max(ddf)
    h = sqrt(12 * eps) * 1 / sqrt((b - a) * max_ddf)
    n = (b - a) / h
    return trapezint(f, a, b, n)


def test_adaptative_trapezint():
    values = [adaptive_trapezint(f[0], f[1], f[2]) for f in functions]
    print(values)
    error = [0 - values[0], 2 - values[1], 1 - values[2]]
    for f, v, e in zip(functions, values, error):
        print("Function {}, from {:.3f} to {:.3f}. Approximation of area: {:.6f}. Margin of error: {:.5f}"
              .format(f[0].__name__, f[1], f[2], v, e))

test_adaptative_trapezint()