# Exercise 3.4: Write a Fahrenheit-Celsius conversion functions


def F(f):
    c = 5/9*(f - 32)
    return c


def C(c):
    f = 9/5*c + 32
    return f

f = 32
c = 0

print("{:2}C° equals {:4}C°? {}".format(c, C(F(c)), C(F(c)) == c))
print("{:2}F° equals {:4}F°? {}".format(c, F(C(f)), F(C(f)) == f))
