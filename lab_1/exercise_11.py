# Draw a smiley.

import turtle

turtle.shape('turtle')

def eye(r, color):
    turtle.begin_fill()
    turtle.fillcolor(f'{color}')
    turtle.circle(r)
    turtle.end_fill()

def pos(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()

if __name__ == "__main__":
    eye(150, 'yellow')
    pos(-60, 210)
    eye(20, 'blue')
    pos(60, 210)
    eye(20, 'blue')
    pos(0, 205)

    turtle.pencolor('navy')
    turtle.pensize(10)
    turtle.right(90)
    turtle.forward(90)

    pos(80, 100)

    turtle.pencolor('red')
    turtle.circle(-80, extent=180)

    turtle.done()
