#Slicing is creating a substring by extracting elements from another string
    #indexing[] or slice()
    #[start:stop:step]

name = "Garrett Woo"

#Strings start with 0. With we just use [:8] it will be the same. Python assumes were starting at 0.
first_name = name[0:8]
#[8:] will also work
last_name = name[8:11]
#Gets every other character. [::2] also works
funky_name = name[0:11:2]
#Name in reverse (Because you take one step back each time)
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

#Not all website urls are the same. Therefore we need to use a negative index
slice = slice(7,-4)

#How to apply a sliced object (The slice variable) to a string
print(website1[slice])
print(website2[slice])
