#!/usr/bin/python3
"""

Start: Flask Web App

"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
def display_python(text):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
