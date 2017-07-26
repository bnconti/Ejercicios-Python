"""
Exercise 1.7: Find error(s) in a program
Suppose somebody has written a simple one-line program for computing sin(1):
x=1; print ’sin(%g)=%g’ % (x, sin(x))
Create this program and try to run it. What is the problem?
"""

from math import sin, pi

x = (1*pi)/180

print ('sin(%g)=%g' % (x, sin(x)))

# MY FRIEND, TO FIX THE PROGRAM YOU NEED TO CONVERT x TO RADIANS BY DOING (THETA*PI)/180!!