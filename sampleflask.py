from flask import Flask
from flask import request
import sys
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

@app.route("/hello/<name>")
def f(name):
    return "Hello %s!\n" % name


@app.route("/")
def foo():
    return "This is test page."

@app.route("/request/", methods=['POST'])

def get_raw_request():
    # retrieve the incoming request data as string
    raw_request = request.data
    line = str(raw_request).replace("\n", " ")
    with open(/srv/runme/groupb/log.txt, 'a+') as f:
        f.write(line+'\n')
    f.close()
    return "Received"


if __name__ == '__main__':
    handler = TimedRotatingFileHandler('/srv/runme/groupb/log.txt', when='S', interval=30)
    #handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run('0.0.0.0', port=8080, debug = True)
