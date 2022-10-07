from tkinter import *

#label is an area widget that holds text and/or an image in a window

window = Tk()

photo = PhotoImage(file="GUI_Icon.png")

label = Label(window, #Paranthesis are constructor for the widget and arguments can be passed in
              text = "Hello this is my first GUI",  #Widget size actually changes in order to accomadate the size of components
              font = ("Arial", 40, "underline"),    #font options (font, font size, style(italics, underline, bold)).
              fg="green",                           #fg stands for foreground and is the text color (can be in hexa decimal or color name).
              bg = "black",                         #bg is background color
              relief=RAISED,                        #Chooses border
              bd=10,                                #increases border width
              padx=20,                              #Increases distance between border and text on the x axis
              pady=20,                              #Increases distance between border and text on the y axis
              image=photo,                          #Adds image to label
              compound="bottom")                    #Places image on bottom
label.pack() #Places widget to top center of window
#label.place(x=100,y=100) #Places label in specific spots in window

window.mainloop()