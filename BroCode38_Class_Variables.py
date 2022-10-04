class Car:
    wheels = 4 #Class varaible. Inside class but not instead constructor. Default is 4 wheels

    def __init__(self, make, model, year, color):
        self.make = make #instance variables
        self.model = model #instance variables
        self.year = year #instance variables
        self.color = color #instance variables

car_1 = Car("Lexus", "GS300", "2002","Tan")
car_2 = Car("Ford","Mustang", "2022", "Red")

car_1.wheels = 2 #Edits car 1 to have 2 wheels

print (car_1.wheels) #2wheels
print(car_2.wheels) #4 wheels

print()

print(Car.wheels) #displays default number of wheels (4)
print()

Car.wheels = 2 #Changes default to 2

print (car_1.wheels) #2 wheels
print(car_2.wheels) #2 wheels