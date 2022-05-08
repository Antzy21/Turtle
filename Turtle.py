# Important imports
from _turtle import _turtle # Include the ability to make a turtle.
import time # Include the ability to stop time
import numpy as np # Include the ability to use pi (3.14...)

t = _turtle() # Initialise Turtle

# Example to draw a octagon
def drawExample(t):    
    t.draw = True # make the turtle draw
    for i in range(0,8):
        t.move(50)
        t.turn(np.pi/4)
        time.sleep(.5)
    time.sleep(2)

drawExample(t)