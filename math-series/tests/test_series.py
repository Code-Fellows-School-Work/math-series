# start off my importing the py test
import pytest 
# from this module, import this/these function(s)
from math_series.series import fibonacci

# Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected



