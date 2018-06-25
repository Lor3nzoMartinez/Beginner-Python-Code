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

for x in [160,-43, 270, -97, -43, 200, -940, 17, -86]:
    tess.lt (x)
    tess.fd(100)
    

##Execution




## ETC.
wn.mainloop()
