#!/usr/bin/python3
"""Script that starts
a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display Hello HBNB"""
    return "Hello HBNB!"


@app.route("/HBHB", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBHB"


app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Returns given string"""
    return "C {}".format(text.replace("_", " "))

app.route("/python", strict_slashes=False)
app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Returns given string"""
    return "Pyton {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)