from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y)) #Gets x and y coordinates

window = Tk()

window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething) #mousebutton release
#window.bind("<Enter>",doSomething) #Activates when you enter the window
#window.bind("<Leave>",doSomething) #Activates when you leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved. Will consistantely give coordinates
window.mainloop()