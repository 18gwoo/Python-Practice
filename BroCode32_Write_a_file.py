
text = "YOOOOOOOOOOO\nThis is some text\nLet's have a good one"  #\n goes to a new line. Also overwrites files

with open ("test.txt","w") as file: #By default it is r for read. But in this case we are writing a file and so we put w
    file.write(text)

#appending files

text = "\n(Edited) Let's have a nice day"

with open ("test.txt","a") as file: #a for append. Adds onto the text file
    file.write(text)
