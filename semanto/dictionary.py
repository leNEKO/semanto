'''Most frequent word dictionary
'''
from random import shuffle

from wordfreq import top_n_list


class Dictionary:
    '''Frequent word dictionnary
    '''
    DICTIONARY_SIZE = 2_048

    def __init__(self):
        self._word_list = [
            word
            for word in top_n_list(
                'fr',
                self.DICTIONARY_SIZE
            )
            if len(word) >= 4
        ]
        shuffle(self._word_list)

    @property
    def next_word(self):
        '''Get next random word
        '''

        return self._word_list.pop()
