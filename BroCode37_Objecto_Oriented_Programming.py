#Object is an instance of a class
#Create actions and characteristics of an object
#Class needs to be created first = blueprint that tells us what specific attributes or methods a disinct object will have. Can be created within main module or in a seperate file

class Car: #classes tend to be capitalized. Also better to put a class in a seperate file if it is really large. To import you would just type "From (file) import (class name)"

# Need a special method called init construct objects for us. (Also known as constructor
    def __init__(self, make, model, year, color):
        self.make = make #self refers to object we are currently making. instance variables
        self.model = model #These valiables found within the constructor are instance variables
        self.year = year #instance variables
        self.color = color #instance variables
#Methods
    def drive(self): #Need to pass in self for methods but not when we call it (Lines 24-25)
        print ("This " + self.model +" is driving")
    def stop(self):
        print ("This " + self.model + " is stopped")

car_1 = Car("Lexus", "GS300", "2002","Tan") #Note that there are five arguments for Car (self, make, year, color). However, we only need to input 4. Python automatically passes in self
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

print()

car_2 = Car("Ford","Mustang", "2022", "Red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()