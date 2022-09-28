#copy file() = copies contents of a file
#copy() = copy file() + copies permission mode + destination can be a directory
#copy2() = copy() + copies meta data (file's creation and modification times)
#Copy or copy2 may need to be used depending on the project

import shutil

shutil.copyfile("test.txt", "copy.txt") #source(src)(need file path unless its in the project folder,destination().
                                        #Since no destination was indicated it goes in the project folder

shutil.copyfile("test.txt", "C:\\Users\\garre\\Desktop\\copy.txt") #Will copy to desktop as "copy.txt

#copy() and copy2() have same formatt. Just replace copyfile() (shutil.copy2()/shutil.copy())