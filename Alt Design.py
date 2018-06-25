
#Youtube:        https://youtu.be/gaJnonPzbss

import turtle



## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("lightgrey")
wn.title("Makin Bacon")


## TURTLEs

'''I will use to make most of background'''
bagrou = turtle.Turtle()
bagrou.color('pink')
bagrou.pensize(3)


'''I will use to make most of the design'''
fogrou = turtle.Turtle()
fogrou.color('lightblue')
fogrou.pensize(3)


'''The turtle i will use if i need to complete my design or to help out'''
extr = turtle.Turtle()
extr.color('white')
extr.pensize(1)

#Screen Facts

'''
Resolution = 795,945
Top right corner = 470,400
Top left corner = -475,400
Bot right corner = 470,-395
Bot left corner = -475,-395

'''

#Variable
a = 0


#Functions


def set_corner(Turtle, x, y):
    Turtle.pu()
    Turtle.setpos(x,y)
    Turtle.pd()

def ultimate_sqaure_white(Turtle):
    Turtle.begin_fill()
    Turtle.fillcolor('black')
    for i in range(4):
        Turtle.lt(90)
        Turtle.fd(50)
    Turtle.end_fill()
    for i in range(1):
        Turtle.begin_fill()
        Turtle.fillcolor('white')
        Turtle.color('white')
        Turtle.lt(135)
        Turtle.fd(35)
        Turtle.lt(90)
        Turtle.fd(35)
        Turtle.lt(135)
        Turtle.fd(50)
        Turtle.end_fill()
        Turtle.lt(135)
        Turtle.fd(70)
        Turtle.rt(135)
        Turtle.begin_fill()
        Turtle.fillcolor('white')
        Turtle.fd(50)
        Turtle.lt(-135)
        Turtle.fd(35)
        Turtle.lt(90)
        Turtle.fd(35)
        Turtle.lt(135)
        Turtle.end_fill()
        Turtle.fd(50)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.lt(180)
    Turtle.fd(49)

def ultimate_sqaure_black(Turtle):
    Turtle.begin_fill()
    Turtle.fillcolor('white')
    for i in range(4):
        Turtle.lt(90)
        Turtle.fd(50)
    Turtle.end_fill()
    for i in range(1):
        Turtle.begin_fill()
        Turtle.fillcolor('black')
        Turtle.color('black')
        Turtle.lt(135)
        Turtle.fd(35)
        Turtle.lt(90)
        Turtle.fd(35)
        Turtle.lt(135)
        Turtle.fd(50)
        Turtle.end_fill()
        Turtle.lt(135)
        Turtle.fd(70)
        Turtle.rt(135)
        Turtle.begin_fill()
        Turtle.fillcolor('black')
        Turtle.fd(50)
        Turtle.lt(-135)
        Turtle.fd(35)
        Turtle.lt(90)
        Turtle.fd(35)
        Turtle.lt(135)
        Turtle.end_fill()
        Turtle.fd(50)
    Turtle.lt(90)
    Turtle.fd(50)
    Turtle.lt(180)
    Turtle.fd(49)
       
def row (Turtle, x, y):
    set_corner(Turtle, x, y)
    Turtle.speed(0)
    for i in range (8):
        ultimate_sqaure_white(extr)
        ultimate_sqaure_black (extr)

def row2 (Turtle, x, y):
    set_corner(Turtle, x, y)
    Turtle.speed(0)
    for i in range (8):
        ultimate_sqaure_black(extr)
        ultimate_sqaure_white(extr)


def finish (Turtle, x, y):
    for i in range (10):
        row(Turtle, x, y)
        row2(Turtle, x + 50, y)
        x = x + 100


##Execution       

finish (extr, -475, -395)

#ultimate_sqaure_white(extr)

## ETC.
wn.mainloop()
