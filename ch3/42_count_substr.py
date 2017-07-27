# Exercise 3.42: Count substrings
# Author: Bruno N. Conti

"""
SAMPLE RUN:
Number of substrings 'ACG' on the DNA 'ACGTTACGGAACG': 3.
"""


def count_substrings(dna, pair):
    s = 0
    for x, y, z in zip(pair[0::1], pair[1::1], pair [2::1]):
        if x == dna[0] and y == dna[1] and z == dna[2]:
            s += 1
    return s

pair = "ACG"; dna = "ACGTTACGGAACG"
print("Number of substrings '{}' on the DNA '{}': {}.".format(pair, dna, count_substrings(pair, dna)))
