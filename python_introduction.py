#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is a python script
# This is a comment

# Introduction to Python, Variables,
# objects, boolean logics, loops, decisions and Control Flow Statements

# https://ourcodingclub.github.io/tutorials/python-intro
# https://docs.python.org/3/tutorial

print("hello, world!")

"""
Python has these commonly used standard data types

Integer (Number)
Float (Number)
String (Text)
List (List of objects)
Tuple (Fixed list of objects)
Dictionary (Key/Value pairing)
Set (List without duplicate elements)

Use the interactive python console to establish a variable
Containing a datatype of each kind listed above.

This comment is a multiline string
"""

# run selection with black arrow
# run file with green arrow

MyInteger = 42
MyFloat = 3.145
MyString = "This is text."
MyList = [1, 2, 3, "Four", "Five"]  # MyList[1] = 2 Common mistake !
MyTuple = (1, 2, 3, "Four", "Five")  # Tuples can not be changed
MyDictionary = {"one":1, "two":2, "three":3}
MySet = {1, 2, 2, 3, 3}

MyInteger
MyFloat
MyString
MyList
MyTuple
MyDictionary
MySet

# Python Arithmetic Operators

21 + 21  # Addition
44 - 2  # Subtraction
336 / 8  # Division
3 * 5  # Multiplication
2 ** 3  # Exponent
22 // 9  # Integer division or "floored quotient" (https://blog.tecladocode.com/pythons-modulo-operator-and-floor-division)
22 % 9  # Modulus/remainder (https://www.computerhope.com/jargon/m/modulo.htm)


# Assignment Operators
a = 1  # save object under a name
b = 2

# Question 1
# Imagine a cube with side s
# Assign a variable to the volume of the cube

s=3
volume_do_cubo = s ** 3

# Python Comparison (Relational) Operators

a == b  # equal
a != b  # not equal
a > b  # greater than
a < b  # less than
a >= b  # greater than or equal to
a <= b  # less than or equal to

# Question 2
# is 243432 + 2345442 equal to 1154312 + 2588874 ?
# write a code line to test this

a = 243432 + 2345442 
b = 1154312 + 2588874
a==b

# Assignment Operators vs Comparison Operators (Common mistake #1)
a == 2  # is a equal to 2 ?
a = 2  # assign 2 to a


# Python is cap sensitive (Common mistake #2)
a = 1
A = 2
a == A

# Logical Operators (Boolean logics)

a = True
b = False

a and b
a or b
not a
not b

# Membership Operators (This aloso works for strings!)

a = [1, 2, 3, 4, 5, 6, 7]

3 in a
9 in a

# Question 3
# Does the word "Hipopotomonstrosesquipedaliofobia"
# contain the word "monstro"?
# write a code line to test this

a = "Hipopotomonstrosesquipedaliofobia"
b = "monstro"
b in a

# Identity Operators
a = ["3", "3"]
b = a
c = ["3", "3"]
a is b
a is c
a is not c


# Functions
print(123)  # built in function
print("123")

print(123, "123")


def area(D):  # user defined function
    pi = 3.14159
    a = pi * ((D / 2) ** 2)
    return a


Mydiameter = 5
MyArea = area(Mydiameter)
print(MyArea)

# Question 4
# Calculate the volume of a box with sides x,y,z
# Write a function named "boxvol"

def boxvol(a,b,c):
    vol = a*b*c
    return vol

x = 5
y = 2
z = 3

MyVol = boxvol(x,y,z)
print(MyVol)

# Reading a text file
h = open("foo.txt")

t = h.read()  # read is a function of the filehandle object = method

h.close()  # close the file

print(t)


# loops

a = [1, 2, 3, 4, 5, 6, 7]
a = ["Mo","Tu", "We", "Th", "Fr"]

for item in a:
    print(item)
    print("!")


x = 0
while x < 9:
    print(x)
    x = x + 0.5


for key in MyDictionary:
    print(key)


for val in MyDictionary.values():
    print(val)


for key, val in MyDictionary.items():
    print(key, val)


# flow control (if statements)

a = 5
if a < 5:
    print("smaller")
elif a == 5:
    print("same")
else:
    print("larger")

a = [1, 2, 3, 4, 5, 6, 7]

if 9 in a:
    print("yes")
else:
    print("no")
    


x = 0
while True:
    x = x + 1
    print(x)
    if x > 9:
        break


# Back to strings
# Python Arithmetic Operators for strings
# Operator overloading

a = "Hi"
b = "You"

a + b

#                       "This is a sample text"
#                        012345678911111111112
#                                  01234567890
                                     

my_string = "This is a sample text"

my_string[2:]
my_string[2:7]

my_string[::2]
my_string[::-1]

my_string[-4:]



# Import a built in library 

from math import pi

type(pi)

pi

import math

math.e

e = 3

type(math.e)

# Question 5
# Update the area(D) function to use the pi contstant from the math library
# copy paste the function below:

from math import pi
def area(D):  # user defined function    
    a = pi * ((D / 2) ** 2)
    return a

area(9)

# Methods for strings

# METHOD	            DESCRIPTION
# capitalize()      	Converts the first character to upper case
# casefold()        	Converts string into lower case
# replace()             replace letters           
# count()           	the number of times a specified value occurs in a string
# endswith()        	true if the string ends with the specified value
# find()            	Returns the position of where value was found
# format()          	Formats specified values in a string


x = 'xpple bxnxnx cherry'
x.replace("x","a")


my_text = 'Aello to All the world'

my_text.replace(my_text[0], 'H')

my_text.replace(my_text[0], 'H', 1)



### Functions II Common error:
    
def add(a,b):  # user defined function
    result = a + b
    return result

a = 2
b = 3

add(a,b)
print(add(a,b))

### This is wrong!
def add2(a,b):  # user defined function
    result = a + b
    print(result)
    return 

print(add2(a,b))



# Question 6
# Define a function called gc that returns the gc
# content for a DNA sequence (gatc)

def gc1(string):
    i=0
    for x in string:
        if x=="G" or x=="C":
            i=i+1
    x=len(string)
    ide=(i/x)*100
    return ide

gc1("GGATT")

def gc2(D):
    n = D.count ("g") + D.count("c")
    t = D.count ("g") + D.count("c") + D.count("a") + D.count ("t")
    result = n/t
    return result

gc2("ggatt")

def gc3(D):
    result = (D.count ("g") + D.count("c")) / len(D)
    return result

gc3("ggatt")



# https://wiki.python.org/moin/BeginnersGuide/NonProgrammers


#   string concatenation
#   slicing of strings and lists
# Functions
# https://runestone.academy/runestone/books/published/thinkcspy/index.html





# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
   for(i in 1:a) {
      b <- i^2
      print(b)
   }
}

# Call the function new.function supplying 6 as an argument.
new.function(6)




for(i in 1:10) {
  # i-th element of `u1` squared into `i`-th position of `usq`
  usq[i] <- u1[i]*u1[i]
  print(usq[i])
}