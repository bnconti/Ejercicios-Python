# Exercise 1.10: Evaluate a Gaussian function

from math import pi, sqrt, exp

m = 0
s = 2
x = 1

r = float((1/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s))**2)

print("Resultado: {:.4f}".format(r))
