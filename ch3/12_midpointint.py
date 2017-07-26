# Exercise 3.12: Derive the general Midpoint integration rule

from math import cos, sin, pi

functions = [(cos, 0, pi), (sin, 0, pi), (sin, 0, pi/2)]


def midpointint(f, a, b, n):
    h = (b-a)/n
    r = 0
    for i in range(0, n):
        r += f(a+i*h+0.5*h)
    return h*r

def test_midpointint():
    values_1n = [midpointint(f[0], f[1], f[2], 1) for f in functions]
    values_10n = [midpointint(f[0], f[1], f[2], 10) for f in functions]
    error_1n = [0 - values_1n[0], 2 - values_1n[1], 1 - values_1n[2]]
    error_10n = [0 - values_10n[0], 2 - values_10n[1], 1 - values_10n[2]]
    print("One rectangle.")
    for f, v, e in zip(functions, values_1n, error_1n):
        print("Area of {}(x) from {:.3f} to {:.3f}. Approximation: {:.5f}. Margin of error: {:.5f}"
              .format(f[0].__name__, f[1], f[2], v, e))
    print("Ten rectangles.")
    for f, v, e in zip(functions, values_10n, error_10n):
        print("Area of {}(x) from {:.3f} to {:.3f}. Approximation: {:.5f}. Margin of error: {:.5f}"
              .format(f[0].__name__, f[1], f[2], v, e))

test_midpointint()

# The midpoint method is a lot more precise than the trapezoidal method!

"""
One rectangle.
Area of cos(x) from 0.000 to 3.142. Approximation: 0.00000. Margin of error: -0.00000
Area of sin(x) from 0.000 to 3.142. Approximation: 3.14159. Margin of error: -1.14159
Area of sin(x) from 0.000 to 1.571. Approximation: 1.11072. Margin of error: -0.11072
Ten rectangles.
Area of cos(x) from 0.000 to 3.142. Approximation: 0.00000. Margin of error: -0.00000
Area of sin(x) from 0.000 to 3.142. Approximation: 2.00825. Margin of error: -0.00825
Area of sin(x) from 0.000 to 1.571. Approximation: 1.00103. Margin of error: -0.00103
"""