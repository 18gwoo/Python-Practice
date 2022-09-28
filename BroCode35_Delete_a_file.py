import os
import shutil #needed to remove filled folders

path = "delete_test.txt"

try:
    #os.remove(path) #Does not remove empty folders
    #os.rmdir("empty_folder") #Deletes empty folders
    shutil.rmtree("folder") #dangerous: deletes folder and files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print (path + " was deleted")