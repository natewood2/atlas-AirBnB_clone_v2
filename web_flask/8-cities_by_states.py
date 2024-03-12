#!/usr/bin/python3
""" Will help display on the front end. """
from models.__init__ import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states_list():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
