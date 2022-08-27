# Draw 10 nested squares.

import turtle

turtle.shape('turtle')

times = 0
x = 0
y = 0
distance = 50

def square(x, y, distance, times):
    if times == 10:
        turtle.done()
    turtle.setposition(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(distance)
        turtle.left(90)
    turtle.penup()
    x -= 10
    y -= 10
    distance += 20
    times += 1
    square(x, y, distance, times)

square(x, y, distance, times)