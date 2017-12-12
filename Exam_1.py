#Turtle Programming (Triangle)
import turtle

wn = turtle.Screen
alex = turtle.Turtle

alex.forward(50)
alex.left(120)
alex.forward(50)
alex.left(120)
alex.forward(50)

#Triangle 'for' loop
import turtle 

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(3):

    alex.left(120)
    alex.forward(50)
	
#Polygon fill Triangle
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

alex.fill(True)
for _ in range(3):
    alex.forward(100)
    alex.left(120)
alex.fill(False)

#Polygon def draw_triangle
import turtle

def draw_triangle(t, sz):

    for aColor in range('Red', 'Green', 'Blue'):
        t.forward(sz)
        t.left(120)


wn = turtle.Screen()
alex = turtle.Turtle()

draw_triangle(alex, 50)

wn.exitonclick()
#Polygon def draw_triangle (Different Colors and sizes)
#Red white and blue triangles
import turtle
wn = turtle.Screen()             

tess = turtle.Turtle()           
tess.color("White")

alex = turtle.Turtle()           
alex.color("Blue")

rambo = turtle.Turtle()
rambo.color("Red")

rambo.fill(True)
for i in range(3):
    rambo.forward(110)
    rambo.left(120)
rambo.fill(False)

tess.fill(True)
for i in range(3):
    tess.forward(80)                 
    tess.left(120)                 
tess.fill(False)

alex.fill(True)
for i in range(3):
    alex.forward(50)                 
    alex.left(120)
alex.fill(False)


wn.exitonclick()

#Calculate the square root of a number
n = int(input('Type a number'))
n = n**0.5
print(n(string))

#Calculate square root for a perf ect square
def is_perfect_square(n):
    for i in range(2,n):
        if n % i == 0:
            return True
    else:
        return False
n = int(input('Type a number'))

print(is_perfect_square,(n))

#square root perfect square part 2
def is_perfect_square(n):
    for i in range(2,n):
        if n % i == 0:
            print('The number', n, 'Is a perfect square')
    else:
        print('The number', n, 'Is not a pefect square')
n = int(input('Type a number'))


