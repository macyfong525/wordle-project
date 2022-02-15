import unittest
from wordle import Wordle


class MyTestCase(unittest.TestCase):
    def test_wordle(self):
        wordle = Wordle()
        a = 'ridgy'
        b = "gybbb"
        wordle.insert(a, b)
        a = 'rubin'
        b = "gbggg"
        wordle.insert(a, b)
        final_word = wordle.get_suggested_words()
        self.assertEqual(final_word, 'robin')  # add assertion here


if __name__ == '__main__':
    unittest.main()
