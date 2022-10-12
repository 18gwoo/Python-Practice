from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor() #assign color to a variable. Varaible is a tuple containing a tuple of rgb values at index 0 and the hexadecimal value at index 1
    colorHex = color[1]         #assigns element at index 1 to a variable
    window.config(bg = colorHex) #change background color



    #window.config(bg=colorchooser.askcolor()) This can also work instead of the above three lines



window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()