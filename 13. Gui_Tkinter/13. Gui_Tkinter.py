from tkinter import *

#1. example  create label and button
text = input("Text = ")
window = Tk()

topframe = Frame(window)
topframe.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)

button1 = Button(topframe,text="Button 1",fg = "pink")
button2 = Button(topframe,text="Button 2",fg = "red")
button3 = Button(bottomframe,text="Button 3",fg = "yellow")
button4 = Button(bottomframe,text="Button 4",fg = "blue")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = RIGHT)
button4.pack()

label = Label(window,text = text)
label.pack() #automatic size


window.mainloop() #run

#2. example - FILL

window2 = Tk()

label1 = Label(window2,text= "Label 1", bg = "green")
label2 = Label(window2,text= "Label 2", bg = "pink")
label3 = Label(window2,text= "Label 3", bg = "blue")
label4 = Label(window2,text= "Label 4", bg = "red")

label1.pack()
label2.pack(fill = X)
label3.pack()
label4.pack(side = LEFT,fill = Y) #if we want to use fill=Y, we have to define side (left or right)

window2.mainloop()

#3. example form - GRID

window3 = Tk()

label5 = Label(window3,text="name")
label6 = Label(window3,text="surname")
entry5 = Entry(window3) #place to input text
entry6 = Entry(window3)

#where we want lables and entries?

label5.grid(row=0,sticky=E)
label6.grid(row=1,sticky=E)

entry5.grid(row=0,column=1)
entry6.grid(row=1,column=1)

check = Checkbutton(window3,text="click here")
check.grid(columnspan=2)

window3.mainloop()

#4. example

window4 = Tk()

def printer():
    print("Hello World - from hello_button")

def printer2(event):
    print("Hello World - from hello_button2")

hello_button = Button(window4,text="Click here!",command=printer)
hello_button.pack()

hello_button2 = Button(window4,text="Click here!")
hello_button2.bind("<Button-1>",printer2)
hello_button2.pack()

window4.mainloop()



#5. example

window5 = Tk()

def left(event):
    print("Left click")
    print(event.x, event.y) #add coordinates

def right(event):
    print("Right click")

def center(event):
    print("center")

frame5 = Frame(window5, width=500, height=450)
frame5.bind("<Button-1>",left)
frame5.bind("<Button-3>",right)
frame5.bind("<Button-2>",center)

frame5.pack()

window5.mainloop()