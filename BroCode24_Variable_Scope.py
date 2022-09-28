#Scope = A region that a variable is recognized
#       A variable is only available from inside the region it is created
#       A global and locally scoped versions of a variable can be created

#Global scope (available inside and outside a function)
name = "Garrett"


#This variable has a local scope bc it is declared inside of a function. So it is only available inside this function
def display_name():
    name = "Woo" #local scope. If this line was removed. Line 15 will produce "Garrett" as well since it is the global version of name
    print(name)

print(name)
display_name()

#LEGB = like pemdas
#Local -> Enclosing -> Global -> Built-in