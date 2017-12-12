#Exercises Lab 5
#Chapter 9 Question 2
#Got as much as i could done but really struggled with Number 18 of the excercises, pig latin translation and the password strength
#Gonna continue to work on the even though i was not able to submit them in time

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p + "u" + suffix)
    else:
        print(p + suffix)

#Question 3
def count(p):
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in p:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1

    percent_with_e = (numberOfe / totalChars) * 100
    print("Your text contains", totalChars, "alphabetic characters of which", numberOfe, "(", percent_with_e, "%)", "are 'e'.")


p = '''
"He never seen rich but he seen poor Mr.Dollar and a dream 
in case you dint know. Its all a man got so if its
about that cream then im all up in the spot i got a dollar
and a dream - J.cole
'''

count(p)

#Question 6
from test import testEqual

def reverse(astring):
    reversed = ''
    astringR = astring + reversed
    for char in astring:
        reversed = char + reversed
    return reversed

testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")

#Question 7
from test import testEqual

def mirror(mystr):
    reversed = ''
    mystrM = mystr + reversed
    for char in mystr:
        reversed = char + reversed
    mystrM = mystr + reversed
    return mystrM
    
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')

#Question 8 
from test import testEqual

def remove_letter(theLetter, s):
    letters = theLetter
    sWithoutletters = ''
    for eachChar in s:
        if eachChar not in theLetter:
            sWithoutletters = sWithoutletters + eachChar
    return sWithoutletters

testEqual(remove_letter('a', 'apple'), 'pple')
testEqual(remove_letter('a', 'banana'), 'bnn')
testEqual(remove_letter('z', 'banana'), 'banana')

#Question 9
from test import testEqual

def reverse(mystr):
    reversed = ''
    for char in mystr:
        reversed = char + reversed
    return reversed

def is_palindrome(myStr):
    if myStr in reverse(myStr):
        return True
    else:
        return False

testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)

#Dont quit understand question 18

#Translating an english sentence to pig latin moves the first letter of the word to the back and adds an 'ay' to the end of it
 
def pigLatin(aString);
	