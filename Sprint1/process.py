import os, json, sys

dataDir = '/srv/runme/'
prefix = sys.argv[1]

f = open(dataDir+prefix+'.txt', 'w')

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError("duplicate key: %r" % (k,))
        else:
           d[k] = v
    return d

for file in os.listdir(dataDir):
    if file.startswith(prefix):
        json_strs = open(dataDir+file).readlines()

        for json_str in json_strs:
            try:
                json_dict = json.loads(json_str, object_pairs_hook=dict_raise_on_duplicates)
                name = json_dict['name']
                age = json_dict['prop']['age']
                if int(age) < 0 or len(name) == 0: continue
                str1 = str(name)+'\t'+str(age)+'\n'
                f.write(str1)

            except:
                continue

f.close()