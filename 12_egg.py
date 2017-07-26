"""
Exercise 1.12: How to cook the perfect egg
"""

from math import pi, log

M = 67  # egg mass [g]
rho = 1.038  # egg density [g/cm^-3]
c = 3.7  # specific heat capacity [J/g^-1]
K = 5.4*10**-3  # thermal conductivity [W cm^-1 K^-1]
Tw = 100  # Temperature of the boiling water [C]
T0 = 24  # Temperature of the egg plus temperature of the room [C]
Ty = 70  # Temperature that the center of the yolf has to reach [C]

t = ((M**0.67*c*rho**0.33)/(K*pi**2*(4*pi/3)**0.67))*log(0.76*((T0 - Tw)/(Ty - Tw)))

print("To hard boil the egg, cook it for {:.2f} minutes.".format(t/60))