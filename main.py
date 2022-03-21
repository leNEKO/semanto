#!/usr/bin/env python3
import click
from pprint import pprint
from semantix.database import Database
from semantix.game import Game

@click.command()
@click.argument('secret_word')
def main(secret_word: str):
    database = Database('data/source.bin')
    game = Game(database, secret_word)
    while True:
        print(r'input:', end=' ')
        word = input().strip()
        try:
            game.move(word)
            click.echo(game.history)
        except KeyError as e:
            click.echo(f'{word} not found')

if __name__ == '__main__':
    main()