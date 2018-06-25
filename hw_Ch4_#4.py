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

def center (Turtle,h):
#I will use this funtion to recenter and prep my turtle for it's next action
        Turtle.pu()
        Turtle.lt(45)
        Turtle.fd(h/2)
        Turtle.pd()
        
def square (Turtle,h):
#This function contains controls for making the square
    for i in range (2):
        Turtle.fd(h)
        Turtle.left(90)
        Turtle.fd(h)
        Turtle.left(90)
        
def Make_row (Turtle, h,r):
#This function is combining previous functions and instructions to
#manipulate the code so it does what I want.
    center(tess, -400)
    for r in range (r):
       square(Turtle,h)
       center(Turtle,h)
       h=20+h
       
def PrettyPattern (Turtle,h):
# I'm not gonna lie I figured this out on accident i was just messing with it for so
# long and it finally happened. I was also thinking it was two seperate designs.
# so I'm glad I figured it out.
    for i in range (24):
        square(Turtle, h)
        Turtle.rt(15)

##Execution

PrettyPattern(tess,100)


## ETC.
wn.mainloop()
