#Exeception= events detected during execution that interrupt the flow of a program

try: #Catch and try dangerous code
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: #When someone attempts to divide by zero
    print(e) #e is optional but will show additional information about the error in the code
    print("You can't divide by zero!")
except ValueError as e: #When something is inputted that is not a integer
    print(e)
    print("Enter only numbers please!")
except Exception as e: #Not good practice to have one exception block to handle a lot of exceptions. Try to handle specific ones first
    print(e)
    print("something went wrong :(")
else: #If no errors are detected then this code is ran
    print(result)
finally: #Always at the end. Whether or not an except is caught. Finally is always ran. Often used to close files
    print("This will always execute")