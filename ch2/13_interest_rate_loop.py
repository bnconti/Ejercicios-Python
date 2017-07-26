# Exercise 2.13: Simulate a program by hand

"""
SAMPLE RUN:
8
"""

initial_amount = 100
p = 5.5 # interest rate
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
    amount += p/100*amount
    years += 1
print(years)

# This program tell us how much years are needed to increase the initial amount by 50%
# with an interest rate of 5.5% per year.
