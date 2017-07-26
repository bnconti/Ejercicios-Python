# Exercise 3.23: Wrap a formula in a function

from math import pi, log

# M = 67  # egg mass [g]
# rho = 1.038  # egg density [g/cm^-3]
# c = 3.7  # specific heat capacity [J/g^-1]
# K = 5.4 * 10 ** -3  # thermal conductivity [W cm^-1 K^-1]
# Tw = 100  # Temperature of the boiling water [C]
# T0 = 24  # Temperature of the egg plus temperature of the room [C]
# Ty = 70  # Temperature that the center of the yolf has to reach [C]


def egg(M, T0=20, Ty=70):
    rho = 1.038
    K = 5.4*10**-3
    c = 3.7
    Tw = 100
    return ((M**0.67*c*rho**0.33)/(K*pi**2*(4*pi/3)**0.67))*log(0.76*((T0 - Tw)/(Ty - Tw)))


print("To hard boil the big egg taken from the fridge, cook it for {:.2f} minutes.".format(egg(67, 4)/60))
print("To hard boil the big egg with room temperature, cook it for {:.2f} minutes.".format(egg(67, 25)/60))

print("To hard boil the little egg taken from the fridge, cook it for {:.2f} minutes.".format(egg(47, 4)/60))
print("To hard boil the little egg with room temperature, cook it for {:.2f} minutes.".format(egg(47, 25)/60))