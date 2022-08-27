# Draw two stars: one with 5 vertices, the other with 11.

import turtle
from lab_1.exercise_11 import pos

turtle.shape('turtle')

n = int(input("Enter n vertices "))
line = int(input("Enter line length, 150 for ex. "))
turtle.color("red")

angle = 360/n
pos(-100, 0)

minus = False

for i in range(n):
    if minus:
        turtle.forward(-line)
        turtle.left(angle/2)
        minus = False
        continue
    turtle.forward(line)
    turtle.left(angle/2)
    minus = True

turtle.done()