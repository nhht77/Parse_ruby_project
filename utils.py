import os, sys

def getTargetPath(p):
    data = os.path.realpath(p)
    target = ("/" + data.replace("\\", "/"))
    return target

def getRubyFiles(argv):
    Ruby_Files = []
    for root, dirs, files in os.walk(argv):
        for file in files:
            if file.endswith('.rb') or file.endswith('.ru'):
                f = os.path.join(root, file)
                Ruby_Files.append(f)
    return Ruby_Files


def getTargetsPath(Ruby_Files):
    Path = []

    for rb in Ruby_Files:
        path = getTargetPath(rb)
        Path.append(path)
    return Path
    

def createList_v1(argv, Path):
    Project_Name = os.path.basename(sys.argv[1])
    
    with open(Project_Name + ".list", "w+") as file:
        for p in Path:
            file.write(p + "\n")
