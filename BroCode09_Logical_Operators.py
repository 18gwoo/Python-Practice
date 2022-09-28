#Logical operators = (and, or, not) checks if two or more conditional statements are true (not is a little different)

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("It is " + str(temp) + " degrees. Go touch some grass!")
elif temp < 0 or temp > 30:
    print("The weather is bad today at " + str(temp) + " degrees. Stay inside!")

#Not comes after if. If the statement is true "not" makes it false and vice versa

temp2 = int(input("What is the temperature outside?: "))

if not temp2 <0 or temp2 >30:
    print("It is " + str(temp2) + " degrees. Go touch some grass!")
elif not temp >= 0 and temp <= 30:
    print("The weather is bad today at " + str(temp2) + " degrees. Stay inside!")
