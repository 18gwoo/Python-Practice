from tkinter import *
from time import *
import time

def update():
    time_string = strftime("%I:%M:%S %p") #colons lets us have colons in between. I is hours M is minutes and S is seconds
    time_label.config(text=(time_string))

    #time_label.after(1000,update) #Creates a recursive function (function that calls itself). .after calls a delay and uses a function after said delay. Delay is in milliseconds

    day_string = strftime("%A")
    day_label.config(text=(day_string))

    date_string = strftime("%B %d %Y")
    date_label.config(text=(date_string))

    window.after(1000,update)

window = Tk()

time_label = Label(window, font=("Times New Roman",50), fg="green", bg="black")
time_label.pack()

day_label = Label(window, font=("Times New Roman",50), fg="green", bg="black")
day_label.pack()

date_label = Label(window, font=("Times New Roman",45), fg="green", bg="black")
date_label.pack()

update()
#while True:  #Used is .after function wasnt used
    #update() #Updates time every second
    #window.update()

window.mainloop()