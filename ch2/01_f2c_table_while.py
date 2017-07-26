# Exercise 2.1: Make a Fahrenheit-Celsius conversion table

"""
SAMPLE RUN:
------------------
    F     C
------------------
 -4.0   -20
  5.0   -15
 14.0   -10
 23.0    -5
 32.0     0
 41.0     5
 50.0    10
 59.0    15
 68.0    20
 77.0    25
 86.0    30
 95.0    35
104.0    40
-----------------
"""

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
Fdegrees = [9/5*C + 32 for C in Cdegrees]

print("------------------")
print("{:>5}{:>6}".format("F", "C"))
print("------------------")
for F, C in zip(Fdegrees, Cdegrees):
    print ("{:5.1f} {:5d}".format(F, C))
print('------------------')
