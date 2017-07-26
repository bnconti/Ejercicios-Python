# Exercise 2.1: Make a Fahrenheit-Celsius conversion table

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]

Fdegrees = [9/5*C + 32 for C in Cdegrees]

print("------------------")
print("{:>5}{:>6}".format("F", "C"))
print("------------------")
for F, C in zip(Fdegrees, Cdegrees):
    print ("{:5.1f} {:5d}".format(F, C))
print('------------------')
