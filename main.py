#!/usr/bin/env python3
import click
from semantix.database import Database
from semantix.game import Game
from semantix.cli import Cli


@click.command()
@click.argument('secret_word')
def main(secret_word: str):
    click.clear()
    database = Database('data/source.bin')
    cli = Cli(database, secret_word)

    cli.main_loop()


if __name__ == '__main__':
    main()
