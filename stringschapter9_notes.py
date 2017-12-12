#Will print the letters of the String in order from 0-n
school = "Luther College"
m = school[2]
print(m) #will print the letter 't' because the counting starts from 0

lastchar = school[-1]#Counting backwards starts at 1
print(lastchar)

		#Changes the letters in the string to either uppercase or lowercase
		ss = "Hello, World"
		print(ss.upper())

		tt = ss.lower()
		print(tt)

#More string operations
ss = "    Hello, World    "

els = ss.count("l") #Counts the number of items within the string in this case 3
print(els)
#'Strip' removes spaces from either "l" left side or "r" right side or both of neither are specified 
print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")

news = ss.replace("o", "***")#'.replace' replaces anything within the string with whatever the user chooses
print(news)

		#More 'String' operations
		food = "banana bread"
		print(food.capitalize())

		#'.center' centers the string '.ljust' '.rjust' moves it either left or right
		print("*" + food.center(25) + "*")
		print("*" + food.ljust(25) + "*")     # stars added to show bounds
		print("*" + food.rjust(25) + "*")

		#'.find' gives the numeric position of a letter in a string
		print(food.find("e"))
		print(food.find("na"))
		print(food.find("b"))

		#'.rfind' or '.lfind' gives the numeric position of a letter either farthest right or left
		print(food.rfind("e"))
		print(food.rfind("na"))
		print(food.rfind("b"))

		print(food.index("e"))

fruit = "Banana"
print(len(fruit))#Gives length of String 

#IMPORTANT PROGRAMMING THAT COULD HELP IN THE FUTURE
fruit = "Banana"
sz = len(fruit)
lastch = fruit[sz-1]
print(lastch)

		#Seperates the string into different parts by using its numeric position
		singers = "Peter, Paul, and Mary"
		print(singers[0:5]) #will print 'Peter'
		print(singers[7:11]) #will print 'Paul'
		print(singers[17:21] #will print 'Mary'

		
		fruit = "banana"
		print(fruit[:3]) #Prints first three letters 
		print(fruit[3:]) #Prints last three letters

#The position of the Word depends on the alphabetical order of the first letter		
word = "Zebra"
if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")
	
		#'ord' gives the ordinal value of letters
		print(ord("A")) = 65
		print(ord("B")) = 66
		print(ord("5")) = 53

		print(ord("a")) = 97
		print("apple" > "Apple")

		#'chr' gives the character value of each integer
		print(chr(65))
		print(chr(66))

		print(chr(49))
		print(chr(53))

		print("The character for 32 is", chr(32), "!!!")
		print(ord(" "))
		
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:] #replaces the first letter of the original string with a 'J'
print(newGreeting)
print(greeting) 
	
fruit = "apple"
for i in range(len(fruit)): #Using 'len' makes it easier than predicting how many items are in the string
    print(fruit[i]) #prints the letters of 'apple' on a different line each time
	
s = "python rocks"
for i in s:
    print("HELLO") #Prints Hello 12 times for the number of items within string of "s"
	
s = "python rocks"
for idx in range(len(s)): 
    if idx % 2 == 0:
        print(s[idx]) #Only prints the letters that are divisible by two according to its numeric position
		
		fruit = "apple"
		position = 0
		while position < len(fruit):
			print(fruit[position])
			position = position + 1 #Will print every letter in the string starting with the position 0 in 'apple'
			
s = "python rocks"
idx = 1
while idx < len(s):
    print(s[idx])
    idx = idx + 2 #same except it will print every other letter starting with 'y' in 'python rocks'
	
	#'in' 'not in' operator self explanatory
	print('p' in 'apple') #True
	print('i' in 'apple') #False
	print('ap' in 'apple') #True
	print('pa' in 'apple') #False
	print('x' not in 'apple') #True
	
	
#Using the accumulator pattern with strings
def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels = sWithoutVowels + eachChar
    return sWithoutVowels

print(removeVowels("compsci")) 
print(removeVowels("aAbEefIijOopUus")) #removes vowels

#Using the accumulator pattern and turtles with strings
import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()

#Counts the number of times a letter appears in a word 
def count(text, aChar):
    lettercount = 0
    for c in text:
        if c == aChar:
            lettercount = lettercount + 1
    return lettercount

print(count("banana","a"))

#Finds the numeric position of a letter in a string and returns it if therre isnt one it returns '-1'
def find(astring, achar):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = 0
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))
#Adds an extra parameter by giving it a starting position
def find2(astring, achar, start):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find2('banana', 'a', 3))

#I dont even know, looks important though
def find4(astring, achar, start=0, end=None):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    if end == None:
        end = len(astring)

    found = False
    while ix < end and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

ss = "Python strings have some interesting methods."

print(find4(ss, 's'))
print(find4(ss, 's', 7))
print(find4(ss, 's', 8))
print(find4(ss, 's', 8, 13))
print(find4(ss, '.'))

	#Mirrors the current word in the string
	s = "ball"
	r = ""
	for item in s:
		r = item.upper() + r
	print(r)


