#While loops are a block of code that executes as long as the condition remains true

name = ""

#Keeps running until while loop is true
while len(name) == 0:
    name = input("What is your name?: ")

print("Hello " + name)

#Keeps running until while loop is false (None, "", and 0 would return as false and would start the while loop)
name2 = None #Can also be 0 or ""

while not name2: #None comes back as false. Opposed to while, while not keeps going until it is true
    name2 = input("What is your name?: ")

print ("Hello " + name2)

#https://stackoverflow.com/questions/53198902/what-is-the-difference-between-none-and-false-in-python-3-in-a-boolean-sense (Person does a good job of explaining while not and None)