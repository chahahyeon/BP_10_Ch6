#7번 문제

import turtle

t=turtle.Turtle()
t.shape("turtle")
t.left(90)

for i in range(1,7):
    t.forward(100)
    t.forward(-30)
    t.left(60)
    t.forward(30)
    t.forward(-30)
    t.right(120)
    t.forward(30)
    t.forward(-30)
    t.left(60)
    t.forward(-70)
    t.left(60)
    
    
#8번 문제    

import turtle

myPen=turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

for j in range (1,10):
    for i in range (1,6):
        myPen.left(144)
        myPen.forward(200)
    myPen.left(10)
    
    
#9번 문제

import turtle
import random

t=turtle.Turtle()
t.shape("turtle")

for j in range (1,10):
    t.up()
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    r=random.randint(10,200)
    t.goto(x,y)
    t.down()
    t.circle(r)
    
    
 #10번 문제   

import turtle

t=turtle.Turtle()
t.shape("turtle")

for i in range(5):
    t.forward(200);
    t.right(90)
    t.forward(20);
    t.right(90)
    t.forward(200);
    t.left(90)
    t.forward(20);
    t.left(90)
    
    
#11번 문제    

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color('red','yellow')
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()


#12번 문제

import turtle
import math

t=turtle.Turtle()
t.shape("turtle")
t.color('red','yellow')

for x in  range(0,360):
      t.goto(x,200*math.sin(x*3.14/100))
