import os
from datetime import datetime
import sys
import subprocess

prefix = sys.argv[1]


def rotate(prefix):
    # get the original file
    origin = '/srv/runme/%s/Raw.txt' % (prefix)
    # check if the dir exists
    if not os.path.exists('/srv/runme/%s' % (prefix)):
        os.system('mkdir /srv/runme/%s' % (prefix))
    # get current time
    global t
    t = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # get the name for renaming
    fname = '/srv/runme/%s/rawlog_%s.txt' % (prefix, t)
    # rename the file, also create lock file to avoid simultaneous accessing
    os.system('mkdir /srv/runme/%s/flock')
    os.rename(origin, fname)
    os.system('rm -f /srv/runme/%s/flock')

    # if not created by flask, create new
    if not os.path.exists(origin):
        with open(origin, 'w'):
            pass
    return "File rotated!"


if os.stat('/srv/runme/%s/Raw.txt' % (prefix)).st_size != 0:
    rotate(prefix)
    bashCommand = "python /home/testtest/Sprint1/process.py %s %s" % (t, prefix)
    os.system(bashCommand)
