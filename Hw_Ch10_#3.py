import turtle
import math


## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Project J")

## TURTLE TED

ted = turtle.Turtle()
ted.color('darkgrey')
ted.pensize(0)

tess = turtle.Turtle()
tess.color('black')
tess.pensize(0)

tom = turtle.Turtle()
tom.color('black')
tom.pensize(0)


#Screen Facts

'''
Resolution = 795,945
Top right corner = 470,400
Top left corner = -475,400
Bot right corner = 470,-395
Bot left corner = -475,-395

'''

#Variable

state_num = 0

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

def Greenlight(Turtle):
    Turtle.hideturtle()
    Turtle.pu()
    Turtle.shape("circle")
    Turtle.shapesize(3)
    Turtle.fillcolor('green')
    Turtle.fd(40)
    Turtle.lt(90)
    Turtle.fd(40)
    
    
def Orangelight(Turtle):
    Turtle.hideturtle()
    Turtle.pu()
    Turtle.shape("circle")
    Turtle.shapesize(3)
    Turtle.fillcolor('orange')
    Turtle.fd(40)
    Turtle.lt(90)
    Turtle.fd(120)
    

def Redlight(Turtle):
    Turtle.hideturtle()
    Turtle.pu()
    Turtle.shape("circle")
    Turtle.shapesize(3)
    Turtle.fillcolor('red')
    Turtle.fd(40)
    Turtle.lt(90)
    Turtle.fd(190)
    

#Execution

draw_housing(ted)

Greenlight(ted)

Orangelight(tess)

Redlight(tom)

## ETC.
wn.ontimer(ted.showturtle, 2000)
wn.ontimer(ted.hideturtle,4000)

wn.ontimer(tess.showturtle, 4100)
wn.ontimer(tess.hideturtle, 6100)

wn.ontimer(tom.showturtle, 6200)
wn.ontimer(tom.hideturtle, 8200)


wn.mainloop()
