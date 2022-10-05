# multi level inheritence is when a derived class (child) inherits another derived class (child)

class Organism:

    alive = True

class Animal(Organism): #child of Organism

    def eat(self):
        print("This animal is eating")

class Dog(Animal): #grandchild of organism

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()