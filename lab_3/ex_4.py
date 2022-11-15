
import turtle 
turtle.shape('turtle')

dt = 0.1

Vx = 50
Vy = 70

x = -350
y = 0

ay = -10
ax = 0
k = 0.1

turtle.goto(350,0)
for i in range(10000):
    turtle.goto(x, y)
    x += Vx*dt + ax*dt**2
    y += Vy*dt + ay*dt**2
    
    ay = -10 - Vy*k
    ax = -Vx*k
    
    Vy += ay*dt
    Vx += ax*dt
    
    if y < 0:
        Vy = -Vy
        
        
        