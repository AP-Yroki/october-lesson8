from unittest import TestCase
from main import get_divisors

class Test_ListDividers(TestCase):
    def test_dividers_positive_number(self):
        numbers = [12]
        result = get_divisors(numbers)
        self.assertEqual(result, [[1, 2, 3, 4, 6, 12]])

    def test_dividers_zero(self):
        numbers = [0]
        result = get_divisors(numbers)
        self.assertEqual(result, [[]])

    def test_dividers_negative_number(self):
        numbers = [-8]
        result = get_divisors(numbers)
        self.assertEqual(result, [[]])

    def test_dividers_prime_number(self):
        numbers = [7]
        result = get_divisors(numbers)
        self.assertEqual(result, [[1, 7]])

    def test_dividers_mixed_numbers(self):
        numbers = [10, 6, 15]
        result = get_divisors(numbers)
        self.assertEqual(result, [[1, 2, 5, 10], [1, 2, 3, 6], [1, 3, 5, 15]])
