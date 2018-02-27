## Lauch a server listening at port 8080, taking POST request and save raw request in Raw.txt.

import sys
from flask import Flask, request
import os
import time

dataDir = '/srv/runme/'
prefix = sys.argv[1]

app = Flask(__name__)

# make prefix dir if it does not exist
if not os.path.exists(dataDir + prefix):
    print("%s does not exists, creating now" % (prefix))
    os.system('mkdir %s' % (dataDir + prefix))


@app.route('/', methods=['POST'])
def get_raw_request():
    
    # check for lock file
    while True:
        if not os.path.exists(dataDir + prefix + "/flock"):
            break
        print "Sorry, the server is busy now..."
        time.sleep(0.001)
    
    # retrieve the incoming request data as string
    raw_request = request.data
    line = str(raw_request).replace("\n", " ")
    
    # 'a' mode to append to the existing Raw.txt
    with open(dataDir + prefix + '/Raw.txt', 'a+') as f:
        f.write(line + '\n')
    f.close()
    
    return "Received"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
