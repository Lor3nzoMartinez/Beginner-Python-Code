import turtle

#youtube link:  https://youtu.be/WVp7SeVjtRw

## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Makin Bacon")


## TURTLE TESS

tess = turtle.Turtle()
tess.color('pink')
tess.pensize(3)

#Functions

def Maze (Turtle,h):
    Turtle.pu()
    Turtle.fd(h*-50)
    Turtle.pd()
    for i in range (50):
        Turtle.rt(90)
        Turtle.fd(h)
        h=h+5

def Hypnotics (Turtle,h):
    Turtle.pu()
    Turtle.fd(h*100)
    Turtle.pd()
    for i in range (50):
        Turtle.rt(91)
        Turtle.fd(h)
        h=h+5

def Recenter(Turtle,h):
    Turtle.pu()
    Turtle.fd(h*-50/2)
    Turtle.rt(90)
    Turtle.fd(h*50/2)
    Turtle.rt(90)
    Turtle.pd()
    
def both (Turtle,h):
    Maze (Turtle,h)
    Recenter(Turtle,h)
    Hypnotics(Turtle,h)
    

##Execution


#Maze(tess,5)

#Hypnotics(tess,5)

both (tess,5)

## ETC.
wn.mainloop()
