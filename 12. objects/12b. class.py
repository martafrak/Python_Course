#1. example
class Parent():

    def __init__(self):
        print("Parent init")

    def dinner(self):
        print("dinner def")

    def example(self):
        print("example def")

class Child(Parent):

    def __init__(self):
        super().__init__()     #if we add this line, we use function from parent
        print("Child init")

    def example(self):
        print("example - child def")


tom = Parent()
tom.dinner()
tom.example()

tina = Child()
tina.example()
tina.dinner() #function from parent


#2. example

class Person():
    def __init__(self,name):
        self.name = name
        self.surname = "unknown"
        self.age = "18"

Carol = Person("Carol")
print(Carol.name,Carol.surname,Carol.age)

class Employee(Person):

    def __init__(self):
        super().__init__("unknown_employee")
        self.position = "doctor"
        self.specialization = "heart attack"

rachel = Employee()
print(rachel.name)
print(rachel.position)

class Client(Person):

    def __init__(self,order):
        super().__init__("unknown_client")
        self.order = order

agnes = Client("web site")
agnes.name = "Agnes"
print(agnes.name," - ",agnes.order)