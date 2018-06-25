
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

def triangle (Turtle, h):
    for i in range (1):
        h = h *2
        Turtle.fd(h)
        Turtle.lt(120)
        Turtle.fd(h)
        Turtle.lt(120)
        Turtle.fd(h)
        Turtle.lt(120)
        
def push (Turtle):
    Turtle.fd(7)

def crazy (Turtle, h):
    for i in range (10):
        triangle(Turtle,h)
        push(Turtle)
    
        
##Execution       

crazy(extr,50)

## ETC.
wn.mainloop()
