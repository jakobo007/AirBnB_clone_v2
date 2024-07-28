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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)