# sort() method   = used with lists
# sort() function = used with iterables

student = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

#Only works with lists not tuples
student.sort() #alphabetical order.      student.sort(reverse=True) will do reverse alphabetical order
for i in student:
    print (i)
print()

#For tuples
students1 = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
sorted_students1 = sorted(students1) #sorted function. Putting sorted(students1, reverse=True) will give reverse order
for i in sorted_students1:
    print(i)
print()

#list of tuples
students2 = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

#Alphabetical order by first object in tuple
students2.sort()
for i in students2:
    print(i)
print()

#Alphabetical by grade
grade = lambda grades:grades[1]
students2.sort(key=grade) # sorts current list. Can use students2.sort(key=grade, reverse=True) to reverse alphabetical order
for i in students2:
    print(i)
print()

#alphabetical by age
age = lambda ages:ages[2]
students2.sort(key=age) # sorts current list. Can use students2.sort(key=age, reverse=True) to reverse alphabetical order
for i in students2:
    print(i)
print()

#for tuples
people = (("Bob","Driver",22),
          ("Fred","Unemployed",18),
          ("Ted",'Student',15),
          ("Ben","Clerk",25))
employment_status = lambda job:job[1]
sorted_Employment_status = sorted(people, key=employment_status)
for i in sorted_Employment_status:
    print (i)
