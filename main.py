#!/usr/bin/env python3
'''My semantle clone
'''
import click

from semanto.cli import Cli
from semanto.game import Game
from semanto.database import Database
from semanto.dictionary import Dictionary

def new_game():
    return Game(
        Database('data/source.bin'),
        Dictionary()
    )

@click.group()
def cli():
    pass

@cli.command()
def web_ui():
    '''Web UI with flask
    '''
    pass

@cli.command()
def cli_ui():
    '''Cli UI with click
    '''
    cli = Cli(
        new_game()
    )

    click.clear()
    cli.game_loop()


if __name__ == '__main__':
    cli()
