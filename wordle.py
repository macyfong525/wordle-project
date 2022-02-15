from nltk.corpus import words
import random


class Wordle():
    def __init__(self):
        def get_all_words():
            return [i for i in words.words() if len(i) == 5]

        self.result = get_all_words()

    def insert(self, input_word, pattern):
        assert len(input_word) == 5
        assert len(pattern) == 5

        def match_wordle(input_word, pattern, word):
            for i in range(5):
                if pattern[i] == 'g':
                    if input_word[i] != word[i]:
                        return False
                elif pattern[i] == 'y':
                    if (input_word[i] not in word) or (input_word[i] == word[i]):
                        return False
                elif pattern[i] == 'b':
                    if input_word.count(input_word[i]) > 1 and input_word[i] == word[i]:
                        return False
                    elif input_word.count(input_word[i]) == 1 and input_word[i] in word:
                        return False
            return True

        self.result = [word for word in self.result if match_wordle(input_word, pattern, word)]

    def get_suggested_words(self):
        return ','.join(self.result) if len(self.result) > 10 else ','.join(self.result)