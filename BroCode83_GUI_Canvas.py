# canvas =  widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="blue",width=5)                        #Creates a line. Starts at 0,0 and ends at 500,500
#canvas.create_line(0,500,500,0,fill="red",width=5)                         #Starts at 0,500 and ends at 500,0 #Can assign these all by variables
#canvas.create_rectangle(250,250,50,50,fill="purple")                       #Starting coordinate is for top left of rectangle and ending is for bottom right
#points = [250,0,500,500,0,500]                                             #Points for next shape
#canvas.create_polygon(points,fill="yellow",outline="black",width=5)        #Creates a polygon. In this case a triangle
canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)             #Alternative styles CHORD (Bow) or ARC (Curved line). Start changes the position by degrees
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)               #Extent is in degrees and denotes what degree our arch is in
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)                   #Creates an oval
canvas.pack()

window.mainloop()