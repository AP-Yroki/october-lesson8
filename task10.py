from main import dct_sum
from unittest import TestCase

class TestDctSum(TestCase):
    def test_sum_of_positive_values(self):
        dct = {
            1: {1: 11, 2: 12, 3: 13},
            2: {1: 21, 2: 22, 3: 23},
            3: {1: 24, 2: 25, 3: 26},
        }
        self.assertEqual(dct_sum(dct), 177)

    def test_sum_of_negative_values(self):
        dct = {
            1: {1: -11, 2: -12, 3: -13},
            2: {1: -21, 2: -22, 3: -23},
            3: {1: -24, 2: -25, 3: -26},
        }
        self.assertEqual(dct_sum(dct), -177)

    def test_empty_dictionary(self):
        dct = {}
        self.assertEqual(dct_sum(dct), 0)

    def test_mixed_values(self):
        dct = {
            1: {1: 10, 2: -5, 3: 15},
            2: {1: 7, 2: 20, 3: -3},
        }
        self.assertEqual(dct_sum(dct), 44)

    def test_float_values(self):
        dct = {
            1: {1: 1.5, 2: 2.5},
            2: {1: 3.2, 2: 4.3},
        }
        self.assertEqual(dct_sum(dct), 11.5)