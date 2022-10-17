from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cut():
    print("You cut some text!")
def copy():
    print("You copied some text!")
def paste():
    print("You pasted some text!")

window = Tk()

openImage = PhotoImage(file="GUI_Icon.png")
saveImage = PhotoImage(file="GUI_Icon.png")
exitImage = PhotoImage(file="GUI_Icon.png")

menubar = Menu(window) #creates menubar
window.config(menu=menubar) #adds menubar

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))                                  #Creates a file menu #Tearoff eliminates whats known as a tear off from the file menu
menubar.add_cascade(label="File",menu=fileMenu)                                         #Adds drop down for file menu
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')     #Adds an open command in file menu
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')     #Adds a save command in file menu
fileMenu.add_separator()                                                                #Adds a line to seperate sections
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')         #Adds exit command. #quit is a shortcut to exit something

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))                                  #Creates an edit menu
menubar.add_cascade(label="Edit",menu=editMenu)                                         #Adds dropdown for edit menu
editMenu.add_command(label="Cut",command=cut)                                           #Adds cut command
editMenu.add_command(label="Copy",command=copy)                                         #Adds copy command
editMenu.add_command(label="Paste",command=paste)                                       #Adds paste command

window.mainloop()