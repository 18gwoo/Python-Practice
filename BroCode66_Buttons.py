from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count #makes it a global variable
    count+=1
    print(count)

window = Tk()

photo = PhotoImage(file='GUI_Icon.png')

button = Button(window,
                text="click me!",
                command=click,              #what the button does
                font=("Ariel",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00", #Used so that button changes colors (or not) when clicked
                activebackground="black",   #Same as above except for background
                state=ACTIVE,               #Can be set to disable so that button cant be used. Greys out button
                image=photo,                #Adds an image to the button
                compound='bottom')          #Image placement for button
button.pack()

window.mainloop()