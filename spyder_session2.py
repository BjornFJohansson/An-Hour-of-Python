"""
            /^\/^\
          _|__|  O|
\/     /~     \_/ \
  \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                  /      /                    \
                /     /                       \\
              /      /                         \ \
              /     /                            \  \
            /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
          (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
                ~--______-~                ~-___-~

                  _                               __ 
    /\           | |                             / _|
   /  \   _ __   | |__   ___  _   _ _ __    ___ | |_ 
  / /\ \ | '_ \  | '_ \ / _ \| | | | '__|  / _ \|  _|
 / ____ \| | | | | | | | (_) | |_| | |    | (_) | |  
/_/    \_\_| |_| |_| |_|\___/ \__,_|_|     \___/|_|  
                                                    

 _____       _   _                 
|  __ \     | | | |                
| |__) |   _| |_| |__   ___  _ __  
|  ___/ | | | __| '_ \ / _ \| '_ \ 
| |   | |_| | |_| | | | (_) | | | |
|_|    \__, |\__|_| |_|\___/|_| |_|
        __/ |                      
        |___/

Version 1.0.0
"""

# There are two ways to interact with python, interactively or by 
# saving a text file with python code as a ".py" file. 
# Using python interactively will give us a response to each command. 

# This is good for testing out python code lines, while writing and saving a
# python program ".py" file is good for 

# Lets get used to the interpreter interactively:

# Lines starting with "#" are comments and ignored by Python

    


# An integer (type: int):

5

# A floating point number (type: float)

3.14

# Addition

2 + 2

# A mathematical expression

50 - 5*6

# Division always returns a floating point number

(50 - 5*6) / 4

# With Python, it is possible to use the ** operator to calculate powers

5 ** 2  # 5 squared

2 ** 7  # 2 to the power of 7

# The equal sign (=) is used to **assign** a 
# value to a **variable**. The value of a variable is remembered
# until you leave the Python interpreter.

width = 3

# No result is displayed before the next interactive prompt

width


height = 4

area = width * height

area

width = 4 # This replaces the old value

width

area = width * height

area # Area now gets a new value

# try to access an undefined variable

n

# Other datatypes
# We learned that Python has int and float to represent numbers.
# Aditionally, Pyhton has the follwing datatypes:

# - str             Text
# - list            A list of variables or "objects"
# - dict            A dictionary

# There are the aditional data types "tuple" and "set", but we
# will leave them for now.







# A string is good for holding text:

mystring = "This is a text"

# We can look at each letter in a string

mystring[0]

mystring[2]

# We can look at parts of a string (a "slice"), and important concept.

mystring[5:7]






# A list is good for holding an ordered collection of variables
# A list can be made using square brackets []
# We can mix varables in a list:

mylist = [1, "Item1", 3.14, "pizza"]

# We can look at each element in a list

mylist[1]

# We can also look at parts of a list (a "slice")
# list slice ->  mylist[start:stop:step]

mylist[0:2]

mylist[1:3]

# IMPORTANT! lists have ZERO based indexing
# look in the link below for more information
# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types

# This is a source of many errors.

mylist[::2] # We can look at every second delement.

mylist[::-1] # We can turn the list around using a negative step.

# We can delete a list element using the command "del"

del mylist[1]

mylist + mylist # We can add two lists together






# A dictionary (datatype: dict) is a collection of keys and values
# We can mix datatypes for both keys and values

mydict = {"rain": "chuva", "umbrella": "guarda-chuva"}

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}

mydict["e"] = 2.718  # This is how you add a dictionary value.

# functions (built-in)
# A function is a "factory" that accepts input (arguments)
# and returns a result.

# Just like a mathematical function, for example:

#   f(x) = 2x + 3

# The type function is very useful. It returns the datatype of a variable.

type(mydict)

print("Hello!")  # Does *not* return anything

len(mylist)







# More functions!
# There are also user defined functions.
# We can package code in a function so that we can reuse the code.

def triangle_area(height, width):  # a function name can have no spaces. height, width are arguments
    area = height * width / 2      # This is a **block** of code.
    return area                    # Return something from the function (area).


triangle_area(3, 4)

triangle_area(30, 40)


# The **block** of code is important. That is how Python knows
# what code belongs to the function.
# Remember this concept, it will be important later.

# Import modules for more functions and other useful things.
# Modules are simply collections of useful fucntions.

import pydna

pydna.logo()

from math import pi

pi

import math

math.pi

import this # The Zen of Python

# Modules are practical if you do not want to have everything in the same
# file. 







### Program flow control statements are "for", "if" and "while".

# Repetition with the for statement
# lets bring back our list from before:

mylist

for element in mylist: # for accepts list, string, dict and other "container" types.
    print(element) # codeblocks are treated as a group of code.
    

for element in range(5): # We can make a list if we do not have one.
    print(element)

range(10)
list(range(10)) # list is another built-in function 


for letter in "python": # we can loop over the letters in a string
    print(letter)
    
# The "if" statement

if 3>2:
    print("Three is bigger.") # This is a codeblock
    print("than two.")        #
elif 3<2: 
    print("Three is smaller than two.") # This is another codeblock

# elif is a contraction of "else - if"

# "if" takes a boolean test that is either True or False

True

False

# boolean statements:

1==1 # Common error! "=" vs "=="; Assignment vs test

1==2

1>2

2>1

1>=1

1<=1

2>=1

2<=1

"a" == "b"

"a" == "b"

# Repetition with the while statement

i = 0
while i < 5:
    print(i)
    i = i + 1



# More useful built-in functions:
    
# list & range

list("This is a string")

list(range(1, 10))

# input to get input from the user

myinput = input("write something here.")

myinput


# Our first Python program
# Save the two lines below as a new file called HelloWorld.py

name = input("what is your name? ")
print("Hello", name, ":)")



# Our first Program with our first Function :)
# A function that returns the reverse complement of a DNA sequence.
# Add user input to the function and print its result.

# Your task is to define a function called "reverse_complement".
# The function should take one argument that is a string.
# This string is a DNA sequence.
# The function should return another string
# The returned string should be the reverse complement of a DNA sequence 

# For example
# reverse_complement("tggcta"); should return "tagcca".

# an simple algorithm:
# 1 asking user input and storing this is a variable
# 2 feeding the variable to our function
# 3 complementing each nucleotide in a for loop inside the function
# 4 return the result
# 4 printing out the reverse-complement.
 
# http://shadarf.blogspot.com/2017/07/how-to-make-reverse-complement-of-dna.html














# pCAPs cloning of a 0.5 kb fragment
# using pydna
# see Schlieper et al. 1998 pdf in repository


from pydna.amplify import pcr
from pydna.genbank import Genbank
from pydna.parsers import parse_primers

f,r = parse_primers("""

>f
GATGAGTTCGTGTCCGTACAACT

>r
GGTTATCGAAATCAGCCACAGCG

""")

f

r

gb = Genbank("bjornjobb@gmail.com")

Lambda = gb.nucleotide("J02459.1")

Lambda

# https://en.wikipedia.org/wiki/Lambda_phage

pcr_prod = pcr(f, r, Lambda)

pcr_prod

pcr_prod.figure()

# https://www.ncbi.nlm.nih.gov/nuccore/AJ001614

pcaps = gb.nucleotide("AJ001614.1")

pcaps

from Bio.Restriction import MluNI

pcaps_linear = pcaps.linearize(MluNI)

pcaps_w_insert = (pcaps_linear + pcr_prod).looped()

pcaps_w_insert.seq

from pydna.editor import ape
ape(pcaps_w_insert)




# Simple Plot

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

plt.show()