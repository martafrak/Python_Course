#convert celsius to kelvin

#how to add exception

class TooColdException(Exception):
    pass #pass do nothing
    def __init__(self,temp):
        super().__init__("Temperature {} is below absolute zero".format(temp))

temp = int(input("Temperature [C]: "))
def cel_to_kelvin(temp):
    if temp < -273.15:
        raise TooColdException(temp)
    return temp + 273.15

print("Temperature: ",cel_to_kelvin(temp),"K")

'''
How to catch Exception

try:
    print("Temperature: ",cel_to_kelvin(temp),"K")
except TooColdException:
    print("Temperature is below absolute zero")
'''