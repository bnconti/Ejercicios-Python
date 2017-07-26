# Exercise 2.20: Explore what zero can be on a computer

eps = 1.0                           # DEFINES eps AS EQUAL TO 1.0
while 1.0 != 1.0 + eps:             # RUNS THIS PROGRAM WHILE 1.0 != 1.0 + eps
    print("...............", eps)   # PRINTS THE ACTUAL eps VALUE
    eps = eps/2.0                   # DIVIDES eps BY TWO
print("final eps:", eps)            # PRINTS THE FINAL eps, SUCH THAT 1.0 == 1.0 + eps

"""
Explain with words what the code is doing, line by line. Then examine the output.
How can it be that the “equation” 1 != 1 + eps is not true? Or in other words, that
a number of approximately size 10**-16 (the final eps value when the loop terminates)
gives the same result as if eps were zero?
"""

# BECAUSE A COMPUTER HAS FINITE MEMORY SPACE TO WORK WITH, SO THE VARIABLE eps
# EVENTUALLY REACHES A POINT WERE THE NUMBER IS SO LITTLE THAT IT CAN'T BE
# REPRESENTED CORRECTLY, SO IT BECOMES ZERO AND DOES NOT AFFECT THE SUM (1.0 = 1.0 + 0).

