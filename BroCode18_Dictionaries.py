#Dictionary = A changeable, unordered collection of unique key:value pairs
#   Fast because they use hashing, which allows us to access a value quickly

#data types dont matter
capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

#Dictionarys are muteable
#Adds key and value
    #capitals.update({"Germany":"Berlin"})
#Updates a keys value
    #capitals.update({"USA":"Las Vegas"})

#Unsafe because if something is inputed that is not in dictionary it will fail
    #print(capitals["Ukraine"])

#Used to delete a key value pair
    #capitals.pop("China")

#Removes everything from dictionary
    #capitals.clear()

#Safer to use get method
print(capitals.get("Ukraine"))

#Shows dictionary keys
print(capitals.keys())
#Shows dictionary values
print(capitals.values())
#Shows every item in a dictionary
print(capitals.items())

#Alternate way to print dictionary items
for key,value in capitals.items():
    print(key,value)

