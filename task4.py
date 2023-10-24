from main import arr_sum
import pytest

arr = [1, 2, 3, 4, 5]

def test_summ1():
    assert arr_sum([1, 2, 3, 4, 5]) == 15

def test_summ2():
    assert arr_sum([-1, -2, -3, -4, -5]) == -15

def test_summ3():
    assert arr_sum([]) == 0

def test_summ4():
    assert arr_sum([1.1, 2.2, 3.3, 4.4, 5.5]) == 16.5

def test_summ5():
    assert arr_sum([1, 2, 3, 4, 'test']) == 'TypeError'