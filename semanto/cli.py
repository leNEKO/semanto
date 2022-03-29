import click
from tabulate import tabulate

from .database import Database
from .game import Game, Turn


class Cli:
    '''Cli game client
    '''
    PROGRESS_BAR_LENGTH = 64
    CHEAT_CODE = '???'

    def __init__(
        self,
        game: Game
    ):
        self._game = game

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

    def _score_display(self, part: Turn):
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

                for word, info in part.scores.items()
            ],
            ('t', 'word', 'score', 'progress')
        )

    def game_loop(self):
        '''Main loop
        '''
        while True:
            self.part_loop(
                self._game.new_turn()
            )
            click.echo()

            if click.confirm('New game?', default=True) is False:
                break
            click.clear()

    def part_loop(self, part: Turn):
        '''Game round loop
        '''

        while True:
            word = click.prompt('word', type=str)

            if word == self.CHEAT_CODE:
                click.echo(f'👹 it was "{part.secret_word}"')

                break

            try:
                score = part.move(word)
                click.clear()

                click.echo(
                    self._score_display(part)
                )

                if score == 1:
                    click.echo()
                    click.echo(f'💖 "{word}" found in {part._game.turn} turns')

                    break
            except KeyError:
                click.echo(f'❓ "{word}" not found')

            click.echo()
