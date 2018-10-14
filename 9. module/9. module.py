#module

#1. exercise: a) create hello.py -> function hello()
#b) import hello.py
#c) use function hello() in this file

import hello

text = input("Your text: ")
text2 = input("Your new text: ")
hello.hello(text)
hello.newfunction(text2)

#if we need only 1 function from module, we can import only this function
from hello import newfunction
newfunction(text2)

#if we want to use shorter form we can import all (*) from module
from hello import *
hello(text) #we can't use module's name (hello.hello() etc.)
newfunction(text2)

#if we have 2 function (the same name):
from hello import hello as hello_hello
text3 = input("Text3 = ")
def hello(text3):
    print(text3)

hello(text3)
hello_hello(text)

#module builtins
import math
print(math.cos(60))

import random
x = random.randrange(1,100)
print(x) #print random number