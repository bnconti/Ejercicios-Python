# Exercise 2.3: Work with a list

primes = [2, 3, 5, 7, 11, 13]

for number in primes:
    print("{} ".format(number), end="")

p = 17
primes.append(p)

print("".format())

for number in primes:
    print("{} ".format(number), end="")
