from main import count_digit
import pytest

def test_count1():
    assert count_digit(10) == 2

def test_count2():
    assert count_digit(-30) == 2

def test_count3():
    assert count_digit(5.2) == 1

def test_count4():
    assert count_digit("test") == 'ValueError'

def test_count5():
    assert count_digit(['123']) == 'TypeError'

