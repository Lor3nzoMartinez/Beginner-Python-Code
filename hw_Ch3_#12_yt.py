
#Youtube Link: https://youtu.be/muxMWF4QBG4

import turtle

# GUI INTERFACE

# Functions


def make_window(colr,ttle):
    wn = turtle.Screen()
    wn.bgcolor(colr)
    wn.title(ttle)


def make_turtle (colr, sz, name):
    (name)=turtle.Turtle
    turtle.color(colr)
    turtle.pensize(sz)
    turtle.shape("turtle")
    return turtle


def make_line (turtle):
    turtle.pu()
    turtle.fd(100)
    turtle.pd()
    turtle.fd(10)
    turtle.pu()
    turtle.fd(15)

    
# Make Window


make_window('pink','Makin bacon')


# Variable Values


n=30


# Loop

for i in range(12):
    make_turtle('blue', 3, 'turtle')
    turtle.lt(n)
    make_line(turtle)
    turtle.stamp()
    turtle.fd(-125)
    

    
# Execution


#ETC.


#wn.mainloop()
