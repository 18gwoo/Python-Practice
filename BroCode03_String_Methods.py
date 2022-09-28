name = "Garrett"

print(len(name))
#Find length of string

print(name.find("G"))
#Find position of letter in string (Note that all strings start with 0

print(name.lower())
#Makes all letters in string lower case. "Upper" does opposite

lower_name = name.lower()
#Creates a variable for "Garrett" but in all lower case

print(lower_name.upper())
#upper uppercases all letters in string

print(lower_name.capitalize())
#Uppercases first letter of string

print(name.isdigit())
#Returns true or false depending if string is digit. If string only contains digits, it will return true

print(name.isalpha())
#Asks if string contains only alphabetical letters. Will show false if there are spaces

print(name.count("r"))
#Counts number of specific letters in string. Case sensitive

print(name.replace("r","f"))
#Replaces first letter with second letter

print(name*3)
#Repeats string X amount of times
