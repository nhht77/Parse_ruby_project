import os, sys

# INPUT   : Ruby file
# OUTPUT  : Absolute source path of a ruby file
# PURPOSE : Return a absolute src path of a ruby file
def get_project_path(sys):
    if(len(sys.argv) < 2 or len(sys.argv[1]) == 0):
        raise ValueError("Please enter the project path.")
    return sys.argv[1]

# INPUT   : Ruby file
# OUTPUT  : Absolute source path of a ruby file
# PURPOSE : Return a absolute src path of a ruby file
def get_target_path(p):
    return ("/" + os.path.realpath(p).replace("\\", "/"))

# INPUT  : PATH in CMD 
# OUTPUT : Array of ruby files
# PURPOSE: This func receive the path in order to sort out all ruby files and return an array of ruby files
def get_ruby_files(argv):
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
def get_ruby_targets_path(Ruby_Files):
    return [get_target_path(rb)[1:] for rb in Ruby_Files]

# INPUT  : An array of absolute path of each ruby files 
# OUTPUT : a dictionary contains absolute ruby files and dependency that belongs to the files
# PURPOSE: Find out if the ruby files has any dependency, then sort them accordingly
def get_dev(ruby_files_target):
    dev = dict()
    for rb in ruby_files_target:
        dev[rb]=[]
   
    for rb in ruby_files_target:
        lines = [line.rstrip('\n') for line in open(rb)]
        dev[rb] = [ line.replace("require ", "") for line in lines if ("require" in line)]  
    return dev

# INPUT  : Array of Ruby files, dictionary of ruby file and dependency, invalid keyword to remove, valid keyword to replace  
# OUTPUT : A dictionary of absolute ruby files and valid dependency file format
# PURPOSE: Format the dependency to be searchable in the dictionary of ruby files
def get_valid_dev(ruby_files_target, dev, kw1, kw2):
    valid_dev = dict()
    for rb in ruby_files_target:
        valid_dev[rb]=[]

    for key, value in dev.items():
        valid_dev[key] = [i.replace(kw1, kw2) for i in value]  
    return valid_dev

# INPUT  : PATH argv from the CMD, dictionary of ruby files and an array of dependency belongs to each ruby files
# OUTPUT : A list of internal files
# PURPOSE: Produces a list of ​internal file-level dependencies.
def create_internal_dev_list(argv, dev):
    list = []
    for root, dirs, files in os.walk(argv):
        for file in files:
            f = os.path.join(root, file)
            for key, value in dev.items():
                for val in value:
                    if val in os.path.join(root, file):
                        f = os.path.join(root, file)
                        list.append("/"+key+":/"+f.replace("\\", "/")+":required_internal")
    create_list(argv, list, "internal_deps")

# INPUT  : PATH argv from the CMD, dictionary of ruby files and an array of dependency belongs to each ruby files
# OUTPUT : A list of exertnal files
# PURPOSE: Produces a list of external file-level dependencies.
def create_external_dev_list(argv, dev):
    list = []
    for root, dirs, files in os.walk(argv):
        f = None
        for file in files:
            for key, value in dev.items():
                for val in value:
                    if val not in os.path.join(root, file):
                        list.append("/" + key + ":/External​/" + val.replace("\\", "/") + ":required_external")
    create_list(argv, list, "external_deps")

# INPUT  : PATH argv from the CMD, Array of files, type of dependency
# OUTPUT : the list file with information of file and its dependency
# PURPOSE: Create the list file with information of file and its dependency
def create_list(argv, Files, dev_type):
    Project_Name = os.path.basename(sys.argv[1])
    with open(Project_Name + "_" + dev_type + ".list", "w+", encoding="utf-8") as file:
        for p in Files:
            file.write(p + "\n")
    print(Project_Name + "_" + dev_type + ".list")