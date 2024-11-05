#!/usr/bin/env python3
"""
0-app: Flask web app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """ Prints a welcome message
    """
    return render_template('0-index.html')
