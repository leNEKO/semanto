from collections import OrderedDict
from .database import Database
from .dictionary import Dictionary


class Turn:
    def __init__(self, game, secret_word: str):
        self._game = game
        self._secret_word = secret_word

        self._scores = {}
        self._tries = 0
        self._top_words = None

        self._win = False

    def move(self, word: str):
        self._tries += 1

        if word == self._secret_word:
            score = 1
            progress = Database.SIMILAR_TOPN
            self._win = True
        else:
            score = self._game._database.get_distance(
                self._secret_word,
                word
            )
            progress = self.get_word_pos(word)

        item = {
            word: {
                'turn': self._tries,
                'score': score,
                'progress': progress,
            }
        }

        self._scores.update(item)

        return score

    def get_word_pos(self, search_word: str) -> int:
        for pos, word in enumerate(self.top_words):
            if word[0] == search_word:
                return pos

    @property
    def win(self):
        return self._win

    @property
    def secret_word(self):
        return self._secret_word

    @property
    def top_words(self) -> list:
        if self._top_words is None:
            self._top_words = self._game._database.get_similar(self._secret_word)
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
        return self._tries

class Game:
    def __init__(
        self,
        database: Database,
        dictionary: Dictionary,
    ):
        self._database = database
        self._dictionary = dictionary

    def new_turn(self, secret_word: str = None) -> Turn:
        return Turn(
            self,
            secret_word
            if secret_word is not None
            else self.get_next_available_random_word()
        )

    def get_next_available_random_word(self):
        '''Get next frequency dictionary word available in the database
        '''
        while next_random_word := self._dictionary.next_random_word:
            if self._database.word_is_avalaible(next_random_word):
                return next_random_word

