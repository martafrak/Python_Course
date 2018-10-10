# control structure - python
#1. exercise
x = input("x = ")
y = input("y = ")

if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal y")
else:
    print("x is greater than y")
print("Done")

#2. exercise

K  = x < y
print(type(K))

if K:
    print("True")
else:
    print("False")
print(K)

#3. exercise
x = input("x = ")

if bool(x):
    print("True")
else:
    print("False")

#4. exercise

a = input("a = ")
a = int(a)

if a < 10 and a > 1:
    print("a is less than 10 and greater than 1")
elif a < 10 and a < 1:
    print("a is less than 10 and 1")
else:
    print("a is greater than 1 and 10")

#5. exercise
if a > 10 or  a < 1:
    print("True")
else:
    print("False")

#6. exercise

z = input("z = ")
string = input("Text: ")
if z in string:
    print("z is in text")
else:
    print("z is not in text")

#7. exercise

R = input("R = ")
R = int(R)
if not R >10:
    print("R is less than 10")
else:
    print("R is greater than 10")
