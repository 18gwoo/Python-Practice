from tkinter import *
import time

WIDTH = 500 #Constants. Will not change throughout code. Make these capitalized
HEIGHT = 500
xVelocity = 1
yVelocity = 1
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='GUI_Icon.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='GUI_Icon.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image) #Coordinates of my_image within the canvas
    print(coordinates) #Returns as a list
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity            #Inverses the velocity if wall is hit
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity            #Inverses the velocity if wall is hit
    canvas.move(my_image,xVelocity,yVelocity) #Moves image (image, x movement, y movement)
    window.update()
    time.sleep(0.03)

window.mainloop()