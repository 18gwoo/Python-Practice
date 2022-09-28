# index operator [] = gives access to a sequence's element (str,list,tuples)
#Refer to string slicing (7)

name = "garrett Woo!"

if name[0].islower():
    name = name.capitalize()
print(name)

#can also use [:7]
first_name = name[0:7].upper()
last_name = name[8:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)