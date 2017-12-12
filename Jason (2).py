#-------------------------
# Jason Archer
# Triangle Extra Credit
# CS 133P Tu/Th
#--------------------------

import math
import turtle

def calcSideC(sideA, sideB):                        #Calculates side C of triangle
    sideC = math.sqrt(sideA**2 + sideB ** 2)
    return int(sideC)

def calcAngle(sideA, sideB):                        #Calcutates the angle to then draw side C
    angle = math.atan(sideA/sideB) * 57.2957795
    return angle

def draw_triangle(t, a, b, c, ca):                  #Draws a triangle
    alex.forward(a)
    alex.left(90)
    alex.forward(b)
    alex.left(180 - ca)
    alex.forward(c)
    alex.left(ca + 90)

wn = turtle.Screen()                                #Screen setup
wn.bgcolor("black")

alex = turtle.Turtle()                              #Create turtle and set starting position
alex.penup()
alex.backward(150)
alex.right(90)
alex.forward(175)
alex.left(90)
alex.pendown()

sideA = 300                                         #Largest side values for A and B
sideB = 400

tri = 0                                             #Counts the number of triangles drawn

while tri < 10:                                     #A loop to draw 10 triangles in different colors
    for i in ["brown","green","yellow","orange","red","purple","blue","darkgreen","black","lightblue"]:
        alex.color(i)
        alex.begin_fill()
        draw_triangle(alex, sideA - tri * 30, sideB - tri * 40, calcSideC(sideA, sideB) - tri * 50, calcAngle(sideA, sideB))
        alex.end_fill()
        alex.penup()
        alex.forward(20)
        alex.left(90)
        alex.forward(10)
        alex.right(90)
        alex.pendown()
        tri = tri + 1

wn.exitonclick()