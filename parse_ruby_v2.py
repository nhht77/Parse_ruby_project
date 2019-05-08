import os, sys
from utils import (getTargetPath, getRubyFiles, getTargetsPath, createList_v1, 
                   getValidDev, getDev, getDevPath)

Ruby_Files = getRubyFiles(sys.argv[1])
Path       = getTargetsPath(Ruby_Files)

# Return the dependency files
dev = getDev(Path)

# Formatting the file
newDev = getValidDev(Path, dev, "'", "")
validDev = getValidDev(Path, newDev, "/", "\\")

str = validDev['C:/Users/ASUS/Desktop/Parse_ruby_project/omniauth-twitter/lib/omniauth-twitter.rb'][1].replace("\"", "")

# return the absolute root of the dependency file
# validDev = 
getDevPath(sys.argv[1], validDev)

