from unittest import TestCase

from core import guess_index, GuessValueError


class TestGuessIndex(TestCase):

    def test_guess_index_len_1(self):
        expected = 0
        actual = guess_index([1])
        self.assertEqual(expected, actual)

    def test_guess_index_len_2(self):
        expected = 1
        actual = guess_index([1, 2])
        self.assertEqual(expected, actual)

    def test_guess_index_len_3(self):
        expected = 1
        actual = guess_index([1, 2, 3])
        self.assertEqual(expected, actual)

    def test_guess_index_len_4(self):
        expected = 2
        actual = guess_index([1, 2, 3, 4])
        self.assertEqual(expected, actual)

    def test_guess_index_len_5(self):
        expected = 2
        actual = guess_index([1, 2, 3, 4])
        self.assertEqual(expected, actual)

    def test_guess_index_none(self):
        with self.assertRaisesRegex(GuessValueError, "Search list is empty"):
            guess_index(None)

    def test_guess_index_empty_list(self):
        with self.assertRaisesRegex(GuessValueError, "Search list is empty"):
            guess_index([])
