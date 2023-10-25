from unittest import TestCase
from main import date_convert

class DateTest(TestCase):
    def test_date1(self):
        self.assertEqual(date_convert('2025-12-31'), ('31', '12', '2025'))
    def test_date2(self):
        self.assertEqual(date_convert('923'), ('923',))
    def test_date3(self):
        self.assertEqual(date_convert('923-14'), ('14', '923'))
    def test_date4(self):
        self.assertEqual(date_convert('test-october'), ('october', 'test'))
    def test_date5(self):
        self.assertEqual(date_convert(2023-13-5), ('AttributeError'))