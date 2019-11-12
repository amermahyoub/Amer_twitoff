"""Minimal flask app"""

from flask import Flask

# Mak the application
app = Flask(__name__)

# make the route
@app.route("/")

# define a function
def hello():
    return "Hello beautiful worls!"

# creating second route
@app.route("/about")

def preds():
    return "This is my about page!"
