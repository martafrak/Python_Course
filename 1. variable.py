#variable - python

variable = "Hello World!"
print(variable)

#VARIABLE TYPES
#int
a = 10

#float
x = 2.4

#boolean
z = True
y = False

#string
variable = "Hello World!"

#how to check variable type
print(type(variable))
print(type(z))
print(type(x))
print(type(a))

#new line
line = "first line\nsecond line"
print(line)

#result is float
result = x + a
print(type(result))

#we can add string
text = variable + " Yoo!"
print(text)

#input
x = input("Write something: ")
print(x)
print(type(x))
#input is always string so we can change type
#int(x) or float(x) etc.
x=int(x)
print(type(x))

#round method
x = 3.45676543234567543
x = (round(x,3))
print(x)

#string
text = "Hello sweetie! How are you?"
x = text[0]
print(x) #print first char
#we can choose some char
x = text[0:4]
print(x)
x = text[5:]
print(x)
x = text [-5:]
print(x)

text = "marta"
print(text.capitalize())
print(text.count("a"))

#LISTS (where cat is 0, dog is 1, fish is 2 etc.)
list = ["cat", "dog", "fish", "donkey"]
print(list[2]) #we choose second element
(print(type(list))) #variables types (list)
print(len(list))
list.append("chicken") #we use function
print(list)
print(list[1:3])
#how to delete from list
list.__delitem__(1) #delete "dog" 'cause is 1 on the list (cat is 0)
print(list)
list.remove("cat") #deleted name
print(list)
chicken = list.count("chicken") #how many chickens are in the list
print(chicken)
list.extend(["cat","cat"]) #added more elements
print(list)
new_list = ["mouse", "horse"]
list.extend(new_list) #added new list
print(list)
list.insert(1,"turtle") #added element - position 1
print(list)
list.pop(0) #deleted position 0
print(list)
list.clear() #deleted all elements from list
print(list) #empty


#TUPLE (we can not edit, we can not use function)
animals = ("cat", "dog", "fish", "donkey")
print(animals)
print(type(animals))


#dictionary (we use keys and we can use functions)
person = {"years": 25, "name": "Marta"}
print(person)
print(type(person)) #dict

print(person["name"]) #we choose want we want to see (key)