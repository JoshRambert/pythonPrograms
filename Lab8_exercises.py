#Lab 8 Exercises
#Question 1
studentdata = open('C:\Users\Joshua\Desktop\studentdata.txt', 'r')

for eachline in studentdata:
    values = eachline.split()
    if len(values[1:]) > 6:
            print(values[0])

studentdata.close()

#Question 2
studentdata = open('C:\Users\Joshua\Desktop\studentdata.txt', 'r')

for eachline in studentdata:
    values = eachline.split()
    total = 0
    for i in range(1, len(values)):
        total = total + int(values[i])
    avg = total / (len(values)-1)
    print(values[0], round(avg, 2))

studentdata.close()

#Question 3 
studentdata = open('C:\Users\Joshua\Desktop\studentdata.txt', 'r')

for eachline in studentdata:
    values = eachline.split()
    print(values[0], max(values[1:]), min(values[1:]))

studentdata.close()

#Question 5
import turtle

wn = turtle.Screen()
wn.bgcolor('Black')
wn.setworldcoordinates(-300, -300, 300, 300)
rambo = turtle.Turtle()
rambo.color('red')
rambo.pensize(3)
rambo.speed(10)

mystery = open('mystery.txt', 'r')

for eachline in mystery:
    values = eachline.split()
    if values[0] == 'UP':
        rambo.up()
    else:
        if values[0] == 'DOWN':
            rambo.down()
        else:
            rambo.goto(int(values[0]), int(values[1]))

mystery.close()
wn.exitonclick() 

