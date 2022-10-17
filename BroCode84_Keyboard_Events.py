from tkinter import *

def doSomething(event):
    #print("You pressed: " + event.keysym)    #keysim shows what key was pressed
    label.config(text=event.keysym)

window = Tk()
#Key denotes any key
window.bind("<Key>",doSomething) #(event[Key name],function) Enter key = Return.

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()