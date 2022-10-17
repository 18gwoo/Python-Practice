from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\garre\\PycharmProjects\\Python_Practice\\copy.txt",  #Returns a string (Filepath of where our file is) #Sets the initial directory for when we open our file explorer
                                          title="Open file okay?",                                                    #Sets title within file explorer
                                          filetypes= (("text files","*.txt"),                                         #What appears to the user. #Creates a frop down menu
                                          ("all files","*.*")))                                                       #For text files and all files. Asterisks denote anything
    file = open(filepath,'r') #r (can also be written as rt) is for read text
    print(file.read()) #reads file
    file.close() #closes file

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()