#list = used to store multiple items in a single variable. Can always be updated/changed

#Each item in list is called an element
food = ["Pizza", "Hamburgers", "Hotdogs", "Spaghetti"]

food[0] = "Sushi"

print(food[0])

#Adds element to end of list
food.append("Ice Cream")

#Removes specified element
food.remove("Hotdogs")

#removes last element in list
food.pop()

#Inserts a value at a given index
food.insert(0,"Cake")

#sorts list alphabetically
food.sort()

#Removes everything in a list
food.clear()

for i in food:
    print(i)