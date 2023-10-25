from unittest import TestCase
from main import random_color

class TestRandomColor(TestCase):

    def test_random_color1(self):
        result = random_color()
        self.assertTrue(isinstance(result, str))
    def test_random_color2(self):
        colors = []
        result = random_color()
        self.assertEqual(result, 'IndexError')

#Больше не смог придумать