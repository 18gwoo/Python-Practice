#Graphical User Interface
from tkinter import * #type of gui included in python. Imports everything related to module

#Widgets = GUI elements: Buttons, textboxes, labels, images]
#Windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window. Creates but doesnt show our window
window.geometry("420x420") #Size of window
window.title("Garrett Woo's first GUI") #Chooses title of window

icon = PhotoImage(file='GUI_Icon.png') #converts image to photo image
window.iconphoto(True,icon) #sets windows icon to our photo "icon"
window.config(background="#5cfcff") #Changes background color

window.mainloop() #place window on computer screen, also listens for events