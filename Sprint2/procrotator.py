#This function will rotate the Proc.txt file in the given 'prefix' folder, name the log file after the timestamp it is rotated.

import os
from datetime import datetime
import sys
import time

prefix = sys.argv[1]


def rotate(prefix):
    # get the original file
    origin = '/srv/runme/%s/Proc.txt' % (prefix)
    
    # get current time
    global t
    t = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    # get the name for renaming
    fname = '/srv/runme/%s/proc_log_%s.txt' % (prefix, t)
    
    # create lock file to avoid simultaneous accessing
    os.system('mkdir /srv/runme/%s/flock_proc')
    
    # rename the raw file
    os.rename(origin, fname)
    
    # create new raw file
    with open(origin, 'w'):pass
    
    #remove the lock after the process is completed
    os.system('rm -f /srv/runme/%s/flock_proc')
    return "Proc Log rotated!"

#If Proc.txt exists and is not empty, rotate it
time.sleep(15)
if (os.path.exists('/srv/runme/%s/Proc.txt' % (prefix))) and (os.stat('/srv/runme/%s/Proc.txt' % (prefix)).st_size != 0):
    rotate(prefix)
