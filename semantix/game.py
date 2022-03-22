from collections import OrderedDict
from .database import Database


class Game:
    def __init__(self, database: Database, secret_word: str):
        self._database = database
        self._scores = {}
        self._turn = 0
        self._secret_word = secret_word
        self._top_words = None

    def move(self, word: str):
        self._turn += 1
        score = self._database.get_distance(
            self._secret_word,
            word
        )
        progress = self.get_word_pos(word)

        item = {
            word: {
                'turn': self._turn,
                'score': score,
                'progress': progress
            }
        }

        self._scores.update(item)

        return (
            1
            if word == self._secret_word
            else score
        )

    def get_word_pos(self, search_word: str) -> int:
        for pos, word in enumerate(self.top_words):
            if word[0] == search_word:
                return pos

    @property
    def top_words(self) -> list:
        if self._top_words is None:
            self._top_words = self._database.get_similar(self._secret_word)
        return reversed(self._top_words)

    @property
    def scores(self) -> OrderedDict:
        return OrderedDict(
            sorted(
                self._scores.items(),
                key=lambda x: x[1]['score'],
            )
        )

    @property
    def progress(self) -> int:
        max_progress = 0

        for info in self.scores.values():
            progress = info['progress']
            if (
                progress is not None
                and progress > max_progress
            ):
                max_progress = progress

        return

    @property
    def turn(self):
        return self._turn