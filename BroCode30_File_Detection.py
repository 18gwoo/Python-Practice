import os

#test.text
path = "C:\\Users\\garre\\Desktop\\test.txt"

if os.path.exists(path): #Tells us if path exists but not if it is a file or not
    print("That location exists")
    if os.path.isfile(path): #checks to see if it is a file
        print("That is a file")
else:
    print("That location doesn't exist")

import os

#Folder
path1 = "C:\\Users\\garre\\Desktop\\folder"

if os.path.exists(path1): #Tells us if path exists but not if it is a file or not
    print("That location exists")
    if os.path.isfile(path1):
        print("That is a file")
    elif os.path.isdir(path1): #checks to see if it is a directory
        print("That is a directory")
else:
    print("That location doesn't exist")