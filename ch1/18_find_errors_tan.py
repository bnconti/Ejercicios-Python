# Exercise 1.18: Find errors in a program

""" 
SAMPLE RUN:
1.00 
1.73
"""

from math import pi, tan

tan1 = tan(pi/4)
tan2 = tan(pi/3)
print ("{:.2f} \n{:.2f}".format(tan1, tan2))
