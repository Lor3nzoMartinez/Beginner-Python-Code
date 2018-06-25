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

def center (Turtle, h):
#I will use this funtion to recenter and prep my turtle for it's next action
        Turtle.pu()
        Turtle.fd(h+50)
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

    

##Execution

Make_row(tess,20,5)


## ETC.
wn.mainloop()
