import os, sys
from utils import getTargetPath

Ruby_Files = []
Path       = []

for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        if file.endswith('.rb') or file.endswith('.ru'):
            f = os.path.join(root, file)
            Ruby_Files.append(f)
            
for rb in Ruby_Files:
   path = getTargetPath(rb)
   Path.append(path)

name = os.path.basename(sys.argv[1])

with open(name + ".list", "w+") as file:
    for p in Path:
        file.write(p + "\n")