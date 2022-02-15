from nltk.corpus import words
import random


class Wordle():
    def __init__(self):
        def get_all_words():
            return [i for i in words.words() if len(i) == 5]

        self.result = get_all_words()

    def insert(self, word, pattern):
        assert len(word) == 5
        assert len(pattern) == 5

        word_list = [i for i in self.result]

        for s_word in word_list:
            for i in range(5):
                if pattern[i] == 'g':
                    if s_word[i] != word[i]:
                        self.result.remove(s_word)
                        break
                elif pattern[i] == 'y':
                    if word[i] not in s_word:
                        self.result.remove(s_word)
                        break
                    elif s_word[i] == word[i]:
                        self.result.remove(s_word)
                        break
                elif pattern[i] == 'b':
                    if word[i] in s_word:
                        self.result.remove(s_word)
                        break

    def get_suggested_words(self):
        return ','.join(random.sample(self.result, 10)) if len(self.result) > 10 else ','.join(self.result)
