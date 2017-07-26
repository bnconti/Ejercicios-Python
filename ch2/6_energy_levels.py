# Exercise 2.6: Compute energy levels in an atom

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

print("END")
