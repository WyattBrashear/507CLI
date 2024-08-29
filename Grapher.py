#Import Libraies
import turtle
import math

#Turtle Setup
t = turtle.Turtle()
t.shape("circle")
t.speed(100)

#functions
def drawtest():
  #Test If the display is active.
  for i in range(1000):
    t.forward(10 + i)
    t.left(90)