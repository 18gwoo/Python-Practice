#Keyword arguments = arguments preceded by an identifier when we pass them to a function
#The order of the argument doesn't matter, unlike positional arguments
#Python knows the names of the arguments that our function receives

#Positional argument. if the arguments (Garrett H Woo) changed positions, it would change the codes outcome
def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello("Garrett", "H", "Woo")

#keyword argument
def hello2(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello2(last="Woo", middle="H", first="Garrett")