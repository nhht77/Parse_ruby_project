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

def createInternalDevList(argv, dev):
    list = []
    for root, dirs, files in os.walk(argv):
        f = None
        for file in files:
            for key, value in dev.items():
                for idx, val in enumerate(value):
                    if val in os.path.join(root, file):
                        f = os.path.join(root, file)
                        list.append("/"+key+":/"+f.replace("\\", "/")+":required_internal")
    createList_v1(argv, list, "internal_deps")

def createExternalDevList(argv, dev):
    list = []
    for root, dirs, files in os.walk(argv):
        f = None
        for file in files:
            for key, value in dev.items():
                for val in value:
                    if val not in os.path.join(root, file):
                        print(val.replace("\\", "/"))
                        print(key)
                        list.append("/" + key + ":/External​/" + val.replace("\\", "/") + ":required_external")
    createList_v1(argv, list, "external_deps")

def createList_v1(argv, Path, dev_type):
    Project_Name = os.path.basename(sys.argv[1])
    with open(Project_Name + "_" + dev_type + ".list", "w+", encoding="utf-8") as file:
        for p in Path:
            file.write(p + "\n")
