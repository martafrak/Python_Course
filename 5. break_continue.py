#1. exercise: enumerate, break, format

list = ["milk","water","juice","tea"]
x = input("x = ")
x = int(x)
print("Start")

for i,element in enumerate(list):
    print("Check {}".format(i))
    if i == x:
        break
    print("{} is OK".format(element))

print("End")

#2. exercise

x = "Hello {}"
y = x.format("World")
print(x)
print(y)

x = "Are {} {}"
y = x.format("you", "understand?")
print(y)

#3. exercise

number = input("What are you looking for? number = ")
number2 = input("number2 = ")
number = int(number)
number2 = int(number2)

for i in range(30):
    if i == number:
        print("Found: ",i)
        break
    print(i)

#if we want continue we add continue instead break!

for i in range(30):
    if i == number:
        print("Found: ",i)
        continue
    if i == number2:
        print("Found: ",i)
        break
    print(i)

#4. exercise
list3 = ["milk","water","juice","tea"]

drink = input("What are you looking for?")
z = False
for num,element in enumerate(list3):
    if drink == element:
        z = True
        print(num+1," ",element, " is here")
    else:
        print(num+1," ",drink," is not here")
print("DONE")

#5. exercise

Fruits = ["orange","apple","banana","berry"]
fruit1 = input("fruit1 = ")
fruit2 = input("fruit2 = ")

if fruit1 in Fruits:
    print(fruit1," is here")
else:
    if fruit2 in Fruits:
        print(fruit1," is not here but ",fruit2," is here")
    else:
        print(fruit1," and ",fruit2," are not here")
print("Done")