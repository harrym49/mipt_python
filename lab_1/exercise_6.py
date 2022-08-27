#Draw a "square" spiral.

import turtle

turtle.shape('turtle')

length = 10

while length < 500:
    turtle.forward(length)
    turtle.left(90)
    length += 10



