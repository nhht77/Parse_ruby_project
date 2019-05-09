import os, sys
from utils import (getTargetPath, getRubyFiles, getTargetsPath, getValidDev,
                   getDev, createInternalDevList, createExternalDevList)

Ruby_Files = getRubyFiles(sys.argv[1])
Path       = getTargetsPath(Ruby_Files)

# Get the dependency files of each ruby file
dev = getDev(Path)

# Formatting the file
newDev = getValidDev(Path, dev, "'", "")
validDev = getValidDev(Path, newDev, "/", "\\")

# return the absolute root of the dependency file
createInternalDevList(sys.argv[1], validDev)
createExternalDevList(sys.argv[1], validDev)