#!/usr/bin/env python3
'''My semantle clone
'''
import click

from semanto.cli import Cli
from semanto.database import Database
from semanto.dictionary import Dictionary


@click.command()
def main():
    '''Main cli game loop
    '''
    cli = Cli(
        Database('data/source.bin'),
        Dictionary()
    )

    click.clear()
    cli.main_loop()


if __name__ == '__main__':
    main()
