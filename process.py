import os, json, sys

dataDir = '/srv/runme/'
prefix = sys.argv[1]

f = open(dataDir+prefix+'.txt', 'w')

for file in os.listdir(dataDir):
    if file.startswith(prefix):
        json_strs = open(dataDir+file).readlines()
        for json_str in json_strs:
            try:
                json_dict = json.loads(json_str)
                name = json_dict['name']
                age = json_dict['prop']['age']
                str1 = str(name)+'\t'+str(age)+'\n'
                f.write(str1)

            except:
                continue

f.close()