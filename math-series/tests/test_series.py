# start off my importing the py test
import pytest 
# from this module, import this/these function(s)
from math_series.series import fibonacci, lucas, sum_series

# Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13]

def test_one_fib():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_two_fib():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_three_fib():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fourth_fib():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fifth_fib():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

# Lucas numbers [2, 1, 3, 4, 7, 11, 18, 29]

def test_one_luc():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_two_luc():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_three_luc():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_four_luc():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_five_luc():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_one_series():
    actual = sum_series(5)
    expected = 3
    assert actual == expected

def test_two_series():
    actual = sum_series(5, 2, 1)
    expected = 7
    assert actual == expected

# def test_two_series():
#     # optional values of 2, 1 align with the first two values of lucas numbers
#     actual = sum_series(req_param, 2, 1)
#     # where req_param is the value of the lucas sequence at that index
#     expected = numbers from lucas numbers

# def test_two_three():
#     actual = sum_series(req_param, anyting, anything)
#     expected = other series?