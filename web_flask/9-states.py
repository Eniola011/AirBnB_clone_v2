#!/usr/bin/python3
"""

Start: Flask Web App

"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    states = storage.all(State)
    if not id:
        dicty = {value.id: value.name for value in states.values()}
        return render_template('7-states_list.html',
                               Table="States",
                               items=dicty)
    s = "State.{}".format(id)
    if s in states:
        return render_template('9-states.html',
                               Table: 'State: {}'.format(states[s].name),
                               items=states[s])

    return render_template('9-states.html', items=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
