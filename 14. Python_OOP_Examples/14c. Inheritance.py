#Inheritance (subclasses)

class Employee:

    raise_amt = 1.2

    def __init__(self,name,surname,pay):
        self.name = name
        self.surname = surname
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.name,self.surname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Emp1(Employee):
    raise_amt = 1.8 #it is more important than variable from parent's class

    def __init__(self, name, surname, pay, language):
        super().__init__(name, surname, pay)
        self.language = language

class Emp2(Employee):
    def __init__(self, name, surname, pay, employees = None):
        super().__init__(name, surname, pay)
        if Employees is None:
            self.employees = []
        else:
            self.employees = employees


em_1 = Employee("Marta","Frak",2000)
em_2 = Employee("Tom","Example",3000)

print(em_1.name,em_1.surname,em_1.pay)
print(em_2.name,em_2.surname,em_2.pay)


em_3 = Emp1("Dona","Carmen",5000, "polish")
em_4 = Emp1("Anastasia","Example",1000, "english")

print(em_3.name,em_3.surname,em_3.pay, em_3.language)
print(em_4.name,em_4.surname,em_4.pay, em_4.language)

print("Salary - em_3:")
print(em_3.pay)
em_3.apply_raise()
print(em_3.pay)


#print(help(Emp1)) #if we need help and more information about class