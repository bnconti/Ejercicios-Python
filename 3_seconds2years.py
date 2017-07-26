"""
Exercise 1.3: Derive and compute a formula
Can a newborn baby in Norway expect to live for one billion (10 9 ) seconds? Write
a Python program for doing arithmetics to answer the question.
Filename: seconds2years.
"""

seconds = 10**9

years = ((((seconds/60)/60)/24)/365)

print ("Norwegian baby's life expectative: {:.0f} years.".format(years))

# El tiempo será de aproximadamente 32 años,
# el pibe noruego seguramente viva ese tiempo.