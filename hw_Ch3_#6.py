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

#Loops

for i in range(3):
    tess.fd(40)
    tess.lt(120)

recenter(tess,45)

for i in range (4):
    tess.fd(40)
    tess.lt(90)

recenter(tess,65)

for i in range (6):
    tess.fd(40)
    tess.lt(60)

recenter(tess,95)

for i in range (8):
    tess.fd(40)
    tess.lt(45)

##Execution




## ETC.
wn.mainloop()
