# Exercise 2.25: Investigate a for loop over a changing list

"""
numbers = range(10)
print numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    i = len(numbers)/2
    del numbers[i]
    print ’n=%d, del %d’ % (n,i), numbers
...
n=0, del 5 [0, 1, 2, 3, 4, 6, 7, 8, 9]
n=1, del 4 [0, 1, 2, 3, 6, 7, 8, 9]
n=2, del 4 [0, 1, 2, 3, 7, 8, 9]
n=3, del 3 [0, 1, 2, 7, 8, 9]
n=8, del 3 [0, 1, 2, 8, 9]
"""

"""
The message in this exercise is to never modify a list that we are looping over.
Modification is indeed technically possible, as shown above, but you really need
to know what you are doing. Otherwise you will experience very strange pro-
gram behavior.
"""