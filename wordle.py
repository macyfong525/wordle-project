from collections import Counter
from itertools import chain

WORD_FILE = '5-letter-words.txt'
LETTER_NUMBER = 5


def get_all_words():
    return [line.rstrip() for line in open(WORD_FILE)]


class Wordle():
    def __init__(self):
        self.result = list(set(get_all_words()))

    def insert(self, input_word, pattern):
        assert len(input_word) == LETTER_NUMBER
        assert len(pattern) == LETTER_NUMBER
        input_word = input_word.upper()

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
        suggest_list = {}

        def letter_frequency(word_list):
            letter_counter = Counter(chain.from_iterable(word_list))
            return {char: cnt / sum(letter_counter.values()) for char, cnt in letter_counter.items()}
        try:
            total_char_score = letter_frequency(get_all_words())
            for word in self.result:
                score = sum(total_char_score[char] for char in word)
                suggest_list[word] = score
                suggest_words = sorted(suggest_list, key=suggest_list.get, reverse=True)[:10]
        except Exception as e:
            print(e)
            return suggest_list
        return suggest_words


if __name__ == '__main__':
    wordle = Wordle()
    a = 'raise'
    b = "yybbb"
    wordle.insert(a, b)
    result = wordle.get_suggested_words()
    print(result)
    a = 'aorta'
    b = "gyybg"
    wordle.insert(a, b)
    result = wordle.get_suggested_words()
    print(result)
