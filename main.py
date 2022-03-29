#!/usr/bin/env python3
'''My semantle clone
'''
import click

from semanto.cli import Cli
from semanto.web import Web
from semanto.game import Game
from semanto.database import Database
from semanto.dictionary import Dictionary

DEFAULT_DATA_SOURCE = 'data/source.bin'

def new_game():
    return Game(
        Database(DEFAULT_DATA_SOURCE),
        Dictionary()
    )

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = new_game()


@cli.command()
@click.pass_obj
def web_ui(game: Game):
    '''Web UI with flask
    '''
    web = Web(game)

@cli.command()
@click.pass_obj
def cli_ui(game: Game):
    '''Cli UI with click
    '''
    cli = Cli(game)
    click.clear()
    cli.game_loop()


if __name__ == '__main__':
    cli()
