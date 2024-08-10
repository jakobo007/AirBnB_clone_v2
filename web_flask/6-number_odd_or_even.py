#!/usr/bin/python3
"""Script that starts
a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display Hello HBNB"""
    return ("Hello HBNB!")
 

@app.route("/HBHB", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return ("HBHB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Returns given string"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display a number"""
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays a HTML page if n=int"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_odd_or_even(n):
    """Display page if n=int and is odd/even"""
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)