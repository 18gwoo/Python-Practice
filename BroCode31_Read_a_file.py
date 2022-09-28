try: #Exception handling
    with open("test.txt") as file: #name file (if it is in your project folder) or file path. "With open" automatically closes the file. Doesn't catch exceptions though
        print(file.read())
except FileNotFoundError:
    print("That file was not found")

print(file.closed) #Checks to see if a files is closed. When reading a file it is normally open and needs to be closed manually.