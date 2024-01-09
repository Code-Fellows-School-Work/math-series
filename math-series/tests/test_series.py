# start off my importing the py test
import pytest 
# from this module, import this/these function(s)
from math_series.series import fibonacci

# Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13]

def fib_test_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def fib_test_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def fib_test_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def fib_test_fourth():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def fib_test_fifth():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

# Lucas numbers [2, 1, 3, 4, 7, 11, 18, 29]

def luc_test_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def luc_test_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def luc_test_three():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def luc_test_four():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def luc_test_five():
    actual = lucas(4)
    expected = 7
    assert actual == expected

