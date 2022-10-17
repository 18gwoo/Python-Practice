from tkinter import *

def drag_start(event):
    widget = event.widget   #Makes it compatible with all widgets
    widget.startX = event.x #Event.x = Where we click within the label not the window.
    widget.startY = event.y
    print(event.x)

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x  #widget.winfo_x() gets top left coordinate of widget relative to our window
    y = widget.winfo_y() - widget.startY + event.y  #Event.y is where we drag widget to
    widget.place(x=x,y=y)
#Widget placement on window - starting clicked position + new position
window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion) #Occurs when left click is held and dragges

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()