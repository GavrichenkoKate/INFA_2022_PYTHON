
import numpy as np
import turtle 

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(6)

def one(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x,y+a)
    turtle.pendown()
    turtle.goto(x+a,y+2*a)
    turtle.goto(x+a,y)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()  

def two(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x,y+2*a)
    turtle.pendown()
    turtle.goto(x+a, y+2*a)
    turtle.goto(x+a, y+a)
    turtle.goto(x, y)
    turtle.goto(x+a, y)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()  
    
def three(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x,y+2*a)
    turtle.pendown()
    turtle.goto(x+a, y+2*a)   
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.goto(x, y)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()

def four(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x, y+2*a)    
    turtle.pendown()
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.goto(x+a, y+2*a)
    turtle.goto(x+2*a, y)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()  
    
def five(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x+a, y+2*a)    
    turtle.pendown()
    turtle.goto(x, y+2*a)
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.goto(x+a, y)
    turtle.goto(x, y)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()  
        
def six(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x+a, y+2*a)    
    turtle.pendown()
    turtle.goto(x, y+a)
    turtle.goto(x, y)
    turtle.goto(x+a, y)
    turtle.goto(x+a, y+a)
    turtle.goto(x, y+a)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()  

def seven(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x, y+2*a)
    turtle.pendown()
    turtle.goto(x+a, y+2*a)
    turtle.goto(x, y+a)
    turtle.goto(x, y)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()
    
def eight(a):
    x, y = turtle.position()
    turtle.goto(x, y+2*a)    
    turtle.goto(x+a, y+2*a)  
    turtle.goto(x+a, y)
    turtle.goto(x, y)
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()      

def zero(a):
    x, y = turtle.position()
    turtle.goto(x, y+2*a)    
    turtle.goto(x+a, y+2*a)  
    turtle.goto(x+a, y)
    turtle.goto(x, y)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown()  
    
def nine(a):
    x, y = turtle.position()
    turtle.goto(x+a, y+a)
    turtle.goto(x+a, y+2*a)
    turtle.goto(x, y+2*a)
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.penup()
    turtle.goto(x+2*a, y)
    turtle.pendown() 

with open('C:\\Users\\Asus\\infa_2021_gavrichenko\\Lab_3\\ex_3_txt.txt') as f:
    s = f.read()
    
a = 30 
q = {0: 'zero(a)', 1: 'one(a)', 2: 'two(a)', 3: 'three(a)', 4: 'four(a)', 5: 'five(a)', 6: 'six(a)', 7: 'seven(a)', 8: 'eight(a)', 9: 'nine(a)'} 
turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()    

for x in s:
    print(eval(q[int(x)]))
    
        
