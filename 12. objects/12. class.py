import run

#use function "fun" from run file
run.fun()

#check variable from run file
print(run.x)

#define class - class is a object's structure

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

#variable in classes
green_calculator = Calculator()