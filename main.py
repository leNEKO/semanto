#!/usr/bin/env python3
import click
from tabulate import tabulate
from semantix.database import Database
from semantix.game import Game

def score_display(game: Game):
    LENGTH = 64
    def format_progress(progress):
        if progress is None:
            progress = 0

        progress_amount = int(progress * (LENGTH / 1000))

        return ''.join(
            (
                '|' * progress_amount,
                '.' * (LENGTH - progress_amount),
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


@click.command()
@click.argument('secret_word')
def main(secret_word: str):
    click.clear()
    database = Database('data/source.bin')
    game = Game(database, secret_word)

    while True:
        click.echo()
        word = click.prompt('word', type=str)
        click.echo()
        try:
            click.clear()
            score = game.move(word)
            if score == 1:
                click.echo(f'{word} found 💖')
        except KeyError as e:
            click.echo(f'{word} not found ❓')
        click.echo(
            score_display(game)
        )



if __name__ == '__main__':
    main()
