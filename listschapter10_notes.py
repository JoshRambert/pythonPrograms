#Introduction to the list Function
vocabulary = ["iteration", "selection", "control"]
numbers = [17, 123]
empty = []
mixedlist = ["hello", 2.0, 5*2, [10, 20]]

print(numbers)
print(mixedlist)
newlist = [ numbers, vocabulary ]
print(newlist)

		#COunts the number of ites within the list/ items inbetween the commas
		alist =  ["hello", 2.0, 5, [10, 20]]
		print(len(alist)) #will print 4
		print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]])) #Will also print 4

#Accessing elements/REMEMBER counting starts from 0
numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2]) 
print(numbers[9 - 8]) #will print 123
print(numbers[-2]) #will print 8398
print(numbers[len(numbers) - 1])

		#'in' and 'not in' are boolean expressions
		fruit = ["apple", "orange", "banana", "cherry"]
		print("apple" in fruit) #True
		print("pear" in fruit) #False
		
#Concatenation and Repetition
fruit = ["apple", "orange", "banana", "cherry"]
print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([1, 2, ["hello", "goodbye"]] * 2)

		#List slices / the slice operation stops at the number indicated and starts counting from zero
		a_list = ['a', 'b', 'c', 'd', 'e', 'f']
		print(a_list[1:3]) #will print ['b', 'c']
		print(a_list[:4]) #will print ['a', 'b', 'c', 'd']
		print(a_list[3:]) #will print ['d', 'e', 'f']
		print(a_list[:]) #will print ['a', 'b', 'c', 'd', 'e', 'f']
		
#You can change an item in the list by accessing it directly For Example
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit) #Replaces the first and the last item within the list with what was

		#List deletion removes an item from the list
		a = ['one', 'two', 'three']
		del a[1] 
		print(a) #print ['one', 'three']

		alist = ['a', 'b', 'c', 'd', 'e', 'f']
		del alist[1:5] 
		print(alist) #prints ['a, 'f']
		
#Objects and References 'is' is a boolean expression
a = "banana"
b = "banana"

print(a is b) #True

a = [81, 82, 83]
b = [81, 82, 83]

print(a is b) #False the 'is' operation does not work for lists

print(a == b) #True, one must use the '=='

		#Aliasing
		alist = [4, 2, 8, 6, 5]
		blist = alist
		blist[3] = 999
		print(alist)
		
#Cloning or copying a list
a = [81, 82, 83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)

		#Reptitions and references 
		origlist = [45, 76, 34, 55]

		newlist = [origlist] * 3 #prints the origlists 3 times

		print(newlist)

		origlist[1] = 99 #Replaces '76' in the list with '99'

		print(newlist)
		
#List methods
mylist = []
mylist.append(5) #'append' adds an item to the list
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12) #'insert' (position, item)
print(mylist)
print(mylist.count(12)) #'count' count the number of times an item appears within the list

print(mylist.index(3)) #'index' gives the numeric position of an item
print(mylist.count(5))

mylist.reverse() #reverses the order of the list
print(mylist)

mylist.sort() #sorts the list from lowest to highest
print(mylist)

mylist.remove(5) #removes said item from the list
print(mylist)

lastitem = mylist.pop() #removes and returns the last item of the list
print(lastitem)
print(mylist)

		#Turtles and Lsystems with the using Lists
		import turtle

		def drawLsystem(aTurtle, instructions, angle, distance):
			savedInfoList = []
			for cmd in instructions:
				if cmd == 'F':
					aTurtle.forward(distance)
				elif cmd == 'B':
					aTurtle.backward(distance)
				elif cmd == '+':
					aTurtle.right(angle)
				elif cmd == '-':
					aTurtle.left(angle)
				elif cmd == '[':
					savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
					print(savedInfoList)
				elif cmd == ']':
					newInfo = savedInfoList.pop()
					print(newInfo)
					print(savedInfoList)

t = turtle.Turtle()
inst = "FF[-F[-X]+X]+F[-X]+X"
drawLsystem(t, inst, 60, 20)

#Lists and 'for' loops
numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 3

print(numbers)

alist = [4, 2, 8, 6, 5]
blist = [ ]
for item in alist:
    blist.append(item+5) #adds five to each of the integers within the original list
print(blist)

		#using lists as parameters
		def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
			for item in range(len(aList)):
				aList[item] = 2 * aList[item]

		things = [2, 5, 9]
		print(things)
		doubleStuff(things)
		print(things)

		#Pure functions / same as above but different way of going about it 
		#Try to use pure funtions over modifiers which is the programming above 
		def doubleStuff(a_list):
			""" Return a new list in which contains doubles of the elements in a_list. """
			new_list = []
			for value in a_list:
				new_elem = 2 * value
				new_list.append(new_elem)
			return new_list

		things = [2, 5, 9]
		print(things)
		things = doubleStuff(things)
		print(things)

#Functions that produce lists
def primes_upto(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result
	
		#List Comprehensions
		mylist = [1,2,3,4,5]

		yourlist = [item ** 2 for item in mylist]

		print(yourlist)#squares each number from the original list

#Nested Lists
nested = ["hello", 2.0, 5, [10, 20]]
innerlist = nested[3]
print(innerlist)
item = innerlist[1]
print(item)

print(nested[3][1])

		#Strings and Lists
		wds = ["red", "blue", "green"]
		glue = ';'
		s = glue.join(wds)
		print(s)
		print(wds)

		print("***".join(wds))
		print("".join(wds))
		
#List type Conversion / seperates the string into a list
xs = list("Crunchy Frog")
print(xs)

#Tuples and mutability / tuples are lists that are immutable and must have a comma within them to be considered a tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

#Tuples as Return Values
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circleInfo(10))
