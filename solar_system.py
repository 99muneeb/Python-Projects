'''
What is a Solar System?
Our solar system consists of the Sun and 8 planets including Earth. Following are the planets in the Solar System in the given order:

1.Mercury
2.Venus
3.Earth
4.Mars
5.Jupiter
6.Saturn
7.Uranus
8.Neptune
'''

'''Project Prerequisites
In this project, we will require basic knowledge of python and its concepts. In this project we will be using two modules:

Math Module
Turtle Module
'''
'''
Steps to Build the Project
Follow the given steps to visualize the Solar System –

1.Install the Modules
2.Import the Modules
3.Create the GUI Screen
4.Create the Sun
5.Next Create the planets
6.Changing angles and adding planets on the screen
'''
#Start Project

#Importing the Modules
import turtle
import math
from math import *

#Creating the GUI Screen:
screen = turtle.Screen()#creating the screen
screen.tracer(50)

#Create the Sun:
sun = turtle.Turtle()#turtle object for sun
sun.shape('circle')#shape of sun
sun.color('yellow')#color of sun

#Creating the Planets:
class Planet(turtle.Turtle):
    def __init__(self,name,radius, color):#initialize function
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move(self):
        x = self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle)
 
        self.goto(sun.xcor()+x,sun.ycor()+y)

#Changing the Angles and Adding the Planets:
# making plantes
mercury = Planet("Mercury",40, 'grey')
venus = Planet("Venus",80, 'orange')
earth=Planet("Earth",100,'blue')
mars = Planet("Mars",150, 'red')
jupiter=Planet("Jupiter",180, 'brown')
saturn=Planet("Saturn",230, 'pink')
uranus=Planet("Uranus",250, 'light blue')
neptune=Planet("Neptune",280, 'black')
 
#adding planets to a list
myList = [ mercury, venus,earth, mars,jupiter,saturn,uranus,neptune]
 
 
while True:#while statement
    screen.update()#updating the screen
    for i in myList:
        i.move()#moving the elements of the list
 
    # Increase the angle by 0.0x radians
   
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005

