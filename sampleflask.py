from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/hello/<name>")
def f(name):
    return "Hello %s!\n" % name


@app.route("/")
def foo():
    return "This is test page."


@app.route("/request/", methods=['GET','POST'])
def print_request():
    try:
        mydata = request.json # will be 
        return "Thanks. Your data is %s" % mydata
        return 'JSON posted'
    except:
        return 'No Json Received'


app.run('0.0.0.0', port=8080, debug = True)