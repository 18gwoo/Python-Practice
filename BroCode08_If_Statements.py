#If statements are blocks that will execute if true

age = int(input("How old are you?: "))

#Even if you put 100 it will come back as "You are an adult" because age>= 18 comes first
if age >= 18:
    print("You are an adult")
elif age == 100:
    print("You are a century old")
elif age <0:
    print("You haven't been born yet")
else:
    print("You are a child")

#This will work instead
if age == 100:
    print("You are a century old")
elif age >=18:
    print("You are an adult")
elif age <0:
    print("You haven't been born yet")
else:
    print("You are a child")
