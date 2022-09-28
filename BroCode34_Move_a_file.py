import os

source = "move_test.txt" #Where the source file is locatied
destination = "C:\\Users\\garre\\Desktop\\Bro_Code_Python_Files\\move_test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print("{} was moved".format(source))
except FileNotFoundError:
    print(source + " was not fount")

source2 = "move_test_folder" #Where the source file is locatied
destination2 = "C:\\Users\\garre\\Desktop\\Bro_Code_Python_Files\\move_test_folder"

try:
    if os.path.exists(destination2):
        print("There is already a file there")
    else:
        os.replace(source2,destination2)
        print("{} was moved".format(source2))
except FileNotFoundError:
    print(source2 + " was not fount")