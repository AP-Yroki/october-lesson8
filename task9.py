from unittest import TestCase
from main import dct_join


class TestDctJoin(TestCase):
	def test_dct_join(self):
		dict1 = {'a': 1, 'b': 2}
		dict2 = {'c': 3, 'd': 4}
		correct_answer = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
		self.assertEqual(dct_join(dict1, dict2), correct_answer)

	def test_merge_dicts_2(self):
		dict1 = {'x': 10, 'y': 20}
		dict2 = {'z': 30, 'w': 40}
		correct_answer = {'x': 10, 'y': 20, 'z': 30, 'w': 40}
		self.assertEqual(dct_join(dict1, dict2), correct_answer)

	def test_merge_dicts_3(self):
		dict1 = {'name': 'Oleg'}
		dict2 = {'age': 30, 'city': 'Kazan'}
		correct_answer = {'name': 'Oleg', 'age': 30, 'city': 'Kazan'}
		self.assertEqual(dct_join(dict1, dict2), correct_answer)

	def test_merge_dicts_4(self):
		dict1 = {}
		dict2 = {'a': 1, 'b': 2}
		correct_answer = {'a': 1, 'b': 2}
		self.assertEqual(dct_join(dict1, dict2), correct_answer)

	def test_merge_dicts_5(self):
		dict1 = {'one': 1, 'two': 2}
		dict2 = {}
		correct_answer = {'one': 1, 'two': 2}
		self.assertEqual(dct_join(dict1, dict2), correct_answer)



