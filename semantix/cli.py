from tabulate import tabulate
from .database import Database
from .dictionary import Dictionary
from .game import Game

import click


class Cli:
    PROGRESS_BAR_LENGTH = 64

    def __init__(self, database: Database, dictionary: Dictionary):
        self._database = database
        self._dictionary = dictionary

    def _format_progress(self, progress):
        if progress is None:
            progress = 0

        progress_ratio = self.PROGRESS_BAR_LENGTH / Database.SIMILAR_TOPN
        progress_amount = int(progress * progress_ratio)

        return ''.join(
            (
                '|' * progress_amount,
                '.' * (self.PROGRESS_BAR_LENGTH - progress_amount),
            )
        )

    def _score_display(self):
        return tabulate(
            [
                (
                    info['turn'],
                    word,
                    '{:.2f}'.format(
                        info['score'] * 100
                    ),
                    self._format_progress(
                        info['progress']
                    )
                )
                for word, info in self._game.scores.items()
            ],
            ('t', 'word', 'score', 'progress')
        )

    def get_next_available_word(self):
        while next_word := self._dictionary.next_word:
            if self._database.word_is_avalaible(next_word):
                return next_word

    def main_loop(self):
        while True:
            self._game = Game(
                self._database,
                self.get_next_available_word()
            )
            self.game_loop()
            click.echo()
            if click.confirm('New game?', default=True) is False:
                break
            click.clear()

    def game_loop(self):
        while True:
            word = click.prompt('word', type=str)

            try:
                score = self._game.move(word)
                click.clear()

                click.echo(
                    self._score_display()
                )
                if score == 1:
                    click.echo()
                    click.echo(f'💖 "{word}" found in {self._game.turn} turns')
                    break
            except KeyError as e:
                click.echo(f'❓ "{word}" not found')

            click.echo()
