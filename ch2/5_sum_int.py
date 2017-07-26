"""
Exercise 2.5: Compute the sum of the first n integers

Write a program that computes the sum of the integers from 1 up to and including
n. Compare the result with the famous formula n(n+1)/2.
"""

n = 9999
total = 0
i = 1

while i <= n:
    total += i
    i += 1

formula = (n*(n+1))/2

print("SUM: {:10d}".format(total))
print("FRM: {:10.0f}".format(formula))

print("END.")
