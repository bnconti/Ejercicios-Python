"""
Exercise 1.15: Explain why a program does not work
"""

C = A + B
A = 3
B = 2
print (C)

#  This program doesn't work because you are using the variables before defining them.
