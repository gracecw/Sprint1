import os
from datetime import datetime
import sys

prefix = sys.argv[1]


def rotate(prefix):
    # get the original file
    origin = '/srv/runme/%s/Raw.txt' % (prefix)
    
    # get current time
    global t
    t = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    # get the name for renaming
    fname = '/srv/runme/%s/rawlog_%s.txt' % (prefix, t)
    
    # create lock file to avoid simultaneous accessing
    os.system('mkdir /srv/runme/%s/flock')
    
    # rename the raw file
    os.rename(origin, fname)
    
    # create new raw file
    with open(origin, 'w'):pass
    
    #remove the lock after the process is completed
    os.system('rm -f /srv/runme/%s/flock')
    return "Log rotated!"

#If Raw.txt is not empty, rotate it; call process2.py to process it.
if os.stat('/srv/runme/%s/Raw.txt' % (prefix)).st_size != 0:
    rotate(prefix)
    bashCommand = "python /home/testtest/Sprint1/Sprint2_v2/process2.py %s %s" % (t, prefix)
    os.system(bashCommand)
