class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color): #Constructor
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image) #Gets coordinates within canvas (given as list (top left and bottom right coordinates are given))

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0): #self.canvas.winfo_width() gives the width of the canvas
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image,self.xVelocity,self.yVelocity) #Moves across window