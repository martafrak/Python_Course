#1. variable global/local (in functions)

x = int(input("x = ")) #it is global variable

def function1():
    print(x)
    z = int(input("z = ")) #local variable, only in function1
    print(x+z)

def function2():
    print(x)
    #print(z) #it doesn't work - z is local variable

function1()
function2()


#2. args
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
def summation(*args): #*args if we don't know how many arguments we need
    S = 0
    for a in args:
        S = S + a
    print(S)

summation(a,b,c)
summation(34,443654,34645432,3546454,54575653,346764532,6454) #example


#BMI calculator
def BMI(name,height,weight):
    R = weight/(height ** 2)
    print(name,", your BMI is: ",R)

lists = ["Mike",1.80,95] #global

BMI(lists[0],lists[1],lists[2])
BMI(*lists)