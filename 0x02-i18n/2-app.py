#!/usr/bin/env python3
"""
2-app: Flask web app
"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel


class Config:
    """ Babel configurations class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


@app.route('/', strict_slashes=False)
def welcome():
    """ Prints a welcome message
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """ Selects and returns the best matching locale
    """
    request.accept_languages.best_match(app.config['LANGUAGES'])
