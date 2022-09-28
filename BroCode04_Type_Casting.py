#Type casting converts the data type of a value to another data type

x = 1 #int
y = 2.0 #float
z = "3" #Str



print(x)
print(y)
print(z)

#Changes float to an integer
#print(int(y))

#Type casts y (Rounds down)
y = int(y)

print(y)

#Changes z into an integer and lets us multiply otherwise, as we see, it just repeats it three times like a string
print(z*3)
z = int(z)
print (z*3)

#Changes to float (Can also be multiplied like normal)
x = float(x)
y = float(y)
z = float(z)

print(x)
print(y)
print(z)

#Same for strings
x = str(x)
y = str(y)
z = str(z)

print("X is " + x)
print("Y is " + y)
print("Z is " + z)
