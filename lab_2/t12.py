import turtle
turtle.shape('turtle')

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)

def half_circle(n):
    for i in range(50):
        turtle.right(180 / 50)  # R = n*50 / pi
        turtle.forward(n)


for i in range(3):
        half_circle(4)
        half_circle(1)