# Exercise 2.18: Values of boolean expressions

C = 41
C == 40                     # NOPE
C != 40 and C < 41          # NOPE
C != 40 or C < 41           # YEP
not C == 40                 # YEP
not C > 40                  # YEP
C <= 41                     # YEP
not False                   # YEP
True and False              # NOPE
False or True               # YEP
False or False or False     # NOPE
True and True and False     # NOPE
False == 0                  # YEP
True == 0                   # NOPE
True == 1                   # YEP