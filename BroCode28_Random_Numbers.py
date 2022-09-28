import random

x = random.randint(1,6) #For integers

print(x)
print()

y = random.random()

print(y)#Random float 0-1
print()

myList = ["rock", "paper", "scissors"]
z = random.choice(myList) #random of the three
print(z)
print()

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards)