"""
Exercise 2.16: Store data in lists
Modify the program from Exercise 2.2 so that all the F , C , and C' values are
stored in separate lists F, C , and C_approx, respectively. Then make a nested list
conversion so that conversion[i] holds a row in the table: [F[i], C[i],
C_approx[i]] . Finally, let the program traverse the conversion list and write
out the same table as in Exercise 2.2.
"""

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]

Fdegrees = [9/5*C + 32 for C in Cdegrees]

Cprimedegrees = [(F-30)/2 for F in Fdegrees]

temperatures = [[F, C, Cp] for F, C, Cp in zip(Fdegrees, Cdegrees, Cprimedegrees)]

print("-----------------------")
print("{:>6}{:>6}{:>8}".format("F", "C", "C'"))
print("-----------------------")
for F, C, Cp in temperatures:
    print ("{:6.1f} {:5d} {:7.1f}".format(F, C, Cp))
print('-----------------------')
