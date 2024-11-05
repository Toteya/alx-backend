#!/usr/bin/env python3
"""
1-app: Flask web app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app, locale_selector='en', timezone_selector='UTC')

class Config:
    """ Babel configurations class
    """
    LANGUAGES = ['en', 'fr']

@app.route('/', strict_slashes=False)
def welcome():
    """ Prints a welcome message
    """
    return render_template('1-index.html')
