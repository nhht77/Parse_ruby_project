import os, sys

# INPUT   : Ruby file
# OUTPUT  : Absolute source path of a ruby file
# PURPOSE : Return a absolute src path of a ruby file
def getTargetPath(p):
    return ("/" + os.path.realpath(p).replace("\\", "/"))

# INPUT  : PATH in CMD 
# OUTPUT : Array of ruby files
# PURPOSE: This func receive the path in order to sort out all ruby files and return an array of ruby files
def getRubyFiles(argv):
    Ruby_Files = []
    for root, dirs, files in os.walk(argv):
        for file in files:
            if file.endswith('.rb') or file.endswith('.ru'):
                f = os.path.join(root, file)
                Ruby_Files.append(f)
    return Ruby_Files

# INPUT  : Array of ruby files
# OUTPUT : Array of absolute path to the ruby files
# PURPOSE: Return an array of absolute path of each ruby file in the received directory
def getTargetsPath(Ruby_Files):
    return [getTargetPath(rb)[1:] for rb in Ruby_Files]

# INPUT  : An array of absolute path of each ruby files 
# OUTPUT : a dictionary contains absolute ruby files and dependency that belongs to the files
# PURPOSE: Find out if the ruby files has any dependency, then sort them accordingly
def getDev(Path):
    dev = dict()
    for p in Path:
        dev[p]=[]
   
    for p in Path:
        lines = [line.rstrip('\n') for line in open(p)]
        dev[p] = [ line.replace("require ", "") for line in lines if ("require" in line)]  
    return dev

# INPUT  : Array of Ruby files, dictionary of ruby file and dependency, invalid keyword to remove, valid keyword to replace  
# OUTPUT : A dictionary of absolute ruby files and valid dependency file format
# PURPOSE: Format the dependency to be searchable in the dictionary of ruby files
def getValidDev(Path, dev, kw1, kw2):
    newDev = dict()
    for p in Path:
        newDev[p]=[]

    for key, value in dev.items():
        newDev[key] = [i.replace(kw1, kw2) for i in value]  
    return newDev

# INPUT  : PATH argv from the CMD, dictionary of ruby files and an array of dependency belongs to each ruby files
# OUTPUT : A list of internal files
# PURPOSE: Produces a list of ​internal file-level dependencies.
def createInternalDevList(argv, dev):
    list = []
    for root, dirs, files in os.walk(argv):
        for file in files:
            f = os.path.join(root, file)
            for key, value in dev.items():
                for val in value:
                    if val in os.path.join(root, file):
                        f = os.path.join(root, file)
                        list.append("/"+key+":/"+f.replace("\\", "/")+":required_internal")
    createList_v1(argv, list, "internal_deps")

# INPUT  : PATH argv from the CMD, dictionary of ruby files and an array of dependency belongs to each ruby files
# OUTPUT : A list of exertnal files
# PURPOSE: Produces a list of external file-level dependencies.
def createExternalDevList(argv, dev):
    list = []
    for root, dirs, files in os.walk(argv):
        f = None
        for file in files:
            for key, value in dev.items():
                for val in value:
                    if val not in os.path.join(root, file):
                        list.append("/" + key + ":/External​/" + val.replace("\\", "/") + ":required_external")
    createList_v1(argv, list, "external_deps")

# INPUT  : PATH argv from the CMD, Array of files, type of dependency
# OUTPUT : the list file with information of file and its dependency
# PURPOSE: Create the list file with information of file and its dependency
def createList_v1(argv, Files, dev_type):
    Project_Name = os.path.basename(sys.argv[1])
    with open(Project_Name + "_" + dev_type + ".list", "w+", encoding="utf-8") as file:
        for p in Files:
            file.write(p + "\n")
    print(Project_Name + "_" + dev_type + ".list")
