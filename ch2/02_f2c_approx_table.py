# Exercise 2.2: Generate an approximate Fahrenheit-Celsius conversion table

"""
SAMPLE RUN:
-----------------------
     F     C      C'
-----------------------
  -4.0   -20   -17.0
   5.0   -15   -12.5
  14.0   -10    -8.0
  23.0    -5    -3.5
  32.0     0     1.0
  41.0     5     5.5
  50.0    10    10.0
  59.0    15    14.5
  68.0    20    19.0
  77.0    25    23.5
  86.0    30    28.0
  95.0    35    32.5
 104.0    40    37.0
-----------------------
"""

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
Fdegrees = [9/5*C + 32 for C in Cdegrees]
Cprimedegrees = [(F-30)/2 for F in Fdegrees]

print("-----------------------")
print("{:>6}{:>6}{:>8}".format("F", "C", "C'"))
print("-----------------------")
for F, C, Cp in zip(Fdegrees, Cdegrees, Cprimedegrees):
    print ("{:6.1f} {:5d} {:7.1f}".format(F, C, Cp))
print('-----------------------')
