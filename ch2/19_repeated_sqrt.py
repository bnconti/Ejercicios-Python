# Exercise 2.19: Explore round-off errors from a large number of inverse operations

from math import sqrt
# for n in range(1, 60):
#     r = 2.0
#     for i in range(n):
#         r = sqrt(r)
#     for i in range(n):
#         r = r**2
#     print('%d times sqrt and **2: %.16f' % (n, r))

"""Explain with words what the program does. Then run the program. Round-off
errors are here completely destroying the calculations when n is large enough! In-
vestigate the case when we come back to 1 instead of 2 by fixing an n value where
this happens and printing out r in both for loops over i . Can you now explain why
we come back to 1 and not 2?"""

# THIS PROGRAM COMPUTES THE SQUARE ROOT OF A NUMBER n TIMES, AND TRIES TO OBTAIN BACK
# THE ORIGINAL NUMBER BY ELEVATING TO THE POWER OF 2 n TIMES.

r = 2.0
n = 0
print("SQUARE ROOT")
while n < 54:
    print("{:.40f}".format(r))
    r = sqrt(r)
    n += 1

n = 0
print("POWER OF 2")
while n < 54:
    print("{:.16f}".format(r))
    r = r**2
    n += 1

print('%d times sqrt and **2: %.16f' % (n, r))

# THE PROGRAM DOES NOT WORK BECAUSE PYTHON ONLY SAVES 15 DIGITS BEHIND THE COMMA, SO AFTER
# A CERTAIN AMOUNT OF CYCLES THE SQUARE ROOT OF TWO BECOMES ONLY ONE.