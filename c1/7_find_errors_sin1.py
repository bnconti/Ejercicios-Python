# Exercise 1.7: Find error(s) in a program

"""
SAMPLE RUN:
sin(0.0174533)=0.0174524
"""

# MY FRIEND, TO FIX THE PROGRAM YOU NEED TO CONVERT x TO RADIANS BY DOING (THETA*PI)/180!

from math import sin, pi

x = (1*pi)/180
print('sin(%g)=%g' % (x, sin(x)))
