from flask import Flask
from flask import request
import sys

app = Flask(__name__)


@app.route("/hello/<name>")
def f(name):
    return "Hello %s!\n" % name


#@app.route("/")
#def foo():
#    return "This is test page."

@app.route("/", methods=['POST'])

#def print_request():
#    try:
#        mydata = request.json # will be 
#       return "Thanks. Your data is %s" % mydata
#       return 'JSON posted'
#   except:
#       return 'No Json Received'

def get_raw_request():
    # retrieve the incoming request data as string
    raw_request = request.data
    line = str(raw_request).replace("\n", " ")

    # 'a' mode to append to the existing Raw.txt
    with open('/srv/runme/groupa/Raw.txt', 'a+') as f:
        f.write(line+'\n')
    f.close()
    return "Json posted"


if __name__ == '__main__':
    #i = sys.argv.index('server:app')
    app.run('0.0.0.0', port=8080, debug = True)
