import turtle
turtle.shape('turtle')

n = 12
for i in range(1, n + 1):
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.setheading(i * (360 / n))