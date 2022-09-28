#These inputs will come out as strings
name = input("What is your name?: ")
#If input contains decimals this will error
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age + 1
age +=1

print("It is nice to meet you " + name)
print("You will turn " + str(age) +" soon.")
print("You are "+str(height)+" cm tall")
