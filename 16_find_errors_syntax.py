# Exercise 1.16: Find errors in Python statements

# 1a = 2 #  The name of a variable can't start with a number!
# a1 = b # b needs to be defined before doing that.
# x = 2 #  O.K.
# y = X + 4 # is it 6? Nope! X is not x.
# from Math import tan # The module is called math, not Math.
# print tan(pi) # pi needs to be imported from math before using it.
# pi = "3.14159’ #  pi is being defined as a string, not as a number.
# print tan(pi) #  pi needs to be a number for that to work.
# c = 4**3**2**3 #  O.K.
# _ = ((c-78564)/c + 32)) # The name of a variable needs to start with a letter.
# discount = 12% #  It should be 0.12
# AMOUNT = 120.- # ??
# amount = 120$ # U cant put $ in there.
# address = hpl@simula.no # U need to add "" if this it a string.
# and = duck # and is a reserverd word of Python, can't use it.
# class = ’INF1100, gr 2" #  Uh...
# continue_ = x > 0 #  I think this would be True (boolean).
# rev = fox = True #  Seems OK.
# Norwegian = [’a human language’] # That is not a string, at least in Python 3.
# true = fox is rev in Norwegian #  ???