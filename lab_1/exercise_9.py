# Draw a "butterfly" from circles.

import turtle

turtle.shape('turtle')
r = 50

for i in range(10):
    turtle.right(90)
    turtle.circle(r)
    turtle.circle(-r)
    r += 10
    turtle.home()

turtle.done()