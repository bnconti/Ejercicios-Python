"""
Exercise 2.17: Store data in a nested list

The purpose of this exercise is to store tabular data in two alternative ways, either
as a list of columns or as a list of rows. In order to write out a nicely formatted
table, one has to traverse the data, and the technique for traversal depends on how
the tabular data is stored.

a) Compute two lists of t and y values as explained in Exercise 2.9. Store the two
lists in a new nested list ty1 such that ty1[0] and ty1[1] correspond to the
two lists. Write out a table with t and y values in two columns by looping over
the data in the ty1 list. Each number should be written with two decimals.

b) Make a list ty2 which holds each row in the table of t and y values ( ty1 is a list
of table columns while ty2 is a list of table rows, as explained in Sect. 2.4).
Loop over the ty2 list and write out the t and y values with two decimals each.
"""

v_0 = 10  # Initial velocity
g = 9.81  # Gravity

a = 0; b = 2*v_0/g; n = 10; h = (b-a)/n

intervals = [a+i*h for i in range(0, n+1)]  # t

values = [v_0*t - 0.5*g*t**2 for t in intervals]  # y

print("------------")

# a
ty1 = [[], []]
for t in intervals:
    ty1[0].append(t)

for y in values:
    ty1[1].append(y)

for t, y in zip(ty1[0], ty1[1]):
    print("y({:.2f}) = {:.2f}".format(t, y))

print("------------")

# b
ty2 = [[t, y] for t, y in zip(intervals, values)]
for t, y in ty2:
    print("y({:.2f}) = {:.2f}".format(t, y))

print("------------")
