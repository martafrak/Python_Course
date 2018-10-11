#while exercise
#1. exercise

print("Start")
i = 0
while i <= 20:
    i += 1
    print(i)
else:
    print("End")

#2. exercise

S = 0
while S <=30:
    x = input("x = ")
    a = int(x) #string -> int
    S += a
    print(S)

#3. exercise - K!
K = input("K = ")
x = 1
i = int(K)
while i > 1:
    x = x * i
    i = i - 1
    print(x)
else:
    print("Factorial is ",x)