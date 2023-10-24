from main import string_sum
import pytest

def test_str1():
    assert string_sum(['12', '32', '15']) == 59

def test_str2():
    assert string_sum(['-12', '32', '-15']) == 5

def test_str3():
    assert string_sum(['-12', 'test', '15']) == 'ValueError'

def test_str4():
    assert string_sum([12, '7', 4]) == 23

def test_str5():
    assert string_sum(4) == 'TypeError'


