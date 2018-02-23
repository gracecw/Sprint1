from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/hello/<name>")
def f(name):
    return "Hello %s!\n" % name


@app.route("/")
def foo():
    return "This is test page."


app.run('0.0.0.0', port=8080, debug = True)