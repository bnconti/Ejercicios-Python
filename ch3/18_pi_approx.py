# Exercise 3.18: Approximate pi

from math import pi, sqrt, sin, cos

values = [2**k for k in range(1, 11)]
approximations = []
for n in values:
    approx = 0
    for i in range(1, n+1):
        x1 = 0.5*cos(2*pi*i/n); y1 = 0.5*sin(2*pi*i/n); x2 = 0.5*cos(2*pi*(i-1)/n); y2 = 0.5*sin(2*pi*(i-1)/n)
        approx += sqrt((x1 - x2)**2 + (y1 - y2)**2)
    approximations.append(approx)

for approx_pi, value in zip(approximations, values):
    print("{:>4} -> {:.17f} || Margin of error: {:.17f}".format(value, approx_pi, abs(pi-approx_pi)))