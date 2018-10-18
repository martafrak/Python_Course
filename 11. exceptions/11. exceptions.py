#1.
try:
    file = open("text.txt","r+")
    file.write("Hello World")
    file.close()
except FileNotFoundError as E:
    print("FileNotFoundError")
    print(E)
print("still working")

'''
if we don't use exceptions:
file = open("text.txt","r+")
FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
'''

#2.
try:
    file2 = open("test.txt","r") #we only can read file
    file2.write("Hello World")
    file2.close()
except:
    print("error")
'''
file2.write("Hello World")
io.UnsupportedOperation: not writable
'''

#3.

while True:
    try:
        number = int(input("Your number = "))
        number = 100/number
        print(number," is your new number")
        break
    except ValueError:
        print("It is not number")
    except ZeroDivisionError:
        print("you don't choose 0")
    finally:
        print("Done")
'''
If we add for example "fff" as number:
ValueError: invalid literal for int() with base 10: 'fff'
'''