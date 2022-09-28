# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments


def hello(**kwargs): #Used instead of (first,last) Doesnt have to be called kwargs. Just use the two asterisks
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end = " ")
    for key,value in kwargs.items():
        print(value, end = " ")



hello (title = "Mister", first = "Garrett", middle= "H", last = "Woo")