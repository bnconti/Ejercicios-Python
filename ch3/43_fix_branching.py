# Exercise 3.43: Resolve a problem with a function
# Author: Bruno N. Conti


"""
>>> def f(x):
...     if 0 <= x <= 2:
...         return x**2
...     elif 2 < x <= 4:
...         return 4
...     elif x < 0:
...         return 0
...
>>> f(2)
4
>>> f(5)
>>> f(10)
"""

# Why do we not get any output when calling f(5) and f(10) ?
# Because the case x > 4 is not contemplated in the function
# It only gives an answer for values of x <= 4
