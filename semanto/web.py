from flask import (
    Flask, jsonify,
    redirect, render_template,
    request, send_from_directory,
    __version__ as flask_version
)

from .game import Game

class Web:
    def __init__(self, game: Game):
        self._game = game

        self._app = Flask(__name__)