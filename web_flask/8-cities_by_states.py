#!/usr/bin/python3
"""

Start: Flask Web App

"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
