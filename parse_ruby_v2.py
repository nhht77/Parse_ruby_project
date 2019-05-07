import os, sys
from utils import (getTargetPath, getRubyFiles,
                   getTargetsPath, createList_v1)

Ruby_Files = getRubyFiles(sys.argv[1])
Path       = getTargetsPath(Ruby_Files)
Path       = [p[1:] for p in Path]

# Return the require files
dev = []
for p in Path:
    lines = [line.rstrip('\n') for line in open(p)]
    for line in lines:
        if("require" in line):
            dev.append(line.replace("require ", ""))

newDev = [] 
for d in dev:
    newDev.append(d.replace("'", ""))

str = newDev[0].replace("/", "\\")
print(str.replace("\"", ""))

for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if str.replace("\"", "") in os.path.join(root, file):
                print(file)