#Function

#1. exercise
def printme():
    print("Hello World",end=" ")
    print(":) :) :) ")

printme()
printme()

#2. function and variable
number = input("number = ") #add variable
def printme(number): #define function
    print(number)
printme(number) #function call

#3. multiplication

number1 = int(input("Number1 = "))
number2 = int(input("Number2 = "))

def multiplication(number1,number2):
    R = number1 * number2
    print(R)
multiplication(number1,number2)

#4. return and function

a = int(input("a = "))
b = int(input("b = "))

def summation(a,b):
    return a+b
Result = summation(a,b)
print(a," + ",b," = ",Result)

#5. key words
c1 = int(input("c = "))
d1 = int(input("d = "))

def device(c,d):
    return c/d
Result2 = device(d=d1,c=c1)
print(c1," : ",d1," = ",Result2)

#6. check name! (for polish name)

name = input("Name: ")

def checkname(name):
    if(name[-1]) == "a": #check last char
        print(name,", You are a woman!")
    else:
        print(name,", You are a man!")

checkname(name)

#7. factorial

var = int(input("var = "))
def factorial(var):
    i = 1
    F = 1
    while i < var:
        i = i+1
        F = F * i
    return F
print(factorial(var))