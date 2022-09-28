# Loop control statements = change a lioops execution from its normal sequence

#break = uesed to terminate the loop enteirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

#Continually goes until there is a break
while True:
    name = input("Enter your name: ")
    if name != "":
        break

Phone_Number = "714-351-4557"

for i in Phone_Number:
    if i == "-":
        continue
    else:
        print (i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)