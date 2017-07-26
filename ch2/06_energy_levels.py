# Exercise 2.6: Compute energy levels in an atom

"""
SAMPLE RUN:
-----------------------------------
 n        Energy levels at n
-----------------------------------
 1        -2.180e-18
 2        -5.450e-19
 3        -2.422e-19
 4        -1.362e-19
 5        -8.720e-20
 6        -6.055e-20
 7        -4.449e-20
 8        -3.406e-20
 9        -2.691e-20
10        -2.180e-20
11        -1.802e-20
12        -1.514e-20
13        -1.290e-20
14        -1.112e-20
15        -9.689e-21
16        -8.516e-21
17        -7.543e-21
18        -6.728e-21
19        -6.039e-21
20        -5.450e-21
-----------------------------------
Energy released from 1 to 2 = -1.6e-18
Energy released from 1 to 3 = -1.9e-18
Energy released from 1 to 4 = -2.0e-18
Energy released from 1 to 5 = -2.1e-18
Energy released from 2 to 3 = -3.0e-19
Energy released from 2 to 4 = -4.1e-19
Energy released from 2 to 5 = -4.6e-19
Energy released from 3 to 4 = -1.1e-19
Energy released from 3 to 5 = -1.6e-19
Energy released from 4 to 5 = -4.9e-20
"""

# a) Write a Python program that calculates and prints the energy level E_n for n = 1, ..., 20.

m_e = 9.1094*10**-31 #  electron mass [Kg]
e = 1.6022*10**-19 #  elementary charge [C]
epsilon_0 = 8.8542*10**-12 #  electrical permittivity of vacuum [C**2 s**2 kg**-1 m**-3]
h = 6.6261*10**-34 #  [Js]

n = 1
energy_levels = [-((m_e*e**4)/(8*epsilon_0**2*h**2))*(1/n**2) for n in range(1, 21, 1)]

print("-----------------------------------")
print("{:>2}{:>26}".format("n", "Energy levels at n"))
print("-----------------------------------")
for energy in energy_levels:
    print("{:>2}{:18.3e}".format(energy_levels.index(energy)+1, energy))
print("-----------------------------------")

# b) Released energy from i to f

released_energy = []

for i in range(1, 6):
    temp = []
    for f in range(i+1, 6):
        deltaE = - ((m_e*e**4) / (8*epsilon_0**2*h**2)) * ((1/i**2) - (1/f**2))
        temp.append(deltaE)
    if temp is not True:
        released_energy.append(temp)

for i in released_energy:
    for f in i:
        print("Energy released from {} to {} = {:.1e}".format(released_energy.index(i)+1, released_energy.index(i)+i.index(f)+2, f))
