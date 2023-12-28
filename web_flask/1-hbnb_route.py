#!/usr/bin/python3
"""

Start: Flask Web App

"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_one():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_two():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
