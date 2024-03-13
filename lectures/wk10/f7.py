"""
OS module
    info about the Operating System

    window, linux, mac environment
    file and folder manipulation
"""
import os

print(os.name)
# help(os)
print(os.linesep)  # '\r\n' => \n
print(os.sep)  # path seperator   \        /

print("All files and folders of CWD is")
files_and_folders = os.listdir(os.getcwd())
print(files_and_folders)

import re

for file in files_and_folders:
    print(file, "is dir?", os.path.isfile(file))
    match1 = re.findall(pattern=r"(.py|.ipyn)$", string=file)
    match2 = file.endswith(".py") or file.endswith(".ipyn")

merge_file_names = ",".join(files_and_folders)
print(merge_file_names)
