#function is a block of code which is executed only when it is called (Invoking a function)

def hello(name):
    print("Hello " + name)
    print("Have a nice day")

hello("Garrett")

print()

#Within the parenthesis are called an argument. However we need a parameter. Parameter in this case is 'name'
    #hello("Garrett")
    #hello("Bruh")

#my_name = "bro"
    #hello(my_name)

def hello2(first_name,last_name):
    print("Hello " + first_name + " " + last_name)
    print("Have a nice day")


hello2("Garrett","Woo")

print()

def hello3(first_name,last_name,age):
    print("Hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day")

hello3("Garrett", "Woo", 22)