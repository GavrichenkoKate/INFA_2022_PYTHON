from random import randint
import turtle

# клетка
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
for i in range(4):
    turtle.forward(400)
    turtle.left(90)


number_of_turtles = 20   # количество черепашек
steps_of_time_number = 200    # количество смещений


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]  # черепашки
angle = []

for unit in pool:
    unit.penup()
    unit.speed(60)
    unit.goto(randint(-195, 195), randint(-195, 195)) # рандомное начальное положение
    left = randint(0, 360)        # рандомный начальный угол движения
    unit.setheading(left)     # поворот на этот угол
    angle.append(left)      # список всег нач. углов


for i in range(steps_of_time_number):
    for unit in pool:
        
        unit.forward(4)   
        ind = pool.index(unit)   # индекс данной черепашки в общем списке
        
        # отражение от стенок
        if unit.pos()[0] <= - 195:
            unit.setheading(360 + 180 - angle[ind])
            angle[ind] = 360 + 180 - angle[ind]
            
        if unit.pos()[0] >= 195:
            unit.setheading(360 + 180 - angle[ind])
            angle[ind] = 360 + 180 - angle[ind]
            
        if unit.pos()[1] >= 195:
            unit.setheading(360 - angle[ind])
            angle[ind] = 360 - angle[ind]
            
        if unit.pos()[1] <= -195:
            unit.setheading(360 - angle[ind])
            angle[ind] = 360 - angle[ind]       
