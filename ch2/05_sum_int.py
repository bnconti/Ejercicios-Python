# Exercise 2.5: Compute the sum of the first n integers

"""
SAMPLE RUN:
SUM:   49995000
FRM:   49995000
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
