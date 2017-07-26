# Exercise 3.14: Simulate a program by hand


def a(x):
    q = 2
    x = 3*x
    return q + x


def b(x):
    global q
    q += x
    return q + x

q = 0
x = 3
print(a(x), b(x), a(x), b(x))