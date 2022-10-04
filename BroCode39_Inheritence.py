#inheritence: Parent child relationships. Parent class traits are give to child classes. Children have everything parents have + whatever the child has

class Animal: #Useful so that we dont need to change the each child class at all if we need to change something like sleep, alive, or eat
    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def hop(self):
        print("The rabbit hopped")
class Fish(Animal):
    def swim(self):
        print("The fish swam")
class Hawk(Animal):
    def fly(self):
        print("The hawk flew")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive) #alive is inherited from parent class
fish.eat()
hawk.sleep()

print()

rabbit.hop()
fish.swim()
hawk.fly()