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
extr.color('black')
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



#Functions
'''
def cross(Turtle, width):
    Turtle.begin_fill()
    Turtle.fillcolor('lightblue')
    for i in range(4):
        Turtle.rt(-90)
        Turtle.fd(width)
        Turtle.rt(90)
        Turtle.fd(width)
        Turtle.rt(90)
        Turtle.fd(width)
    Turtle.end_fill()
    Turtle.pu()
    Turtle.fd(width/2)
    Turtle.rt(90)
    Turtle.fd(width/2)
    Turtle.rt(-90)
    Turtle.pd()
'''

def petal(Turtle, width):
    Turtle.rt(-90)
    Turtle.fd(width)
    Turtle.rt(90)
    Turtle.fd(width)
    Turtle.rt(90)
    Turtle.fd(width)

def cross(Turtle, width,color):
    Turtle.begin_fill()
    Turtle.fillcolor(color)
    for i in range (4):
        petal(Turtle, width)
    Turtle.end_fill()
    center(Turtle, width)


def center(Turtle, width):
    Turtle.pu()
    Turtle.fd(width/2)
    Turtle.rt(90)
    Turtle.fd(width/2)
    Turtle.rt(-90)
    Turtle.pd()

def move(Turtle, width):
    Turtle.pu()
    Turtle.fd(width)
    Turtle.lt(90)
    Turtle.fd(width/2)
    Turtle.rt(90)
    Turtle.fd(width/2)
    Turtle.fd(width)
    Turtle.pd()

    
def line_of_crosses(Turtle, width, color, color2, cross_amt):
    for i in range (cross_amt):
        cross(Turtle, width, color)
        move(Turtle,width)
        color,color2 = color2, color
        
def move_down(Turtle, width):
    Turtle.pu()
    Turtle.rt(90)
    Turtle.fd(width*3)
    Turtle.rt(90)
    Turtle.fd(width/2)
    Turtle.rt(180)
    Turtle.pd()
    
def line_reset(Turtle, width):
    Turtle.pu()
    Turtle.bk(width*11.5)
    Turtle.pd()


def array_of_crosses(Turtle,width,color,color2,cross_amt,row_amt):
     for i in range (row_amt):
         line_of_crosses(Turtle, width, color, color2, cross_amt)
         line_reset(Turtle,width)
         move_down(Turtle,width)
         
##Execution       


array_of_crosses(extr, 25, 'lightblue','green',4,5)


## ETC.
wn.mainloop()
