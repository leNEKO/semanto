#!/usr/bin/env python3
import click
from semantix.database import Database
from semantix.game import Game
from semantix.cli import Cli
from semantix.dictionary import Dictionary


@click.command()
def main():
    cli = Cli(
        Database('data/source.bin'),
        Dictionary()
    )

    click.clear()
    cli.main_loop()


if __name__ == '__main__':
    main()
