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

mylist = [1, "Item1", 3.14]

# We can look at each element in a list

mylist[1]

# We can also look at parts of a list (a "slice")

mylist[0:2]

# We can delete a list element using the command "del"

del mylist[1]

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

# There are also user defined functions
# We can package code in a function so that we can reuse it.

def triangle_area(height, width):  # a function name can have no spaces. height, width are arguments
    area = height * width / 2      # This is a **block** of code.
    return area                    # Return something from the function (area).


triangle_area(3, 4)


# The **block** of code is important. That is how Python knows
# what belongs to the function
# Remember this concept, it will be important later.

# Import modules for more functions and other useful things.

import pydna

pydna.logo()

from math import pi

pi

import math

math.pi

import this # The Zen of Python

# Modules are practical if you do not want to have everything in the same
# file. 

### Program flow control statements are "if", "for", and "while".

if 3>2:
    print("Three is bigger.") # This is a codeblock
    print("than two.") 
if 3<2:
    print("Three is smaller than two.") # This is another codeblock

# codeblocks are treated as a group of code

# Repetition with the for statement

mylist

for element in mylist: # for accepts list, string, dict and other "container" types.
    print(element)

# Repetition with the while statement

i = 0
while i < 5:
    print(i)
    i = i +1
    



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



# Our first Function :)
# A function that returns the reverse complement 


# Your task is to define a function called "reverse_complement".
# The function should take one argument that is a string
# This string is a 
# The function should return the reverse complement of a DNA sequence 

# For example, if seq is "tggcta", the function should return "tagcca".







    print(mylist[::2])


        >>> print(range(10))
    range(0, 10)
    >>> rangelist = list(range(10))
    >>> print(rangelist)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for number in range(10):
        # Check if number is one of
        # the numbers in the tuple.
        if number in (3, 4, 7, 9):
            # "Break" terminates a for without
            # executing the "else" clause.
            break
        else:
            # "Continue" starts the next iteration
            # of the loop. It's rather useless here,
            # as it's the last statement of the loop.
            continue
    else:
        # The "else" clause is optional and is
        # executed only if the loop didn't "break".
        pass # Do nothing

    if rangelist[1] == 2:
        print("The second item (lists are 0-based) is 2")
    elif rangelist[1] == 3:
        print("The second item (lists are 0-based) is 3")
    else:
        print("Dunno")

    while rangelist[1] == 1:
        print("We are trapped in an infinite loop!")



In [35]: if value>2:

    ...:     print "good"

    ...: elif value>5:

    ...:     print "better"

    ...: else:

    ...:     print "really good"

good



In [36]: if value>10:

    ...:     print "really good"

    ...: elif value>5:

    ...:     print "better"

    ...: elif value>2:

    ...:     print "really good"

    ...:     

really good



In [37]: if value>10:

    ...:     print "really good"

    ...: elif value>5:

    ...:     print "better"

    ...: elif value>2:

    ...:     print "good"

really good



In [38]: value

Out[38]: 20



In [39]: value=1



In [40]: if value>10:

    ...:     print "really good"

    ...: elif value>5:

    ...:     print "better"

    ...: elif value>2:

    ...:     print "good"



In [41]: if value>10:

    ...:     print "really good"

    ...: elif value>5:

    ...:     print "better"

    ...: elif value>2:

    ...:     print "good"

    ...: else:

    ...:     print "not defined!"

not defined!



In [42]: value=2



In [43]: if value>10:

    ...:     print "really good"

    ...: elif value>5:

    ...:     print "better"

    ...: elif value>2:

    ...:     print "good"

    ...: else:

    ...:     print "not defined!"

not defined!



In [44]: if value>10:

    ...:     print "really good"

    ...: elif value>5:

    ...:     print "better"

    ...: elif value>=2:

    ...:     print "good"

    ...: else:

    ...:     print "not defined!"

good



In [45]: if value>=10:

    ...:     print "really good"

    ...: elif value>=5:

    ...:     print "better"

    ...: elif value>=2:

    ...:     print "good"

    ...: else:

    ...:     print "not defined!"

good



In [46]: if 10=<value:

    ...:     print "really good"

    ...: elif 5=<value<10:

    ...:     print "better"

    ...: elif 2=<value<5:

    ...:     print "good"

    ...: else:

    ...:     print "not defined!"

  File "<ipython-input-46-de68f1112b6d>", line 1

    if 10=<value:

         ^

SyntaxError: invalid syntax





In [47]: if 10<=value:

    ...:     print "really good"

    ...: elif 5<=value<10:

    ...:     print "better"

    ...: elif 2<=value<5:

    ...:     print "good"

    ...: else:

    ...:     print "not defined!"

good



In [48]: value=5



In [49]: if 10<=value:

    ...:     print "really good"

    ...: elif 5<=value<10:

    ...:     print "better"

    ...: elif 2<=value<5:

    ...:     print "good"

    ...: else:

    ...:     print "not defined!"

better



In [50]: def myfunc(value):

    ...:     if 10<=value:

    ...:         print "really good"

    ...:     elif 5<=value<10:

    ...:         print "better"

    ...:     elif 2<=value<5:

    ...:         print "good"

    ...:     else:

    ...:         print "not defined!"



In [51]: myfunc(20)

really good



In [52]: myfunc(1)

not defined!



In [53]: myfunc(5)

better



In [54]: def myfunc(value)

    ...:     if 10<=value:

    ...:         print "really good"

    ...:     elif 5<=value<10:

    ...:         print "better"

    ...:     elif 2<=value<5:

    ...:         print "good"

    ...:     else:

    ...:         print "not defined!"

  File "<ipython-input-54-74ab83858810>", line 1

    def myfunc(value)

                     ^

SyntaxError: invalid syntax





In [55]: def myfunc(value)

    ...:     if 10<=value:

    ...:         print "really good"

    ...:     elif 5<=value<10:

    ...:         print "better"

    ...:     elif 2<=value<5:

    ...:         print "good"

    ...:     else:

    ...:         print "not defined!"





# pCAPs cloning of a 0.5 kb fragment


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

# https://www.ncbi.nlm.nih.gov/nuccore/AJ001614

pcaps = genbank("AJ001614.1")

pcaps

from Bio.Restriction import MluNI

pcaps_linear = pcaps.linearize(MluNI)

pcaps_w_insert = (pcaps_linear + pcr_prod).looped()

pcaps_w_insert.seq





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