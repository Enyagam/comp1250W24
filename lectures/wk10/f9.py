"""
Ask the user for a folder name

Determine if the folder name exists
    If so, output message to user => already exists & do you want to delete it?
        If yes, delete it
        If no, thank user for using program
    If no, create the folder

"""
import os
import sys

folder_name = input("Enter a folder name")

if os.path.exists(folder_name):
    print("Folder", folder_name, "exists", file=sys.stderr)
    result = input("Do you want to delete this folder? y/n")
    if result.strip().lower()[0] == 'y':
        if len(os.listdir(folder_name)) == 0:
            os.rmdir(folder_name)
            print("Folder deleted successfully")
        else:
            print(folder_name, "is not empty. Cannot remove because I do not want to code a loop and manually delete all content", file=sys.stderr)

            for file in os.listdir(folder_name):
                target = folder_name + "/" + file
                if os.path.isfile(target):
                    print("Removing file", file)
                    os.remove(target)
                else:
                    print("Removing dir", file)
                    os.rmdir(target)
            os.rmdir(folder_name)
    else:
        print("Thank you for using the program")
else:
     os.makedirs(folder_name)
     print("Folder", folder_name, "created successfully")