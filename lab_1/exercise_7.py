# Draw 10 nested regular polygons. Use the function that draws a regular n-gon.

import turtle

turtle.shape('turtle')

rad = 10

for i in range(10):
    ink = rad*(i+1)
    turtle.circle(radius=ink, steps=(i+3))
    turtle.penup()
    turtle.setposition(0, -ink)
    turtle.pendown()