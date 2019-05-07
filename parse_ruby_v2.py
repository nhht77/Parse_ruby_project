import os, sys
from utils import (getTargetPath, getRubyFiles,
                   getTargetsPath, createList_v1)

Ruby_Files = getRubyFiles(sys.argv[1])
Path       = getTargetsPath(Ruby_Files)

createList_v1(sys.argv[1], Path)



