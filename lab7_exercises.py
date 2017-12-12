#Lab 7 Exercises
#Question 7
import random

def countOdd(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd

# make a random list to test the function
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(countOdd(lst))

#Question 8
import random

def sumPositive(lst):
    sum = 0
    for e in lst:
        if e > 0:
            sum = sum + e
    return sum

lst = []
for i in range(100):
    lst.append(random.randrange(0, 1000))

print(sumPositive(lst))


#Question 9
import random

def sumNegative(lst):
    sum = 0
    for e in lst:
        if e < 0:
            sum = sum + e
    return sum

lst = []
for i in range(100):
    lst.append(random.randrange(-1000, 1000))

print(sumNegative(lst))

#Question 11
import random

def sum(lst):
    sum = 0
    index = 0
    while lst[index] % 2 != 0 and index < len(lst):
        sum = sum + lst[index]
        index = index + 1
    return sum

lst = []
for i in range(100):
    lst.append(random.randint(0,1000))

print(sum(lst))
