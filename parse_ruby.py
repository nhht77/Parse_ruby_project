import os, sys
from utils import (get_target_path, get_ruby_files, get_ruby_targets_path, get_valid_dev,
                   get_dev, create_internal_dev_list, create_external_dev_list, get_project_path)

project_path = get_project_path(sys)

# Get all ruby files from the project path in an array
Ruby_Files = get_ruby_files(project_path)

# Get the absolute target path of each ruby file in an array
Ruby_files_target = get_ruby_targets_path(Ruby_Files)

# Get the dependency files of each ruby file as a dictionary
dev = get_dev(Ruby_files_target)

# Formatting the dependency file
new_dev = get_valid_dev(Ruby_files_target, dev, "'", "")
valid_dev = get_valid_dev(Ruby_files_target, new_dev, "/", "\\")

# creating the list of internal and external file
create_internal_dev_list(sys.argv[1], valid_dev)
create_external_dev_list(sys.argv[1], valid_dev)