import turtle
turtle.shape('turtle')
import math

r0 = 20

def polygon(n, R):
    turtle.left(90 * (n + 2) / n)  
    
    for i in range(n):
        turtle.forward(2 * R * math.sin(math.pi / n))
        turtle.left(180 - (180 * (n - 2)) / n)
        
    turtle.right(90 * (n + 2) / n)
    
for i in range(1, 10):
    polygon(i + 2, r0 * (i))
    turtle.penup()
    turtle.forward(r0)
    turtle.pendown()