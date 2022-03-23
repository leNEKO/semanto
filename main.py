#!/usr/bin/env python3
import click
from semanto.database import Database
from semanto.game import Game
from semanto.cli import Cli
from semanto.dictionary import Dictionary


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
