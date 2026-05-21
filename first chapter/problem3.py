#write a python program to print the content of directory using the os module, search online for the function which does that
import os

# Specify the directory path
path = "/"

# Get all files and folders in the directory
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)