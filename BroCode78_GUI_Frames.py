# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

#button = Button(window,text="W",font=("Consolas",25),width=3)
#button.pack()
#Shortcut for above is Button(window,text="W",font=("Consolas",25),width=3).pack()
#Just cant be adjusted by its name since it doesnt have one anymore

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN) #Frames are needed so that widgets are contained when the window is expanded. #bd is the width of border and relief is type of border
frame.pack(side=BOTTOM)                               #Has frame stick to bottom of window. x and y has frame stick to those coordinates no matter how the window is resized (#x=0,y=0)

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP) #Shortcut. Notice how they are allotted for frames rather than anything else
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()