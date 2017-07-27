# Exercise 3.36: Rewrite a mathematical function
# Author: Bruno N. Conti
# Date: 7/27/17
# Run pytest 37_cos_sum.py for testing

"""
SAMPLE RUN:
Approximations to ln(x) by different methods.

  x  L3_ci(x)                  L3(x)
---  ------------------------  ------------------------
  1  (0.6931463282650033, 16)  (0.6931463282650033, 16)
  2  (1.0986111084058483, 27)  (1.0986111084058483, 27)
  3  (1.3862919617153997, 36)  (1.3862919617153997, 36)
  4  (1.6094344036517214, 45)  (1.6094344036517214, 45)
  5  (1.791755021194045, 54)   (1.791755021194045, 54)
  6  (1.9459049175432903, 63)  (1.9459049175432903, 63)
  7  (2.079435654960612, 72)   (2.079435654960612, 72)
  8  (2.197218138193527, 81)   (2.197218138193527, 81)
  9  (2.302577337140829, 89)   (2.302577337140829, 89)
 10  (2.397886256831465, 97)   (2.397886256831465, 97)
"""

from tabulate import tabulate


def L3_ci(x, epsilon=1E-6):
    i = 1
    ci = (1/i) * (x/(1+x))**i
    term = s = ci
    while abs(ci) > epsilon:
        cj = (1/i) * (x/(1+x))**i
        i += 1
        ci = (1/i) * (x/(1+x))**i
        a = ci / cj
        term = a*term
        s += term
    return s, i


def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i

print("Approximations to ln(x) by different methods.\n")
values = [(x, L3_ci(x), L3(x)) for x in range(1, 11)]
print(tabulate(values, headers=["x", "L3_ci(x)", "L3(x)"]))


def test_L3_ci():
    tol = 1E-10
    for x, y1, y2 in values:
        assert abs(y1[0]-y2[0]) < tol
