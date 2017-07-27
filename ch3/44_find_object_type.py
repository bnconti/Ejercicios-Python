# Exercise 3.44: Determine the types of some objects
# Author: Bruno N. Conti

"""
This exercise demonstrates that we can write a function and have in mind
certain types of arguments, here typically int and float objects. However, the
function can be used with other (originally unintended) arguments, such as lists and
strings in the present case, leading to strange and irrelevant behavior (the problem
here lies in the boolean expression value <= stop which is meaningless for some
of the arguments).
"""


def makelist(start, stop, inc):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value = value + inc
    return result


l1 = makelist(0, 100, 1)
# [0, 1, 2, ..., 100]

l2 = makelist(0, 100, 1.0)
# [0, 1.0, 2.0, ..., 100.0]

l3 = makelist(-1, 1, 0.1)
# [-1, -0.9, -0.8, ..., 1]

l4 = makelist(10, 20, 20)
# [10]

# l5 = makelist([1, 2], [3, 4], [5])
# This one hangs the computer (infinite loop)!

# l6 = makelist((1, -1, 1), ("myfile.dat", "yourfile.dat"))
# Doesn't work

# l7 = makelist("myfile.dat", "yourfile.dat", "herfile.dat’")
# Doesn't work

print(l1)
print(l2)
print(l3)
print(l4)
