import turtle
import pygame
from pygame.locals import *
from sys import exit


## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("lightgrey")
wn.title("Makin Bacon")


## TURTLEs

'''I will use to make most of background'''
bagrou = turtle.Turtle()
bagrou.color('grey')
bagrou.pensize(3)

#Screen Facts

'''
Resolution = 795,945
Top right corner = 470,400
Top left corner = -475,400
Bot right corner = 470,-395
Bot left corner = -475,-395

'''

#Variable

keys = pygame.keys.get_pressed()

#Functions



##Execution       

if keys[pygame.K_w] and keys[pygame.K_SPACE]:
    print(1)

## ETC.

wn.mainloop()
