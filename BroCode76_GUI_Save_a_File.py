from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\garre\\PycharmProjects\\Python_Practice",
                                    defaultextension='.txt',            #Defaults what files are saved as
                                    filetypes=[                         #What file types we can save as
                                        ("Text file",".txt"),           #(What shows in drop down menu, file extension)
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None: #prevents us from getting an exception from exiting file early
        return
    filetext = str(text.get(1.0,END)) #Gets text from text area
    #filetext = input("Enter some text I guess: ") //use this if you want to use console window. Still has us open and save a file but we enter text in console after we save it
    file.write(filetext) #Writes text to file
    file.close()

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()