#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 4.15: Write a function given its test function
# Author: Bruno N. Conti


from itertools import zip_longest


def halve(x):
    if type(x) is float:
        y = x/2
    elif type(x) is int:
        y = x//2
    else:
        raise ValueError("Invalid input.")
    return y


def test_halve():
    assert halve(5.0) == 2.5    # Real number division
    assert halve(5) == 2        # Integer division


def add(a, b):
    try:
        return a+b
    except:
        raise ValueError("Invalid input.")


def test_add():
    # Test integers
    assert add(1, 2) == 3
    # Test floating-point numbers with rounding error
    tol = 1E-14
    a = 0.1; b = 0.2
    computed = add(a, b)
    expected = 0.3
    assert abs(expected - computed) < tol
    # Test lists
    assert add([1,4], [4,7]) == [1,4,4,7]
    # Test strings
    assert add("Hello, ", "World!") == "Hello, World!"


def equal(a, b):
    if a == b:
        same = True
        difference = a
    else:
        same = False
        difference = ''
        for letter_a, letter_b in zip_longest(a, b):
            if letter_a == letter_b:
                difference += letter_a
            elif letter_a is None:
                difference += '*' + '|' + letter_b
            elif letter_b is None:
                difference += letter_a + '|' + '*'
            elif letter_a != letter_b:
                difference += letter_a + '|' + letter_b
    return same, difference


def test_equal():
    assert equal("abc", "abc") == (True, "abc")
    assert equal("abc", "aBc") == (False, "ab|Bc")
    assert equal("abc", "aBcd") == (False, "ab|Bc*|d")
    assert equal("Hello, World!", "hello world") == \
        (False, "H|hello,|  |wW|oo|rr|ll|dd|*!|*")

test_halve()
test_add()
test_equal()
