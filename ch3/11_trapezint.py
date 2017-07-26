# Exercise 3.11: Integrate a function by the Trapezoidal rule

from math import cos, sin, pi

functions = [(cos, 0, pi), (sin, 0, pi), (sin, 0, pi/2)]


def test_trapezint1():
    trapezint1 = lambda f, a, b: ((b - a) / 2) * (f(a) + f(b))
    values1 = [trapezint1(f, a, b) for (f, a, b) in functions]
    print("One trapezoid.")
    error1 = [0-values1[0], 2-values1[1], 1-values1[2]]
    for f, v, e in zip(functions, values1, error1):
        print("Function {}, from {:.3f} to {:.3f}. Approximation of area: {:.6f}. Margin of error: {:.5f}"
              .format(f[0].__name__, f[1], f[2], v, e))


def test_trapezint2():
    trapezint2 = lambda f, a, b: (b - a) / 4 * (f(a) + 2 * f((a + b) / 2) + f(b))
    values2 = [trapezint2(cos, 0, pi), trapezint2(sin, 0, pi), trapezint2(sin, 0, pi / 2)]
    print("Two trapezoids.")
    error2 = [0 - trapezint2(cos, 0, pi), 2 - trapezint2(sin, 0, pi), 1 - trapezint2(sin, 0, pi / 2)]
    for f, v, e in zip(functions, values2, error2):
        print("Function {}, from {:.3f} to {:.3f}. Approximation of area: {:.6f}. Margin of error: {:.5f}"
              .format(f[0].__name__, f[1], f[2], v, e))


def trapezint(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(1, n):
        x1 = a + i*h
        x2 = a + ((i+1)*h)
        result += 0.5 * h * (f(x1) + f(x2))
    return result


def test_trapezint():
    values = [trapezint(f[0], f[1], f[2], 5) for f in functions]
    print("Five trapezoids.")
    error = [0 - values[0], 2 - values[1], 1 - values[2]]
    for f, v, e in zip(functions, values, error):
        print("Function {}, from {:.3f} to {:.3f}. Approximation of area: {:.6f}. Margin of error: {:.5f}"
              .format(f[0].__name__, f[1], f[2], v, e))

#test_trapezint1()
#test_trapezint2()
test_trapezint()