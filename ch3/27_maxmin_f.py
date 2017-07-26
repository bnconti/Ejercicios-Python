# Exercise 3.27: Find the max and min values of a function

from math import cos, pi

def maxmin(f, a, b, n=1000):
    h = (b - a) / (n - 1)
    values = []
    for i in range(n):
        x_i = a + i*h
        values.append(f(x_i))
    return max(values), min(values)

max, min = maxmin(lambda x: cos(x), -pi/2, 2*pi)
print("Max: {:>5.2f} \nMin: {:>5.2f}".format(max, min))

# There is more than 1 maximum value on that interval, but the function max() gives you only one max. value.
