# Exercise 2.2: Generate an approximate Fahrenheit-Celsius conversion table

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]

Fdegrees = [9/5*C + 32 for C in Cdegrees]

Cprimedegrees = [(F-30)/2 for F in Fdegrees]

print("-----------------------")
print("{:>6}{:>6}{:>8}".format("F", "C", "C'"))
print("-----------------------")
for F, C, Cp in zip(Fdegrees, Cdegrees, Cprimedegrees):
    print ("{:6.1f} {:5d} {:7.1f}".format(F, C, Cp))
print('-----------------------')
