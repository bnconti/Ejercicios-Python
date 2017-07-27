# Exercise 3.40: Find prime numbers
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Primes lower or equal to 80: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
"""


def erathosthenes(n):
    data = [i for i in range(2, n+1)]
    for i in data:
        for n in data[i-1:]:
            if n%i == 0:
                data.remove(n)
    return data

n = 80
print("Primes lower or equal to {}: {}".format(n, erathosthenes(n)))
