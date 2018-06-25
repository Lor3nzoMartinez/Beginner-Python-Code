import turtle


## GUI INTERFACE


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Makin Bacon")


## TURTLE TESS


tess = turtle.Turtle()
tess.color('blue')
tess.pensize(3)


#Functions

def begin(Turtle):
    Turtle.pu()
    Turtle.bk(400)
    Turtle.pd()


def MiniSquare (Turtle,h):
    Turtle.pd()
    for i in range(2):
        Turtle.fd(h/4)
        Turtle.lt(90)
        Turtle.fd(h/4)
        Turtle.lt(90)

def Row (Turtle,h):
    Turtle.pu()
    Turtle.fd(h/2)
    turtle.pd()

def MakeRow (Turtle, h, r):
    for i in range (r):
        MiniSquare(Turtle, h)
        Row (Turtle,h)
    Turtle.pu()
    Turtle.lt(90)
    Turtle.fd(h/3)
    Turtle.pd()
    for i in range (r):
        MiniSquare(Turtle, h)
        Row(Turtle, h)
    Turtle.pu()
    Turtle.lt(90)
    Turtle.fd(h/3)
    Turtle.pd()


def MakeSquare (Turtle, h, r):
    MakeRow(Turtle, h, r)
    MakeRow(Turtle, h, r)
    
def Rows (Turtle, h, r):
    Turtle.speed(0)
    begin(tess)
    for i in range(5):
        MakeSquare (Turtle, h, r)
        Turtle.pu()
        Turtle.fd(h*4.5)
        Turtle.pd()
        
##Execution

Rows (tess, 40, 5)

## ETC.


wn.mainloop()
