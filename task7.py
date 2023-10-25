from main import string_sum
from unittest import TestCase

class SumTest(TestCase):
    def test_summ1(self):
        self.assertEqual(string_sum(['1', '2', '3', '4', '5']), 15)
    def test_summ2(self):
        self.assertEqual(string_sum([134]), 134)
    def test_summ3(self):
        self.assertEqual(string_sum([1.5, 6.7, 15.2]), 22)
    def test_summ4(self):
        self.assertEqual(string_sum([4, '7', '10']), 21)
    def test_summ5(self):
        self.assertEqual(string_sum('test'), 'ValueError')