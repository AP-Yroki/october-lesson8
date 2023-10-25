from main import sum_divider
from unittest import TestCase

class DivTest(TestCase):
    def test_divider1(self):
        self.assertEqual(sum_divider([1, 2, 3, 4, 5]), 0.25)
    def test_divider2(self):
        self.assertEqual(sum_divider([-1, -2, -3, 4, 5]), -0.5)
    def test_divider3(self):
        self.assertEqual(sum_divider(['-10', '-2', -3, 4, 5]), -2.0)
    def test_divider4(self):
        self.assertEqual(sum_divider(['hello']), 'ValueError')
    def test_divider5(self):
        self.assertEqual(sum_divider([15.5, 23.1, 12, 1]), 2.923076923076923)