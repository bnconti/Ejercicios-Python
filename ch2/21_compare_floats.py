# Exercise 2.21: Compare two real numbers with a tolerance

# if a != b:
#     print("Wrong result!")

a = 1/947.0*947
b = 1
tol = 1e-15

if abs(a-b) < tol:
    print("{:.40f}".format(abs(a - b)))
    print("{:.40f}".format(tol))
    print("Seems OK to me!")

print("END")