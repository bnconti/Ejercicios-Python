# Exercise 1.6: Compute the growth of money in a bank

"""
SAMPLE RUN:
AFTER 3 YEARS AND WITH AN INTEREST RATE OF 5.0 PERCENT, THE INITIAL 1000.0€ HAVE BECOME 1157.6€. WOOOOOOOOOO.
"""

A = 1000.0
n = 3
p = 5.0

growth = A*(1 + p/100)**n

print("""\
AFTER {:d} YEARS AND WITH AN INTEREST RATE OF {:.1f} PERCENT, THE INITIAL {:.1f}€ HAVE BECOME {:.1f}€. WOOOOOOOOOO.
""".format(n, p, A, growth))
