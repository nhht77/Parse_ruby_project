import os, sys
from utils import (getTargetPath, getRubyFiles, getTargetsPath, createList_v1, 
                   getValidDev, getDev)

Ruby_Files = getRubyFiles(sys.argv[1])
Path       = getTargetsPath(Ruby_Files)

# Return the dependency files
dev = getDev(Path)

# Formatting the file
newDev = getValidDev(Path, dev, "'", "")
validDev = getValidDev(Path, newDev, "/", "\\")

str = validDev['C:/Users/ASUS/Desktop/Parse_ruby_project/omniauth-twitter/spec/spec_helper.rb'][5]
print(str)

# return the absolute root of the dependency file
for root, dirs, files in os.walk(sys.argv[1]):
        f = None
        for file in files:
            if str in os.path.join(root, file):
                f = os.path.join(root, file)
            else: 
                f = False
        print(f)