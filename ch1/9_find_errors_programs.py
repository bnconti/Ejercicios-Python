# Exercise 1.9: Type in programs and debug them

"""
SAMPLE RUN:
1.0
4.0
First equation: 73.96 = 73.96
Second equation: 4 = 4
"""

# a) Does (sin x)**2 + (cos x)**2 = 1?

from math import sin, cos, pi
x = pi/4
val_1 = (sin(x))**2 + (cos(x))**2
print(val_1)

# DEBUGGED!

# b) Compute s in meters when s = v0*t + 1/2a*t**2,
# with v0 = 3 m/s, t = 1 s, a = 2 m/s**2.

v0 = 3
t = 1
a = 2

s = v0*t + 0.5*a*t**2

print(s)

# DEPURADO!

# c) Verify these equations:
# (a + b)**2 = a**2 + 2ab + b**2
# (a - b)**2 = a**2 - 2ab + b**2

a = 3.3
b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a**2 + 2*a*b + b**2
eq2_sum = a**2 - 2*a*b + b**2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print("First equation: %g = %g" % (eq1_sum, eq1_pow))
print("Second equation: %g = %g" % (eq2_sum, eq2_pow))

# PURGADO!
