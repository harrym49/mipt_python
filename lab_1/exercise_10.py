#Draw a spring.

import turtle

turtle.shape('turtle')

turtle.penup()
turtle.setposition(-300, 0)
turtle.pendown()

for i in range(7):
    turtle.left(90)
    turtle.circle(radius=-50, extent=180)
    turtle.circle(radius=-10, extent=180)
    turtle.right(90)

turtle.done()
