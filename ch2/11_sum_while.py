# Exercise 2.11: Compute a mathematical sum

s = 0; k = 1; M = 5
while k < M:
    s += 1/k
    k += 1  # This was missing in the original program.
print("{:.3f}".format(s))