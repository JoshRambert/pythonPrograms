#Hands on portion of the Exam Part 1
def is_composite(n):
	for i in range(2,n):
		if n % i == 0:
			return True 
		else: 
			return False 
numb = int(input('Please enter a number'))

print(is_composite(numb)) 

#Hands on Exam part 2

import math
def calcSideC(sideA, sideB):
	sideC = math.sqrt(sideA**2 + sideB**2)
	return int(sideC)
def calcAngle(sideA, sideB)
	angle = math.atan(sideA/sideB) * 57.2957795
	return angle
sideA = 30
sideB = 40
sideC = calcSideC(sideA, sideB)
angle = calcAngle(sideA, sideB)
print (sideC)
print (angle)

import turtle

wn = turtle.Turtle()
alex = turtle.Turtle()

alex.forward(sideA)
alex.left(90)
alex.forward(sideB)
lex.left(142)
alex.forward(sideC)

#Question 31

import turtle

wn = turtle.Screen
alex = turtle.turtle

for i in range(4):
	alex.forward(50)
	alex.left(90)