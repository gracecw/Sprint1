import os, json, sys

dataDir = '/srv/runme/'
prefix = sys.argv[1]
f = open(dataDir+prefix+'.txt', 'w')

for file in os.listdir(dataDir):
    if file.startswith(prefix) and file.endswith('json'):
        json_str = open(dataDir+file).read()
        json_dict = json.loads(json_str)

        try:
            name = json_dict['name']
            age = json_dict['prop']['age']
            str1 = str(name)+'\t'+str(age)+'\n'
            f.write(str1)

        except:
            continue

f.close()