from .database import Database
class Game:
    def __init__(self, database: Database, secret_word: str):
        self._database = database
        self._scores = {}
        self._turn = 0
        self._secret_word = secret_word

    def move(self, word: str):
        self._turn += 1
        score = self._database.get_distance(
            self._secret_word,
            word
        )

        self._scores.update(
            {
                word: {
                    'turn': self._turn,
                    'score': score,
                }
            }
        )

    @property
    def history(self):
        # return self._scores
        return sorted(self._scores, key=lambda w: self._scores[w]['score'], reverse=True)