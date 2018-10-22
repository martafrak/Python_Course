#class variables


class Employee2:

    num_of_emps = 0
    raise_amount = 1.2  #class variable

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay

        Employee2.num_of_emps += 1 #new employee will be add

    def fullname(self):
        return "{} {}".format(self.name,self.surname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

em_11 = Employee2("Marta","Frak",5000)
em_22 = Employee2("Tom","Example",4000)

print(Employee2.raise_amount)
print(em_11.raise_amount)
print(em_22.raise_amount)

#differences
print(em_11.__dict__)
print(Employee2.__dict__)

#we can change variable for only for 1 instance

em_11.raise_amount = 2

print(Employee2.raise_amount)
print(em_11.raise_amount)
print(em_22.raise_amount)


#Employee in company
print("Employee:",Employee2.num_of_emps)
em_33 = Employee2("Edward","Example",7000)
print("Employee:",Employee2.num_of_emps)