import turtle

## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Makin Bacon")


## TURTLE TESS

tess = turtle.Turtle()
tess.color('pink')
tess.pensize(3)


#Functions

def recenter (Turtle,h):
    Turtle.pu()
    Turtle.fd(h)
    Turtle.pd()

def star (Turtle, h):
    Turtle.lt(75)
    Turtle.fd(h)
    Turtle.lt(-150)
    Turtle.fd(h)
    Turtle.lt(210)
    Turtle.fd(h)
    Turtle.lt(225)
    Turtle.fd(h)
    Turtle.lt(-140)
    Turtle.fd(h+10)

    

##Execution

star(tess,100)


## ETC.
wn.mainloop()
