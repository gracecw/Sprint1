import os, json, sys


prefix = sys.argv[2]
dataDir = '/srv/runme/' + prefix + '/'
timestamp = sys.argv[1]

proc_log_name = "procraw_%s.txt" % (timestamp)
raw_log_name = "rawlog_%s.txt" % (timestamp)
f = open(dataDir + proc_log_name, 'w')


def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            raise ValueError("duplicate key: %r" % (k,))
        else:
            d[k] = v
    return d


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
