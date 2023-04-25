#!/usr/bin/python3
"""Return string when navigating to root dir"""
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Route /c/<text> returns C message"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisbest(text="is cool"):
    """Route /python/(<text>) returns Python message"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def isint(n):
    """Route /number/<n> returns int status message"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def inttemplate(n):
    """Route /number_template/<n> sends integer to template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd_int_template(n):
    """Route /number_odd_or_even/<n> sends odd-even int to template"""
    even = n % 2 == 0
    return render_template('6-number_odd_or_even.html', n=n, even=even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
