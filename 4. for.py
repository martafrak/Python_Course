#for

#1. first and simple exercise

list = ["milk", "dog","22"]

for number,element in enumerate(list):
    print(number+1,element)

#2. exercise
list2 = ["1","2","3","4","5","11","12"]
x = input("Where is x? x = ")
x = str(x)
for number in list2:
    if number == x:
        print("YES, ",x," is here!")
    else:
        print("Not here")

#3. generator
print("generator")
for i in range(10): #print -> 0-9
    print(i)

for i in range(10,30): #print -> 10-30
    print(i)

for i in range(10,100,5): #5 is step, so print -> 10-100 with step=5
    print(i)