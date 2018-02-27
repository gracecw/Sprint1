import os, json, sys
import time

timestamp = sys.argv[1]
prefix = sys.argv[2]
dataDir = '/srv/runme/' + prefix + '/'

raw_log_name = "rawlog_%s.txt" % (timestamp)

f = open(dataDir + prefix + 'proc', 'a+')

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            raise ValueError("duplicate key: %r" % (k,))
        else:
            d[k] = v
    return d

while True:
    if not os.path.exists(dataDir + prefix + "/flock_proc"):
        break
    print "Sorry, the server is busy now..."
    time.sleep(0.001)

json_strs = open(dataDir + raw_log_name).readlines()

for json_str in json_strs:
    try:
        json_dict = json.loads(json_str, object_pairs_hook=dict_raise_on_duplicates)
        name = json_dict['name']
        age = json_dict['prop']['age']
        if int(age) < 0 or len(name) == 0:
                                            continue
        str1 = str(name) + '\t' + str(age) + '\n'
        f.write(str1)

    except:
        continue

f.close()
