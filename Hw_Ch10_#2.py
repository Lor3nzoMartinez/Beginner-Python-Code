import turtle
import math


## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Project J")

## TURTLE TED

ted = turtle.Turtle()
ted.color('green')
ted.pensize(0)

tess = turtle.Turtle()
tess.color('orange')
tess.pensize(0)

sett = turtle.Turtle()
sett.color('red')
sett.pensize(0)

#Screen Facts

'''
Resolution = 795,945
Top right corner = 470,400
Top left corner = -475,400
Bot right corner = 470,-395
Bot left corner = -475,-395

'''

#Variable


#Functions

def draw_housing(Turtle):
    ''' Draw a nice housing that holds the traffic light'''
    Turtle.pensize(3)
    Turtle.color("black", "darkgrey")
    Turtle.begin_fill()
    Turtle.forward(80)
    Turtle.left(90)
    Turtle.forward(200)
    Turtle.circle(40, 180)
    Turtle.forward(200)
    Turtle.left(90)
    Turtle.end_fill()
    Turtle.penup()

'''
def orange_light(Turtle):
    Turtle.forward(70)
    Turtle.fillcolor("orange")

def red_light(Turtle):
    Turtle.forward(70)
    Turtle.fillcolor("red")

def green_light(Turtle):
    Turtle.back(140)
    Turtle.fillcolor("green")

def circle(Turtle):  
    ted.penup()
    ted.forward(40)
    ted.left(90)
    ted.forward(50)
    ted.shape("circle")
    ted.shapesize(3)
'''

def circle(Turtle):  
    Turtle.forward(40)
    Turtle.left(90)
    Turtle.forward(50)
    Turtle.begin_fill()
    Turtle.shape('circle')
    Turtle.shapesize(3)
    Turtle.end_fill()

def circle1(Turtle):
    Turtle.forward(40)
    Turtle.lt(90)
    Turtle.fd(120)
    Turtle.begin_fill()
    Turtle.shape('circle')
    Turtle.shapesize(3)
    Turtle.end_fill()

def circle2(Turtle):
    Turtle.forward(40)
    Turtle.lt(90)
    Turtle.fd(190)
    Turtle.begin_fill()
    Turtle.shape('circle')
    Turtle.shapesize(3)
    Turtle.end_fill()

#Execution

draw_housing(ted)

ted.color('green')




## ETC.

wn.ontimer(circle(ted), 5000)

wn.ontimer(circle1(tess), 1000)

wn.mainloop()
