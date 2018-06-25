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

def set_cord(Turtle, x,y):
    Turtle.pu()
    Turtle.goto(x,y)
    Turtle.pd()

def border (Turtle, width):
    Turtle.fd(width)
    Turtle.rt(120)
    Turtle.fd(width*2)
    Turtle.rt(150)
    Turtle.fd(width*1.73)
    Turtle.rt(90)

def triangle (Turtle, width):
    Turtle.speed(0)
    for i in range (3):
        Turtle.fd(width)
        Turtle.lt(120)
    Turtle.pu()
    Turtle.fd(10)
    Turtle.rt(-90)
    Turtle.fd(5)
    Turtle.rt(90)
    Turtle.pd()
    
def design (Turtle, width, color, color2):
    for i in range (12):
        Turtle.begin_fill()
        Turtle.fillcolor(color)
        triangle (Turtle,width)
        width = width - 20
        Turtle.end_fill()
        color, color2 = color2, color

def move (Turtle, width):
    Turtle.pu()
    Turtle.fd(5)
    Turtle.lt(90)
    Turtle.fd(width/1.59)
    Turtle.rt(150)
    Turtle.pd()

def full(Turtle, width, color, color2):
    for i in range (6):
        design(Turtle, width, color, color2)
        move(Turtle,width)
    Turtle.fd(width*2)
            
##Execution
'''   
set_cord(extr, -475,-175)
full(extr, 250, 'orange', 'black')
full(extr, 250, 'orange', 'black')
set_cord(extr, -475, 260)
full(extr, 250, 'orange', 'black')
full(extr, 250, 'orange', 'black')
'''

border(extr, 250)

## ETC.
wn.mainloop()
