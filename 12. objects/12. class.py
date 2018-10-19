import run

#1. use function "fun" from run file
run.fun()

#2. check variable from run file
print(run.x)

#3. define class - class is a object's structure

class Calculator():
    def add(self,a,b):
        R = a + b
        print(R)
    def rm(self,a,b):
        R2 = a - b
        print(R2)

#create object

red_calculator = Calculator()

#how to use object
a = int(input("a = "))
b = int(input("b = "))
red_calculator.add(a,b)
red_calculator.rm(a,b)

#variable in classes - continue in 4.
green_calculator = Calculator()


#4. special method (init, del)

class Calculator2():

    def __init__(self):
        print("init")
    def __del__(self):
        print("Del")
    def add(self,a,b):
        R = a + b
        print(R)
    def rm(self,a,b):
        R2 = a - b
        print(R2)

#(if we run project -> print "init" and "del"  - because we create object and delete it below:
first_calculator = Calculator2()
second_calculator = Calculator2()

#example

def example():
    print("EXAMPLE - STEP 1")
    ex_calculator = Calculator2()
    print("STEP 2")
    a = int(input("a = "))
    print("STEP 3")
    b = int(input("b = "))
    print("STEP 4")
    Result = ex_calculator.add(a,b)
    print("STEP 5")
    print(Result)

example()
#DONE -> garbage collection
#we also create and delete "on my own"
print("new calc123")
calc123 = Calculator2()
del calc123

#we also use it in variable
print("delete variable")
a = int(input("a = "))
print(a)
del a
#print(a) - it doesn't work 'cause we deleted it
#but if we add new record:
a = "Hello"
print(a)

#new class

class Text():
    def __str__(self):
        return "def str is here"

    def __int__(self):
        return "def int is here"

    def __len__(self):
        return 100000

    def __bool__(self):
        return True

    def example_text(self,z):
        result = z
        print(result)
supertext = Text()
supertext.example_text(10)
print(len(supertext))

print(str(supertext))

if supertext:
    print("true")
else:
    print("false")
