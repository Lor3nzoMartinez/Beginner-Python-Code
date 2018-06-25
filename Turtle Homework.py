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

def dashed_line (Turtle, lng, n):
    for i in range(n):
        Turtle.pu()
        for i in range (3):
            Turtle.fd(lng/9)
            Turtle.pd()

def octagon (Turtle, lng, n):
    for i in range(5):
        dashed_line(Turtle, lng, n)
        Turtle.lt(72)

##Execution       

octagon(extr, 100,5)



## ETC.
wn.mainloop()
