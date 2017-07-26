# Exercise 1.17: Find errors in the coding of a formula

from math import sqrt

a = 2; b = 1; c = 2
q = b*b - 4*a*c
q_sr = sqrt(-q)*1j
x1 = (-b + q_sr)/(2*a)
x2 = (-b - q_sr)/(2*a)
print (x1) ; print(x2)

# The problem is that the program is trying to solve a negative square root.
# I think it gets fixed by multiplying q_sr by i and doing the
# square root of the negation of q.
