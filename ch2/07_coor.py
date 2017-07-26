# Exercise 2.7: Generate equally spaced coordinates

"""
SAMPLE RUN:
20 interval of length 0.05. Range [0;1].
0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00
"""

a = 0; b = 1; n = 20; h = (b-a)/n

coord_list_alternative = [a+i*h for i in range(0, n+1)]
print("{} interval of length {:.2f}. Range [{};{}].".format(n, h, a, b))
for x in coord_list_alternative:
    print("{:4.2f} ".format(x), end='')
