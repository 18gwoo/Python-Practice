# set = collection which is unordered, unindexed. No duplicate values. Lists are ordered and indexed

silverware = {"fork", "spoon", "knife", "knife"}

silverware.add("napkin")

silverware.remove("fork")
#clears set
    #silverware.clear()

for i in silverware:
    print (i)

#set is faster than a list and does not allow duplicates

dishes = {"bowl", "plate", "cup", "knife"}

#adds a sets elements to another set
    #silverware.update(dishes)

for i in dishes:
    print (dishes)

#merges two sets into one
dinner_table = silverware.union(dishes)

for i in dinner_table:
    print (dinner_table)

#want to see what silverware has that dishes doesnt

print(silverware.difference(dishes))

#What do the two have in common
print(silverware.intersection(dishes))