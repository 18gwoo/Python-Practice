# ------------------------------
# if _name_ == '__main__'
# ------------------------------

# why?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is _name_
#  Python will assign the _name_ variable a value of '__main__' if it's
#  the initial module being run
import BroCode59_part_2

print(__name__)
print(BroCode59_part_2.__name__) #shows as name of module (BroCode58_zip_function)

def main():
    print("Hello!")


if __name__ == '__main__':
    print ("Running this module directly")
else:
    print("Running other module indirectly")

#still a bit confused look at https://www.youtube.com/watch?v=OBabwRH0XUo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=60&ab_channel=BroCode again
