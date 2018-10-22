#simple classes and instances

class Employee:
    pass #pass do nothing

#instances: em_1 and em_2 - have different location in memory

em_1 = Employee()
em_2 = Employee()
print(em_1)
print(em_2)

#instances variables

em_1.name = "Marta"
em_1.surname = "Frak"
em_1.age = 24

em_2.name = "Jennifer"
em_2.surname = "Example"
em_2.age = 21

print(em_1.name,em_2.name)

#how to use constructor
#if we want automatic create Employee objects

class Employee2:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def fullname(self):
        return "{} {}".format(self.name,self.surname)

em_11 = Employee2("Marta","Frak","24")
em_22 = Employee2("Tom","Example","33")
print(em_11)
print(em_22)
print(em_11.surname,em_22.surname)

print(em_11.fullname())
print(em_22.fullname())