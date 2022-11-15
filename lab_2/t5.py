import turtle
turtle.shape('turtle')

for x in range(20, 201, 10):
    turtle.forward(x)
    turtle.setheading(90)
    turtle.forward(x)
    turtle.setheading(180)
    turtle.forward(x)
    
    turtle.setheading(270)
    
    turtle.forward(x)
    turtle.penup()
    turtle.forward(5)
    turtle.setheading(180)
    turtle.forward(5)
    turtle.setheading(0)
    turtle.pendown()