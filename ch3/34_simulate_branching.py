# Exercise 3.34: Test your understanding of branching
# Author: Bruno N. Conti
# Date: 7/26/17

"""
THIS PROGRAM WILL PRINT:
quadrant I or II
quadrant II
quadrant I or IV
quadrant I or II
quadrant I or IV
"""

def where1(x, y):
    if x > 0:
        print('quadrant I or IV')
    if y > 0:
        print('quadrant I or II')


def where2(x, y):
    if x > 0:
        print('quadrant I or IV')
    elif y > 0:
        print('quadrant II')

for x, y in (-1, 1), (1, 1):
    # x = -1, 1; y = 1, 1
    where1(x, y)
    where2(x, y)
