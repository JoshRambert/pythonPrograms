#Three different Shapes 
import turtle
def drawPolygon(t, sideLength, numSides):
    
    
    t.penup()
    t.left(90)
    t.forward(130)
    t.right(90)
    t.forward(40)
    t.pendown()
    t.fill(True)
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)
    t.fill(False)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)


wn = turtle.Screen()
wn.bgcolor('Black')
wheel = turtle.Turtle()
wheel.pensize(4)
wheel.color('Blue')
wheel.speed(1000)

def drawTriangle(t, sz):
    """Make turtle t draw a square of sz."""
    
    t.penup()
    t.backward(35)
    t.pendown()
    rambo.fill(True)
    for i in range(3):
        t.forward(sz)
        t.left(360/3)
    rambo.fill(False)

rambo = turtle.Turtle()
rambo.color('white')
rambo.shape('circle')
rambo.pensize(3)
rambo.speed(5)

def drawSquare(t, sz):

    t.penup()
    t.backward(5)
    t.pendown()
    caleb.fill(True)
    for i in range(4):
        t.forward(sz)
        t.left(360/4)
    caleb.fill(False)
    
caleb = turtle.Turtle()
caleb.color('red')
caleb.shape('turtle')
caleb.pensize(3)
    
drawCircle(wheel, 90)   
drawTriangle(rambo, 150)
drawSquare(caleb, 60)

#all filled programming