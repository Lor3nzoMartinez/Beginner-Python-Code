import turtle

## GUI INTERFACE
def make_window(colr,ttle):
    wn = turtle.Screen()
    wn.bgcolor(colr)
    wn.title(ttle)

def make_turtle (colr, sz, name):
    t=turtle.Turtle(name)
    t.color(colr)
    t.pensize(sz)
    return t

def rectangle (t,w,h):
    for i in range(2):
        t.fd(W1)
        t.lt(90)
        t.fd(H1)
        t.lt(90)
make_window("blue",'makin bacon')
make_turtle('hot_pink',5,tess)
rectangle('blue',4,tess)


## ETC.
wn.mainloop()
