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
    mydata = request.json
    if mydata != None:
        dataDir = '/srv/runme/groupa/'
        f = open(dataDir+'Raw.txt', 'w')
        f.write(mydata)
        f.close()
        return 'JSON posted'
    
    else:
        return 'No Json Received.'


app.run('0.0.0.0', port=8080, debug = True)

