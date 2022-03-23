from gensim.models import KeyedVectors


class Database:
    '''Word similarity DB
    '''
    SIMILAR_TOPN = 1000

    def __init__(self, source_path: str):
        self._model = KeyedVectors.load_word2vec_format(
            source_path,
            binary=True,
            unicode_errors='ignore'
        )

    def word_is_avalaible(self, word):
        '''Check if the word is available
        '''

        return self._model.has_index_for(word)

    def get_similar(self, word: str) -> list:
        '''Get SIMILAR_TOPN words
        '''

        return self._model.most_similar(
            word,
            topn=self.SIMILAR_TOPN
        )

    def get_distance(self, target: str, current: str) -> float:
        '''Calculate distance between two words
        '''

        return self._model.similarity(target, current)
