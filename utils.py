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
        Path.append(path[1:])
    return Path

def getDev(Path):
    dev = dict()

    for p in Path:
        dev[p]=[]
   
    for p in Path:
        lines = [line.rstrip('\n') for line in open(p)]
        for line in lines:
            if("require" in line):
                dev[p].append(line.replace("require ", ""))
    return dev

def getValidDev(Path, dev, kw1, kw2):
    newDev = dict()

    for p in Path:
        newDev[p]=[]

    for key, value in dev.items():
        for i in value:
            newDev[key].append(i.replace(kw1, kw2))

    return newDev

def createList_v1(argv, Path):
    Project_Name = os.path.basename(sys.argv[1])
    
    with open(Project_Name + ".list", "w+") as file:
        for p in Path:
            file.write(p + "\n")
