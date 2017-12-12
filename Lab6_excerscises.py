#Lab 6 Exercises 
#Question 2
#Didnt have enough time to complete other two excercises in the assignment 
mylist = []
mylist.append(76)
mylist.append(92.3)
mylist = mylist + ["hello", True]
mylist.append(4)
mylist.append(76)

print(mylist)

#Question 3
myList = [76, 92.3, 'hello', True, 4, 76]

myList.append("apple")         
myList.append(76)              
myList.insert(3, "cat")        
myList.insert(0, 99)           

print(myList.index("hello"))   
print(myList.count(76))        
myList.remove(76)              
myList.pop(myList.index(True)) 

print (myList)

#Question 4
import random
def average(n):
    mylist = []
    random.randrange(1000)
    for i in n:
        mylist = mylist.append(n)
    return average
    
print(average(100))

#question 5
import random

def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max

lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(max(lst))
