'''
write/read MODE:
r - reading
r+ - reading and writting, no truncate
w - writting, truncate, create file if it not exists
w+ - reading, writting, truncate, create file if it not exists
a - writting, no truncate, create file if it not exists
a + -reading, writting, create file if it not exists
'''


handler = open("file.txt",mode="a+")
handler.write("Hello\nWorld\n123")
handler.close()

handler2 = open("file.txt",mode="r")
print(handler2.read(5))
print(handler2.read(6))
handler2.seek(6)
print(handler2.read(6))
print(handler2.readline())
print(handler2.readlines()) #all file -> as list

#example use
for line in handler2.readlines():
    print(line,end="")

for line in handler2.readlines():
    print(line.rsttip())

handler.close()

