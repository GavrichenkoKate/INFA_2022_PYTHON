import turtle
turtle.shape('turtle')
import math

N = 8
k = 5

for i in range(301):
    phi = i * (2 * math.pi * N / 300)
    turtle.goto((k * phi * math.cos(phi)), (k * phi * math.sin(phi)))