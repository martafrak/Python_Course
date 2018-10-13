import time
#date and time exercises

#1. exercise
print("Start")
time.sleep(2)
print("Stop")

#2. example (when we want to do a few things at the same time)

timer = time.time()
timer2 = time.time()
timer3 = time.time()
while True:
    if time.time()-timer > 3:
        print("3 seconds")
        timer = time.time()
    if time.time()-timer2 > 5:
        print("5 seconds")
        timer2 = time.time()
    if time.time()-timer3 > 10:
        print("10 second")
        timer3 = time.time()
        break

#3. Timer
seconds = int(input("x = "))
timer4 = time.time()
while True:
    if time.time() - timer4 > seconds:
        print("It's time! It was ",seconds," seconds!")
        timer4 = time.time()
        break

#4. Date and time (we have to import datetime)

import datetime

now = datetime.datetime.now()
print(now)
#we also choose what we want to print
print(now.day,"/",now.month,"/",now.year," and ",now.hour,":",now.minute)
#we also use strftime function
print(now.strftime("%H:%M %d/%m/%Y"))
print(now.strftime("%I:%M %p %d %b %Y"))
print(now.strftime("%I:%M %p %d %B %Y"))