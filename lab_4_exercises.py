# Lab 4 Exercises.
# Chapter 8 Exercise CalcPay
def calcPay(h,r):
     if h<40:
        p = h * r
     else:
        p = (p*40) + ((h-40)*r*1.5)
        return p


hours = int(input('How any hours did you work'))
rate = int(input('What is your rate of pay'))

print(calcPay(hours, rate))
#It keeps saying "none" no matter what I try. Needs some review

#Chapter 8 problem 3
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

numb = int(input('Please enter the highest number'))

print(isPrime(number))

#Chapter 8 triNumber
def triNumber(n):
    triNumber = 0
    for aNumber in range(1, n + 1):
        triNumber = triNumber + aNumber

    return triNumber

print(triNumber(4))

#Struggled with Chart practice, countDigits, and guessing game
#guessing game, just a start 
import random

guessingGame = random.random()
guessingGame = random.randrange(1,101)
userguess = int(input('What is your guess'))
if userguess == guessingGame:
		print('You got it')
if userguess > guessingGame:
    print('Too high')
else:
    print('Too low')

#Worked on this lab assignment alone

