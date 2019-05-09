import os, sys
from utils import (getTargetPath, getRubyFiles, getTargetsPath, getValidDev,
                   getDev, createInternalDevList, createExternalDevList, getProjectPath)

project_path = getProjectPath(sys)

# Get all ruby files from the project path in an array
Ruby_Files = getRubyFiles(project_path)

# Get the absolute target path of each ruby file in an array
Path = getTargetsPath(Ruby_Files)

# Get the dependency files of each ruby file as a dictionary
dev = getDev(Path)

# Formatting the dependency file
newDev = getValidDev(Path, dev, "'", "")
validDev = getValidDev(Path, newDev, "/", "\\")

# creating the list of internal and external file
createInternalDevList(sys.argv[1], validDev)
createExternalDevList(sys.argv[1], validDev)