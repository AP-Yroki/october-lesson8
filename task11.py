from unittest import TestCase
from main import max_min

class TestMaxMinFunction(TestCase):
    def test_max_min1(self):
        lst = [4, 1, 2, 4, 2, 6]
        result = max_min(lst)
        self.assertEqual(result, 'max: 6\nmin: 1')

    def test_max_min2(self):
        lst = [-5, -2, -8, -1]
        result = max_min(lst)
        self.assertEqual(result, 'max: -1\nmin: -8')

    def test_max_min3(self):
        lst = [10, -3, 5, 2, -7, 1]
        result = max_min(lst)
        self.assertEqual(result, 'max: 10\nmin: -7')

    def test_max_min4(self):
        lst = []
        result = max_min(lst)
        self.assertEqual(result, 'ValueError')

    def test_max_min5(self):
        lst = [7]
        result = max_min(lst)
        self.assertEqual(result, 'max: 7\nmin: 7')

