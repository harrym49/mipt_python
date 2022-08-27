#Draw a "flower" from circles.

import turtle

turtle.shape('turtle')

angle = 360/6

for i in range(6):
    turtle.right(angle)
    turtle.circle(radius=50)
turtle.done()

