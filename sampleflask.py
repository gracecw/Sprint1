from flask import Flask
from flask import request
import sys
import logging
from logging.handlers import TimedRotatingFileHandler


app = Flask(__name__)
app.logger.setLevel(logging.NOTSET)

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
    app.logger.info('line')
    return "Received"


if __name__ == '__main__':
    handler = TimedRotatingFileHandler('/srv/runme/groupb/log.txt', when='S', interval=10)
    handler.setLevel(logging.NOTSET)
    app.logger.addHandler(handler)
    app.run('0.0.0.0', port=8080, debug = True)
