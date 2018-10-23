#classmethods

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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        name, surname, pay = emp_str.split('-')
        return cls(name, surname, pay)

    @staticmethod
    def work_day(day):
        if day.weekday() == 5 or day.weekday() == 6: #in Python: Monday is 0 etc. so 5 is Saturday
            return False
        return True

em_11 = Employee2("Marta","Frak",5000)
em_22 = Employee2("Tom","Example",4000)

print(Employee2.raise_amount)
print(em_11.raise_amount)
print(em_22.raise_amount)

Employee2.set_raise_amt(1.02) #we change amount in class (it change in all objects)

print(Employee2.raise_amount)
print(em_11.raise_amount)
print(em_22.raise_amount)

#!!!

emp_str_1 = 'Marta-Frak-4000'
emp_str_2 = 'Dona-Carmen-2000'

name, surname, pay = emp_str_1.split('-')

new_emp_1 = Employee2(name, surname, pay)
print(new_emp_1.name, new_emp_1.surname,new_emp_1.pay) #it is working!

new_emp_2 = Employee2.from_string(emp_str_2) #use classmethod
print(new_emp_2.name, new_emp_2.surname,new_emp_2.pay)


#check static method (work day)
import datetime

date = datetime.date(2018, 10, 23)
print(Employee2.work_day(date)) #true

date = datetime.date(2018, 10, 27)
print(Employee2.work_day(date)) #false
