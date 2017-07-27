# Exercise 3.35: Simulate nested loops by hand
# Author: Bruno N. Conti
# Date: 7/26/17

n = 3

# This for will print: -1, 1, 2
for i in range(-1, n):
    if i != 0:
        print(i)

print("{}".format("-"*40))
# This for will print: (1, 0), (1, 1), (1, 2), (7, 0), (7, 1), (7, 1)
for i in range(1, 13, 2*n):
    for j in range(n):
        print(i, j)


print("{}".format("-" * 40))
# This for will print: (2, 1), (3, 1), (3, 2)
for i in range(1, n+1):
    for j in range(i):
        if j:
            print(i, j)


print("{}".format("-" * 40))
# This for will print: (7, 4, 2), (7, 4, 3), (7, 6, 2), (7, 6, 3), (7, 6, 4), (7, 6, 5)
for i in range(1, 13, 2*n):
    for j in range(0, i, 2):
        for k in range(2, j, 1):
            b = i > j > k
            if b:
                print(i, j, k)
