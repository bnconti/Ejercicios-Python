# Exercise 3.41: Find pairs of characters
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Number of pairs 'AT' on the DNA 'ACTGCTATCCATT': 2.
"""


def count_pairs(dna, pair):
    s = 0
    for x, y in zip(pair[0::1], pair[1::1]):
        if x == dna[0] and y == dna[1]:
            s += 1
    return s

pair = "AT"; dna = "ACTGCTATCCATT"
print("Number of pairs '{}' on the DNA '{}': {}.".format(pair, dna, count_pairs(pair, dna)))
