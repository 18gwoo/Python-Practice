from tkinter import *

def submit():
    print("It is " + str(scale.get()) + " degrees C.")

window = Tk()

#placed at top
hotImage = PhotoImage(file = "GUI_Icon.png") #placeholder for fire image
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100, #sets range for scale
              to=0,
              length=600, #length of scale
              orient=VERTICAL, #scale orientation
              font = ("Consolas",20),
              tickinterval = 10, #adds indicator for values
              #showvalue = 0, #Hide current numeric value of slider
              troughcolor= "green", #changes color of slider
              fg = "#FF1C00",
              bg = "Black"
              )
scale.set(50) #has the scale start at 50 \\\\ ((scale["from"]-scale["to"])/2)+scale("to") will always start at the middle
scale.pack()

#placed at bottom
coldImage = PhotoImage(file = "GUI_Icon.png") #placeholder for snowflake image
coldLabel = Label(image=hotImage)
coldLabel.pack()


button = Button(window,
                text = "submit",
                command = submit)
button.pack()
window.mainloop()