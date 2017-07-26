# Exercise 3.20: Write functions

"""
SAMPLE RUN:
Hello, World!
Hello, World!
Hello, World!
Python function
"""


def hw1():
    return "Hello, World!"


def hw2():
    print("Hello, World!")


def hw3(a, b):
    return str(a + b)


print(hw1())
hw2()
print(hw3('Hello, ', 'World!'))
print(hw3('Python ', 'function'))
