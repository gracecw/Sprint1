import time
import os
from datetime import datetime
import sys

prefix =  sys.argv[1]

def rotate(prefix):
    #get the original file
    origin = '/srv/runme/%s/Raw.txt' %(prefix)

    #get current time
    t =datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    #get the name for renaming
    fname ='/srv/runme/%s/rawlog_%s.txt'%(prefix, t)


    #rename the file
    os.rename(origin, fname)

    #if not created by flask, create new
    if not os.path.exists(origin):
        with open(origin, 'w'): pass
    
    return "File rotated!"

rotate()