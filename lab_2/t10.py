import turtle
turtle.shape('turtle')
turtle.speed(15)

k = 2
def circle(n):
    for i in range(50):
        turtle.forward(n)
        turtle.left(360 / 50)

for i in range(k):
    circle(6)
    turtle.left(180)
    circle(6)
    turtle.left(360 / (2 * k))