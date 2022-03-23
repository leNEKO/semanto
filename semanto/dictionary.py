from random import shuffle
from wordfreq import top_n_list


class Dictionary:
    DICTIONARY_SIZE = 40_000

    def __init__(self):
        self._word_list = top_n_list('fr', self.DICTIONARY_SIZE)
        shuffle(self._word_list)

    @property
    def next_word(self):
        return self._word_list.pop()