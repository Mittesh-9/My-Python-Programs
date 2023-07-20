from turtle import *
from math import *

A = 50
B = 100
C = 0
D = 0

penup()
for x in range(-200, 200):
    # Sine wave equation
    y = A * sin((2 * pi / B) * (x + C)) + D
    goto(x, y)
    pendown()

hideturtle()
mainloop()