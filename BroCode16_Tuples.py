# tuples are collections which are ordered and unchangeable
# used to group together related data

student = ("Garrett", 22, "Male")

#Counts how many times given item shows up in tuple
print(student.count("Garrett"))
#Gives numbered location of element in given tuple
print(student.index("Male"))

for i in student:
    print(i)

if "Garrett" in student:
    print("Garrett is here")