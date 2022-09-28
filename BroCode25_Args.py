#args = parameter that packs all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

def add(num1,num2):
    sum = num1 + num2
    return sum

print (add(1,2)) #if third parameter was added function will not work


def add2(*args): #args can be named whatever you want. The asterisk is the impoortant part
    sum = 0
    args = list(args) #This and line 14 are needed so that we can turn the tuple into a list
    args[0] = 0
    for i in args:
        sum += i
    return sum

print (add2(1,2,3,4,5,6)) #varying amount of arguments are input but are ok due to args