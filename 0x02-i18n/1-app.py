#!/usr/bin/env python3
"""
1-app: Flask web app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Babel configurations class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app, default_locale='en', default_timezone='UTC')


@app.route('/', strict_slashes=False)
def welcome():
    """ Prints a welcome message
    """
    return render_template('1-index.html')
