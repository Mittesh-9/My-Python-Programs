# Exercise 2 CWH (Good Morning Sir)

# Morning 00 to 12
# Afternoon 12 to 18
# Evening 18 to 20
# Night 20 to 00

import time
timestamp = time.strftime('%H:%M:%S')

a = int(time.strftime('%H'))

b = (input("What's your name?\n"))

if (a>0 and a<12):
    print("Good Morning", b)
elif(a>12 and a<18):
    print("Good Afternoon", b)
elif(a>18 and a<20):
    print("Good Evening", b)
else:
    print("It's time to sleep",b)
    print("Good Night")