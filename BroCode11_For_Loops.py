import time
#For loop is a statement that executes its block of code a limited number of times.

#While loops = unlimited
#For loops = limited

for i in range(1,11):
    print (i)

for index in range(10):
    print (index+1)

#First number is inclusive and last number is exclusive. 2 is the step. Similar to string slicing
for i in range(50,100+1,2):
    print(i)

#Can iterate through anything deemed iterable such as strings or collections

for i in "Garrett Woo":
    print (i)

for seconds in range (10,0,-1):
    print (seconds)
    time.sleep(1)
print("Happy New Year!")
