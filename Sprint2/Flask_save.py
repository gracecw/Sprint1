import sys
from flask import Flask, request
import os

dataDir = '/srv/runme/'
prefix = sys.argv[1]

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_raw_request():
    # retrieve the incoming request data as string
    raw_request = request.data
    line = str(raw_request).replace("\n", " ")

    if not os.path.exists(dataDir + prefix):
        os.system('mkdir %s' % (dataDir + prefix)) 
    # 'a' mode to append to the existing Raw.txt
    with open(dataDir + prefix + '/Raw.txt', 'a+') as f:
        f.write(line + '\n')
    f.close()
    return "Received"


app.run(host='0.0.0.0', port=8080)
