#!/usr/bin/env python3
"""
1-app: Flask web app
"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel


class Config:
    """ Babel configurations class
    """
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app, default_locale='en', default_timezone='UTC')


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
