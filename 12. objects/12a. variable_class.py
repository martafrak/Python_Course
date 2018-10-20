#variable in class

class Calculator():

    def __init__(self):
        print("init")

    def add(self,a,b):
        R = a + b
        print(R)

    def rm(self,a,b):
        R2 = a - b
        print(R2)

#create object
calc = Calculator()

#use variable in class (variable "calc.number" is only in calc!

calc.number = 1
print(calc.number)
calc.number += 5
print(calc.number)


#but we can add variable as self (self.number in __init__ method)

class Calculator2():

    def __init__(self):
        self.number = 1

    def add(self,a,b):
        R = a + b
        print(R)

    def rm(self,a,b):
        R2 = a - b
        print(R2)

#create object
calc2 = Calculator2()
calc3 = Calculator2()

#we can use variable in every calc
calc2.number += 2
print(calc2.number)
calc3.number += 4
print(calc3.number)


#EXAMPLE - last result

class Calculator5():

    def __init__(self):
        self.last_result = 0

    def add(self,a,b):
        R = a + b
        print(R)
        self.last_result = R

    def rm(self,a,b):
        R2 = a - b
        print(R2)
        self.last_result = R2

#create object
calc5 = Calculator5()
calc5.add(1,7)
calc5.rm(10,1)
print("Last result is ",calc5.last_result)

