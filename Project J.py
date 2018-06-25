import turtle
import math

## https://youtu.be/xTP-HVlM4ak

## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Makin Bacon")


## TURTLE TED

ted = turtle.Turtle()
ted.color('darkgrey')
ted.pensize(0)


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



def set_corner(Turtle, x, y):
#This function takes X and Y and tells the pointer where to go
    Turtle.pu()
    Turtle.setpos(x,y)
    Turtle.pd()

def Square(Turtle, C1, s):
#Makes a sqaure filled with a color
    Turtle.begin_fill()
    Turtle.fillcolor(C1)
    for i in range(4):
        Turtle.fd(s)
        Turtle.rt(90)
    Turtle.end_fill()
    Turtle.rt(90)
    Turtle.fd(s+1)
    Turtle.lt(90)

def Half_Square(Turtle, C1, C2, s):
#This function makes a square that is made out of right triangles
    #RT Tri 1
    d = s*math.sqrt(2)
    Turtle.begin_fill()
    Turtle.fillcolor(C1)
    Turtle.rt(45)
    Turtle.fd(d)
    Turtle.lt(135)
    Turtle.fd(s)
    Turtle.lt(90)
    Turtle.fd(s)
    Turtle.end_fill()
    #RT Tri 2
    Turtle.begin_fill()
    Turtle.fillcolor(C2)
    Turtle.lt(90)
    Turtle.fd(s)
    Turtle.lt(90)
    Turtle.fd(s)
    Turtle.lt(135)
    Turtle.fd(d)
    Turtle.end_fill()
    Turtle.lt(135)
    Turtle.fd(s+1)
    Turtle.lt(90)

def Half_Square_Flip(Turtle, C1, C2, s):
#This function makes a square that is made out of right triangles flipped over its self
    d=s*math.sqrt(2)
    #RT Tri  1
    Turtle.begin_fill()
    Turtle.fillcolor(C2)
    Turtle.fd(s)
    Turtle.rt(135)
    Turtle.fd(d)
    Turtle.rt(135)
    Turtle.fd(s)
    Turtle.end_fill()
    #RT Tri 2
    Turtle.begin_fill()
    Turtle.fillcolor(C1)
    Turtle.rt(90)
    Turtle.fd(s)
    Turtle.rt(135)
    Turtle.fd(d)
    Turtle.lt(135)
    Turtle.fd(s)
    Turtle.lt(90)
    Turtle.fd(s)
    Turtle.lt(135)
    Turtle.end_fill()
    Turtle.fd(d)
    Turtle.lt(45)
    Turtle.fd(1)
    Turtle.lt(90)




def row_1_1(Turtle, x, y, C1, C2, s):
#This will take the shapes above and start to put them in a design row by row
    Turtle.speed(0)
    set_corner(Turtle, x, y)
    Square(Turtle, C1, s)
    Half_Square(Turtle, C1, C2, s)
    Half_Square_Flip(Turtle, C1, C2, s)
    Square(Turtle, C1, s)

def row_1_2(Turtle, x, y, C1, C2, s):
    set_corner(Turtle, x+s, y)
    for i in range (2):
        Half_Square(Turtle, C1, C2, s)
        Half_Square_Flip(Turtle, C1, C2, s)

def row_1_3(Turtle, x, y, C1, C2, s):
     set_corner(Turtle, x+s*2, y)
     for i in range(2):
          Half_Square_Flip(Turtle, C1, C2, s)
          Half_Square(Turtle, C1, C2, s)

def row_1_4(Turtle, x, y, C1, C2, s):
    Turtle.speed(0)
    set_corner(Turtle, x+s*3, y)
    Square(Turtle, C1, s)
    Half_Square_Flip(Turtle, C2, C1, s)
    Half_Square(Turtle, C2, C1, s)
    Square(Turtle, C1, s)



    


def row_2_1(Turtle, x, y, C1, C2, s):
    Turtle.speed(0)
    set_corner(Turtle, x, y)
    for i in range(4):
        Square(Turtle, C1, s)

def row_2_2(Turtle, x, y, C1, C2, s):
    Turtle.speed(0)
    set_corner(Turtle, x+s, y)
    Square(Turtle, C1, s)
    Half_Square_Flip(Turtle, C2, C1, s)
    Half_Square(Turtle, C2, C1, s)
    Square(Turtle, C1, s)

def row_2_3(Turtle, x, y, C1, C2, s):
    Turtle.speed(0)
    set_corner(Turtle, x+s*2, y)
    Square(Turtle, C1, s)
    Half_Square(Turtle, C1, C2, s)
    Half_Square_Flip(Turtle, C1, C2, s)
    Square(Turtle, C1, s)

def row_2_4(Turtle, x, y, C1, C2, s):
    Turtle.speed(0)
    set_corner(Turtle, x+s*3, y)
    for i in range(4):
        Square(Turtle, C1, s)






def design_1 (Turtle, x, y, C1, C2, s):
#This function takes the previously created rows and turn them into actual 4 x 4 designs
    Turtle.speed(0)
    set_corner(Turtle, x, y)
    row_1_1(Turtle, x, y, C1, C2, s)
    row_1_2(Turtle, x, y, C2, C1, s)
    row_1_3(Turtle, x, y, C1, C2, s)
    row_1_4(Turtle, x, y, C1, C2, s)

def design_2(Turtle, x, y, C1, C2, s):
    row_2_1(Turtle, x, y, C2, C1, s)
    row_2_2(Turtle, x, y, C2, C1, s)
    row_2_3(Turtle, x, y, C2, C1, s)
    row_2_4(Turtle, x, y, C2, C1, s)

def design_1_(Turtle, x, y, C1, C2, s):
    row_1_1(Turtle, x, y, C1, C2, s)
    row_1_2(Turtle, x, y, C2, C1, s)

def design_2_(Turtle, x, y, C1, C2, s):
    row_2_1(Turtle, x, y, C2, C1, s)
    row_2_2(Turtle, x, y, C2, C1, s)
  
    




def block_1(Turtle, x, y, C1, C2, s):
#This function takes the designs and lines them up into a pattern 
    design_1(Turtle, x, y,C1, C2, s)
    design_2(Turtle, x+s*4, y, C1, C2, s)
    design_1(Turtle, x+s*8, y, C1, C2, s)
    design_2(Turtle, x+s*12, y, C1, C2, s)
    design_1_(Turtle, x +s*16, y, C1, C2, s)

def block_2(Turtle, x, y, C1, C2, s):
    design_2(Turtle, x, y-s*4-4, C1, C2, s)
    design_1(Turtle, x+s*4, y-s*4-4, C1, C2, s)
    design_2(Turtle, x+s*8, y-s*4-4, C1, C2, s)
    design_1(Turtle, x+s*12, y-s*4-4, C1, C2, s)
    design_2_(Turtle, x+s*16, y-s*4-4, C1, C2, s)

def Final_Design(Turtle, x, y, C1, C2, s):
    for i in range(3):
        block_1(Turtle, x, y, C1, C2, s)
        block_2(Turtle, x, y, C1, C2, s)
        y = y - s*8-8





            
##Execution

Final_Design(ted, -475, 400, 'lightgreen', 'lightblue', 25)

## ETC.
wn.mainloop()
