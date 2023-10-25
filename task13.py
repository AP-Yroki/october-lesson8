from main import non_repeat
from unittest import TestCase

class TestNonRepeats(TestCase):
    def test_non_repeat1(self):
        N = 10
        start = 1
        end = 20
        result = non_repeat(N, start, end)
        self.assertEqual(len(result), N)
        for i in range(1, N):
            self.assertNotEqual(result[i], result[i - 1])

    def test_non_repeat2(self):
        N = 30
        start = 1
        end = 20
        result = non_repeat(N, start, end)
        self.assertEqual(result, "Невозможно создать список без повторяющихся чисел.")

    def test_non_repeat3(self):
        N = 20
        start = 1
        end = 20
        with self.assertRaises(ValueError):
            non_repeat(N, start, end)

    def test_non_repeat4(self):
        N = 5
        start = 1
        end = 100
        result = non_repeat(N, start, end)
        self.assertEqual(len(result), N)
        for i in range(1, N):
            self.assertNotEqual(result[i], result[i - 1])

    def test_non_repeat5(self):
        N = 5
        start = -10
        end = -5
        result = non_repeat(N, start, end)
        self.assertEqual(len(result), N)
        for i in range(1, N):
            self.assertNotEqual(result[i], result[i - 1])
