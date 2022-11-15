import turtle
turtle.shape('turtle')

a = 20
d = 5
for i in range(5):
    turtle.forward(a + d * 2*i)
    turtle.left(90)
    turtle.forward(a + d * 2*i)
    turtle.left(90)
    turtle.forward(a + d * (2*i + 1))
    turtle.left(90)
    turtle.forward(a + d * (2*i + 1))
    turtle.left(90)