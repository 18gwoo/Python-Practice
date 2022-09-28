# str.format() = optional method that gives users more control when displaying output

animal = "Cow"
item = "Moon"

#print("The " + animal + " jumped of the " + item)

print("1. The {} jumped over the {}".format(animal,item)) #postion within format matters.

print()

print("2. The {1} jumped over the {0}".format(animal,item,"beef")) #positional argument
print("3. The {1} jumped over the {1}".format(animal,item,"beef"))

print()

print("4. The {item} jumped over the {animal}".format(animal = "cow",item = "moon")) #keyword argument (animal and item are now apart of keyword argument pairs)
print("5. The {animal} jumped over the {animal}".format(animal = "cow",item = "moon")) #Keywords can be used more than once

print ()

text = "6. The {} jumped over the {}"
print(text.format(animal,item))

print()

name = "Garrett"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10} nice to meet you".format(name))
print("Hello, my name is {:<10} nice to meet you".format(name)) # Won't change because it is the default
print("Hello, my name is {:>10} nice to meet you".format(name))
print("Hello, my name is {:^10} nice to meet you".format(name))
#IF WE WANT TO USE A KEYWORD OR POSITIONAL ARGUMENT PLACE IS BEFORE THE COLON {0/animal/etc:>10}

print ()

number = 3.14159
number2 = 1000
print("The number pi is {:.2f}".format(number)) #.2f makes it so that we only go 2 spaces after decimal. f stands for float. WILL ROUND THEN NUMBER
print("The number pi is {:,}".format(number2)) #Adds a comma every time its needed for 1,000 or 1,000,000 or etc
print("The number pi is {:b}".format(number2)) #Comes out in binary
print("The number pi is {:o}".format(number2)) #Displayed as an octal number
print("The number pi is {:x}".format(number2))#Works for lower case and upper case hexadecimal
print("The number pi is {:X}".format(number2))
print("The number pi is {:e}".format(number2))#Works for scientific notation as well (upper and lower case
print("The number pi is {:E}".format(number2))