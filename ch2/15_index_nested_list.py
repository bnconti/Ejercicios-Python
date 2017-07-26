# Exercise 2.15: Index a nested list

"""
SAMPLE RUN:
a
['d', 'e', 'f']
h
d
abcdefgh
"""


q = [["a", "b", "c"], ["d", "e", "f"], ["g", "h"]]

# a) Index this list to extract:
# 1) the letter a
# 2) the list [’d’, ’e’, ’f’]
# 3) the last element h
# 4) the d element.

print(q[0][0])
print(q[1])
print(q[2][1])
print(q[1][0])

# Explain why q[-1][-2] has the value g.
# Because it is accessing the elements in reverse order.

for i in q:  # elements i are lists.
    for j in range(len(i)):  # elements j are integers.
        print(i[j], end='')

