# Prevents a user from creating an object of that class "abstract classes are like a template. it's not real"
# + compels a user to override abstract methods in a child class (form of checks and balances

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.


from abc import ABC, abstractmethod

class Vehicle(ABC): #What if we wanted to prevent someone from creating something of the vehicle class. (Its too generic and doesnt have features/implementations)(Child classes are fully fleshed out)

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self): #method overriding
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self): #without a overriding method, code will fail. In this way, abstract classes can be used to make sure that overriding methods are done properally
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle() #doesnt work because vehicle is now an absract class
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.stop()