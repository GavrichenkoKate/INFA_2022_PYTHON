import numpy as np
import turtle 

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(4)

def one(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x,y+a)
    turtle.pendown()
    turtle.goto(x+a,y+2*a)
    turtle.goto(x+a,y)

def two(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x,y+2*a)
    turtle.pendown()
    turtle.goto(x+a, y+2*a)
    turtle.goto(x+a, y+a)
    turtle.goto(x, y)
    turtle.goto(x+a, y)
    
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
    turtle.goto(x+a, y)
    turtle.pendown()

def four(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x, y+2*a)    
    turtle.pendown()
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.goto(x+a, y+2*a)
    turtle.goto(x+a, y)
    
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
    turtle.goto(x+a, y)
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
    turtle.goto(x+a, y)
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
    turtle.goto(x+a, y)
    turtle.pendown()
    
def eight(a):
    x, y = turtle.position()
    turtle.goto(x, y+2*a)    
    turtle.goto(x+a, y+2*a)  
    turtle.goto(x+a, y)
    turtle.goto(x, y)
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.goto(x+a, y)

def zero(a):
    x, y = turtle.position()
    turtle.goto(x, y+2*a)    
    turtle.goto(x+a, y+2*a)  
    turtle.goto(x+a, y)
    turtle.goto(x, y)
    turtle.goto(x+a, y)
    
def nine(a):
    x, y = turtle.position()
    turtle.goto(x+a, y+a)
    turtle.goto(x+a, y+2*a)
    turtle.goto(x, y+2*a)
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.penup()
    turtle.goto(x+a, y)
    turtle.pendown() 

def probel(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x+a, y)
    turtle.pendown()
         


turtle.penup()
turtle.goto(-300,0)
turtle.pendown()

a = 50
one(a)
probel(a)
four(a)
probel(a)
one(a)
probel(a)
seven(a)
probel(a)
zero(a)
probel(a)
zero(a)