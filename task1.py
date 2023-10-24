from main import num
import pytest


def test_num_1():
    assert num(10) == "no"


def test_num_2():
    assert num(-1) == "yes"


def test_num_3():
    assert num("gfdgfd") == "ValueError"


def test_num_4():
    assert num(3.14) == "no"

def test_num_5():
    assert num(-3.14) == "yes"

