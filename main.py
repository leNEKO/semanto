#!/usr/bin/env python3
import click
from tabulate import tabulate
from semantix.database import Database
from semantix.game import Game


def score_display(game: Game):
    PROGRESS_BAR_LENGTH = 64

    def format_progress(progress):
        if progress is None:
            progress = 0

        progress_ratio = PROGRESS_BAR_LENGTH / Database.TOPN
        progress_amount = int(progress * progress_ratio)

        return ''.join(
            (
                '|' * progress_amount,
                '.' * (PROGRESS_BAR_LENGTH - progress_amount),
            )
        )

    return tabulate(
        [
            (
                info['turn'],
                word,
                info['score'] * 100,
                format_progress(
                    info['progress']
                )
            )
            for word, info in game.scores.items()
        ],
        ('t', 'word', 'score', 'progress')
    )


def loop(database: Database, secret_word: str):
    game = Game(database, secret_word)

    while True:
        word = click.prompt('word', type=str)

        try:
            score = game.move(word)
            click.clear()

            click.echo(
                score_display(game)
            )
            if score == 1:
                click.echo()
                click.echo(f'💖 "{word}" found in {game.turn} turns')
                break
        except KeyError as e:
            click.echo(f'❓ "{word}" not found')

        click.echo()

@click.command()
@click.argument('secret_word')
def main(secret_word: str):
    click.clear()
    database = Database('data/source.bin')

    while True:
        loop(database, secret_word)
        click.echo()
        if click.confirm('New game?', default=True) is False:
            break
        click.clear()


if __name__ == '__main__':
    main()
