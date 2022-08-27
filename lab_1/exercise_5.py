# Draw a spider with n paws.

import turtle

n = int(input())
angle = 360/n
final_angle = angle

turtle.shape('turtle')

while True:
    if final_angle > 360:
        turtle.done()
    turtle.right(angle=final_angle)
    turtle.forward(100)
    turtle.stamp()
    turtle.home()
    final_angle += angle