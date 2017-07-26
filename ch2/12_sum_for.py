# Exercise 2.12: Replace a while loop by a for loop

"""
SAMPLE RUN:
2.083
"""

s = 0; M = 5

for k in range(1, M):
    s += 1/k
print("{:.3f}".format(s))
