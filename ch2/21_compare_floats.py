# Exercise 2.21: Compare two real numbers with a tolerance

"""
SAMPLE RUN:
0.0000000000000001110223024625156540423632
0.0000000000000010000000000000000777053999
They look equal to me!
"""

a = 1/947.0*947
b = 1
tol = 1e-15

if abs(a-b) < tol:
    print("{:.40f}".format(abs(a - b)))
    print("{:.40f}".format(tol))
    print("They look equal to me!")
