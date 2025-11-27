# test_algorithms.py
import pytest
from lw_8 import Algorithms

# 1) min_positive
def test_min_positive_ok():
    assert Algorithms.min_positive([5, 2, 9]) == 2

def test_min_positive_bad():
    with pytest.raises(ValueError):
        Algorithms.min_positive([5, 0, 2])

# 2) sum_negative_only
def test_sum_negative_only_ok():
    assert Algorithms.sum_negative_only([-1, -2, -3]) == -6

def test_sum_negative_only_bad():
    with pytest.raises(ValueError):
        Algorithms.sum_negative_only([-1, 2, -3])

# 3) fibonacci_n
def test_fibonacci_ok():
    assert Algorithms.fibonacci_n(7) == 13

def test_fibonacci_bad():
    with pytest.raises(ValueError):
        Algorithms.fibonacci_n(-5)

# 4) current
def test_current_ok():
    assert Algorithms.current(10, 2) == 5

def test_current_bad():
    with pytest.raises(ValueError):
        Algorithms.current(10, 0)