# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

#happy = True
#print(happy)

#print(happy := True) #Returns as true. assignment within expression

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

#same as above
foods = list()
while food := input("What food do you like?: ") != "quit": #food is assigned using the walrus operator. != is not equal
    foods.append(food)