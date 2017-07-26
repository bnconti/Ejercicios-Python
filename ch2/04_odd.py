# Exercise 2.4: Generate odd numbers

"""
SAMPLE RUN:
    1,     3,     5,     7,     9,
   11,    13,    15,    17,    19,
   21,    23,    25,    27,    29,
   31,    33,    35,    37,    39,
   41,    43,    45,    47,    49,
"""

n = 50
i = 0

while i < n:
    i += 1
    if i%10 == 0:
        print("")
    if i%2 == 0:
        continue
    else:
        print("{:5d}, ".format(i), end="")
