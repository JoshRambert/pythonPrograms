# Some Turtle Programming 

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("square")

tess.up()                     # this is new
for size in range(3, 60, 2):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)          # move tess along
    tess.right(24)              # and turn her

wn.exitonclick()

#Some more programming notes to keep in mind for the future 
#3n + 1 sequence 
def seq3np1(n):
    """Multiplies a number by three then adds 1 and divides it by two until it can finally reach 1 by division even numbers will always divide down to 1"""
    while n != 1:
        print(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n)                  # the last print is 1

seq3np1()
# The sum of consecutive numbers 
def addTo(n):
    """Adds the total of consecutive numbers""" 

    thesum  = 0
    number = 2
    while number <= n:
        thesum = thesum + number
        number = number + 2
    return thesum

print(addTo(4))
print(addTo(1000))

#Sum of consecutive numbers (different way to do it)
def sumTo(aBound):
    theSum = 0
    for aNumber in range(1, aBound + 1):
        theSum = theSum + aNumber

    return theSum

print(sumTo(4))

print(sumTo(1000))

#Turtle programming 
#triangle 
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(3):
    alex.left(120)
    alex.forward(50)
    
wn.exitonclick()

#Square
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(4):
    alex.left(90)
    alex.forward(90)

wn.exitonclick()

#Octagon
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(8):
    alex.left(45)
    alex.forward(50)
    
wn.exitonclick

#More interesting turtle programs and 'for' loop uses
 
import turtle

wn = turtle.Screen()
lovelace = turtle.Turtle()

# move the turtle forward a little so that the whole path fits on the screen
lovelace.penup()
lovelace.forward(60)

# now draw the drunk pirate's path
lovelace.pendown()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:

    # we use .left() so that positive angles are counter-clockwise
    # and negative angles are clockwise
    lovelace.left(angle)
    lovelace.forward(100)

# the .heading() method gives us the turtle's current heading in degrees
print("The pirate's final heading was", lovelace.heading())

wn.exitonclick()

#Draw a Star

import turtle

turing = turtle.Turtle()

for i in range(5):
    turing.forward(110)
    turing.left(216)

#GuessingGame 
import random

guessingGame = random.random()
guessingGame = random.randrange(1,6)

userguess = int(input('Guess a number between 1 and 5'))
if userguess == guessingGame:
		print('Bitch YOU GUESSED IT')
if userguess > guessingGame:
    print(userguess, '...Forreal nigga', userguess,'!?!', 'Too DAMN HIGH')
else:
    print(userguess, 'That number is TOO LOW weak nigga! TOO LOWWWW')
	
#Random module programming
import random 

howmany = 10
for counter in range(howmany):
    arandom = random.random()
    print(arandom)
	
#More random programming 
import random 

howmany = 10
for counter in range(howmany):
    arandom = random.randrange(25,35)
    print(arandom)

#import Math Programming
import math

side1 = 3
side2 = 4

hypotenuse = math.hypot(side1, side2)
print(hypotenuse)

#Squaring numbers programming
def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
print("The result of ", toSquare, " squared is ", result)

#Drawing polygons using the 'def' function
import turtle

def drawRectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def drawSquare(tx, sz):        # a new version of drawSquare
    drawRectangle(tx, sz, sz)

wn = turtle.Screen()             # Set up the window
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess

drawRectangle(tess, 50, 60)

wn.exitonclick()

#More of the same 
import turtle
def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""
    
    rambo.fill(True)
    for i in range(4):
        t.forward(sz)
        t.left(90)
    rambo.fill(False)

wn = turtle.Screen()
wn.bgcolor('blue')
rambo = turtle.Turtle()
rambo.color('white')

drawSquare(rambo, 50)

#Triangle using the 'def' function
import turtle
def drawTriangle(t, sz):
    """Make turtle t draw a square of sz."""
    
    rambo.fill(True)
    for i in range(3):
        t.forward(sz)
        t.left(120)
    rambo.fill(False)
    
wn = turtle.Screen()
wn.bgcolor('lightblue')
rambo = turtle.Turtle()
rambo.color('Red')
rambo.shape('turtle')
            
drawTriangle(rambo, 100)
#Octogon Using turtle programming
import turtle
def drawOctogon(t, sz):
    """Make turtle t draw a square of sz."""
    
    rambo.fill(True)
    for i in range(8):
        t.forward(sz)
        t.left(360/8)
    rambo.fill(False)
    
wn = turtle.Screen()
wn.bgcolor('black')
rambo = turtle.Turtle()
rambo.color('blue')
rambo.shape('circle')
rambo.pensize(5)
            
drawOctogon(rambo, 200)

#More versatile way of going bout I have been doing this whole time -___-
import turtle

def drawPolygon(t, sideLength, numSides):
    
    for i in range(10):
        geo.forward(sideLength)
        geo.left(360/10)


wn = turtle.Screen()
geo = turtle.Turtle()

drawPolygon(geo,50,10)  # draw a decagon

wn.exitonclick()

#A CIRCLE!!!
import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)


wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 20)

wn.exitonclick()

# using the main function 
def squareit(n):
    return n * n

def tripleit(n):
    return n*n*n

def main():
    anum = int(input("Please enter a number"))
    print(squareit(anum))
    print(tripleit(anum))

if __name__ == "__main__":
    main()
	
#To find a prime number 
def isPrime(n):
    for i in range(1,n):
        if n % i == 0 and n % n**.5 == 0:
            return True
        else:
            return False
number = int(input('Please enter a number'))
print(isPrime(number))

#To find a composite number that is opposite Prime
def isComposite(n):
    for i in range(1,n):
        if n % i == 0 and n % n**.5 == 0:
            return False
        else:
            return True
number = int(input('Please enter a number'))
print(isComposite(number))

#Using Import random and Turtle programming to get turtles to do random patterns
import random
import turtle


def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(90)
    else:                      # tails
        t.right(90)

    t.forward(50)

wn.exitonclick()

#Kinda Useless but approximation of square root numbers 
def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(10, 3))
print(newtonSqrt(10, 5))
print(newtonSqrt(10, 10))

#To make a table pretty simple

print("n", '\t', "2**n")     #table column headings
print("---", '\t', "-----")

for x in range(13):        # generate values for columns
    print(x, '\t', 2 ** x)
	
#Image editing 
import image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())

#added iteration technique "For j in range" iterates the iteration
for i in range(5):
    for j in range(3):
        print(i, j)
		
#More image editing that could end up being useful in the future
import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 0 - p.getGreen()
        newblue = 0 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
#Changes the color setting of the picture

#Using data files and turtle programming
import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)

f = open("mystery.txt", "r")

for aline in f:
    items = aline.split()
    if items[0] == "UP":
        t.up()
    else:
        if items[0] == "DOWN":
            t.down()
        else:
            # must be coords
            t.goto(int(items[0]), int(items[1]))

f.close()
wn.exitonclick()
