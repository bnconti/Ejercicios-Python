"""
Exercise 1.6: Compute the growth of money in a bank
Let p be a bank’s interest rate in percent per year. An initial amount A has then
grown to

A(1 + p/100)**n

after n years. Make a program for computing how much money 1000 euros have
grown to after three years with 5 percent interest rate.
Filename: interest_rate .
"""

A = 1000.0
n = 3
p = 5.0

growth = A*(1 + p/100)**n

print("""\
AFTER {:d} YEARS AND WITH AN INTEREST RATE OF {:.1f} PERCENT, THE INITIAL {:.1f}€ HAVE BECOME {:.1f}€. WOOOOOOOOOO.
""".format(n, p, A, growth))