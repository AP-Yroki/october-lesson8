from main import is_even
import pytest

def test_even1():
    assert is_even(10) == True

def test_even1():
    assert is_even('6') == "TypeError"

def test_even2():
    assert is_even(-9) == False

def test_even3():
    assert is_even('test') == "TypeError"

def test_even4():   
    assert is_even(4.0) == True

def test_even5():
    assert is_even(9.7) == False

