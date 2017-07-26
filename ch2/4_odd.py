# Exercise 2.4: Generate odd numbers

"""Write a program that generates all odd numbers from 1 to n . Set n in the beginning
of the program and use a while loop to compute the numbers. (Make sure that if n
is an even number, the largest generated odd number is n-1 .)"""

n = 10000
i = 0


while i < n:
    i += 1
    if i%10 == 0:
        print("")
    if i%2 == 0:
        continue
    else:
        print("{:5d}, ".format(i), end="")
