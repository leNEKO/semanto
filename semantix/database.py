from gensim.models import KeyedVectors


class Database:
    TOPN = 1000

    def __init__(self, source_path: str):
        self._model = KeyedVectors.load_word2vec_format(
            source_path,
            binary=True,
            unicode_errors='ignore'
        )

    def get_random(self):
        return self._model.get_normed_vectors()

    def get_similar(self, word: str) -> list:
        return self._model.most_similar(
            word,
            topn=self.TOPN
        )

    def get_distance(self, target: str, current: str) -> float:
        return self._model.similarity(target, current)
