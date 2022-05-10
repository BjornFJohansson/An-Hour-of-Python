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

Version 1.1.0
"""




# There are two ways to interact with python, interactively or by 
# saving a text file with the extension ".py" like this file.






 
# Using python interactively will give us a response to each command. 

# This is good for testing out python code lines.

# For programs with several code lines, it is bettwe to save tem in a ".py"
# file.





# Lets get used to the interpreter interactively:

# Lines in this document starting with "#" are comments and ignored by Python

"""   
 _   _                 _                   
| \ | |_   _ _ __ ___ | |__   ___ _ __ ___ 
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| |\  | |_| | | | | | | |_) |  __/ |  \__ \
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |___/
"""                                                   

# An integer number (type: int):
# select the number and click on the "Run selection or current line" button
# above.

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

25/7    # Normal division

25//7   # Floor division

25 % 7  # Modulo division


"""
 __     __         _       _     _                           ___  _     _           _       
 \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___    ___  _ __   / _ \| |__ (_) ___  ___| |_ ___ 
  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|  / _ \| '__| | | | | '_ \| |/ _ \/ __| __/ __|
   \ V / (_| | |  | | (_| | |_) | |  __/\__ \ | (_) | |    | |_| | |_) | |  __/ (__| |_\__ \
    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/  \___/|_|     \___/|_.__// |\___|\___|\__|___/
                                                                     |__/                   
"""

# The equal sign (=) is used to **assign** a
# value to a **variable name**. The value of a name is remembered
# until you leave the Python interpreter.

width = 3

# No result is displayed before the next interactive prompt

width

height = 4

# We can do calculations with variables

area = width * height

area

width = 4 # We can assign a new value that replaces the old value

width

area = width * height

area # Area now gets a new value

# try to access an undefined variable:

# n

# Other datatypes
# We learned that Python has int and float to represent numbers.
# Aditionally, Pyhton has the follwing datatypes:

# - str             Text
# - list            A list of variables or "objects"
# - dict            A dictionary

# There are the aditional data types "tuple" and "set", but we
# will leave them for now.





# A string is good for holding text
# it is made using "" or '' or """

mystring = "This is a text"

mystring # This will give us the content of "mystring"

"""
  ____  _ _      _             
 / ___|| (_) ___(_)_ __   __ _ 
 \___ \| | |/ __| | '_ \ / _` |
  ___) | | | (__| | | | | (_| |
 |____/|_|_|\___|_|_| |_|\__, |
                         |___/ 
"""

# We can look at each letter in a string. This is called slicing.
# The index **always** starts at 0!

mystring[0]

mystring[2]

#  This is a text
#  01234567891111         letters 0 .. 13
#            0123


mystring[13]

# Negative index: 

#  This is a text
#  11119876543210         letters -1 .. - 14
#  3210

mystring[-1]

mystring[-14]

# We can look at parts of a string (a "slice").

mystring[5:7]

# We can look at second to second last letter

mystring[1:-1]


multiline = """This text
has two lines"""

# a new line is denoted by “\n”, also called a Line Feed


multiline

# We can add two strings

mystring + mystring

# Useful! String formatting with fstrings

name = "Zé"
number = 12345

myfstring = f"My name is {name} and my number is {number}"
myfstring

# A list is good for holding an ordered collection of variables or "objects"
# A list can be made using square brackets []
# Lists and strings are similar in many ways, but lists can hold any object
# strings can only hold 

"""
  _     _     _   
 | |   (_)___| |_ 
 | |   | / __| __|
 | |___| \__ \ |_ 
 |_____|_|___/\__|
                  
"""

# We can mix varables in a list:

mylist = [1, "Item1", 3.14, "pizza"]

mylist

# We can look at each element in a list

mylist[1]

# We can also look at parts of a list (a "slice")
# list slice ->  mylist[start:stop:step]

mylist[0:2]    # Lists have ZERO based indexing, just like strings

mylist[1:3]

mylist[1:-1]  # Slicing works the same as for string



# look in the link below for more information
# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types


# Slice     [start:stop:step]

mylist[::2] # We can look at every second element.

mylist[::-1] # We can turn the list around using a negative step.

# We can delete a list element using the command "del"

del mylist[1]

mylist + mylist # We can add two lists together


"""
  ____  _      _   _                              
 |  _ \(_) ___| |_(_) ___  _ __   __ _ _ __ _   _ 
 | | | | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
 | |_| | | (__| |_| | (_) | | | | (_| | |  | |_| |
 |____/|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
                                            |___/ 

"""

# A dictionary (datatype: dict) is a collection of keys and values
# We can mix datatypes for both keys and values

mydict = {"rain": "chuva", "umbrella": "guarda-chuva"}

mydict["umbrella"]

mydict2 = {"Key 1": "Value 1", 2: 3, "pi": 3.14}

mydict["e"] = 2.718  # This is how you add a dictionary value.


"""
  _                 _                  
 | |__   ___   ___ | | ___  __ _ _ __  
 | '_ \ / _ \ / _ \| |/ _ \/ _` | '_ \ 
 | |_) | (_) | (_) | |  __/ (_| | | | |
 |_.__/ \___/ \___/|_|\___|\__,_|_| |_|
                                       
 """


# A boolean variable is either True or False

True
False

# boolean statements:

1==1 # This is a very common error "=" vs "=="; Assignment vs test

1==2

1>2

2>1

1>=1

1<=1

2>=1

2<=1

"a" == "a"

"a" == "b"


# Boolean operators

True and True

True and False

True or True

True or False

False or True

not True

 
True and not True

True or not True

"""
  _____                 _   _                 
 |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
 | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                                              
 """



# functions (built-in)
# A function is a "factory" that accepts input (arguments)
# and returns a result.

# Just like a mathematical function, for example:

#   f(x) = 2x + 3 = y



# The type function is very useful when looking for errors.
# It returns the datatype of a variable.


mystring = "This is a text."

type(mystring)

# The type function returns a result that we can save in a variable

x = type(mystring)

x

print("Hello!")  # Does *not* return anything. **Common source of error**

y = print("Hello!")

y

# The len function gets us the length of a list or a str

basket = ['bread', 'butter', 'milk']

len(basket)


# length of a string

mystring

len(mystring)

# The input function ask the user for input and returns it

z = input("Write something here:")

z

# The sorted function returns a sorted list or str

sorted([3,4,1,2,9])

# The list function makes lists of other variables

list("qwerty")

# The range function returns a range type object

range(1, 10)

list(range(1,10))

int(3.14)

str(3.14)

float("3.14")




"""
  _   _                                          _        _____                 _   _                 
 | | | | ___  _ __ ___   ___ _ __ ___   __ _  __| | ___  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
 | |_| |/ _ \| '_ ` _ \ / _ \ '_ ` _ \ / _` |/ _` |/ _ \ | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 |  _  | (_) | | | | | |  __/ | | | | | (_| | (_| |  __/ |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
 |_| |_|\___/|_| |_| |_|\___|_| |_| |_|\__,_|\__,_|\___| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                                                                                                      
 """
 
# There are also user defined functions.

# We can package our own code in a function so that we can reuse it.


def triangle_area(theight, tlength): # a function name can not have spaces.
    tarea = theight * tlength / 2     # This is a **block** of code.
    return tarea                     # Return something from the function.
    
# height, width are arguments, area is the return value

triangle_area(3, 4)

triangle_area(30, 40)

# The **block** of code is important. That is how Python knows
# what code belongs to the function.
# Remember this concept, it will be important later.
# tarea, theight and tlength are **local variables**


tarea
theight
tlength


# Import modules for more functions and other useful things.
# Modules are simply collections of useful functions.

# The import statement:
    
import this

import math

math.pi

math.log

from math import pi

pi

# Modules are practical if you do not want to have everything in the same
# file. 






### Program flow control statements are "for", "if" and "while".

# Repetition with the for statement
# lets bring back our list from before:

mylist

for element in mylist: # for accepts list, string, dict and other "container" types.
    print(element)     # codeblocks are treated as a group of code.
    

for element in range(5): # We can make a list if we do not have one.
    print(element)

range(10)
list(range(10)) # list is another built-in function 


for letter in "python": # we can loop over the letters in a string
    print(letter)
    
# The "if" statement

if 3>2:
    print("Three is bigger.") # This is a codeblock
    print("than two.")        
elif 3<2: 
    print("Three is smaller than two.") # This is another codeblock
else:
    print("This should never happen!")

# elif is a contraction of "else - if"

# "if" takes a boolean test that is either True or False

True
False



# Repetition with the while statement

i = 0
while i < 5:
    print(i)
    i = i + 1

# Check condition at the end

i = 0
while True:
    print(i)
    i = i + 1
    if i>4:
        break



# More useful built-in functions:
    
# list & range

list("This is a string")

list(range(1, 10))

# input to get input from the user

myinput = input("write something here. ")

myinput


# Our first Python program
# Save the two lines below as a new file called HelloWorld.py

name = input("what is your name? ")
print("Hello", name, ":)")



# Programming task: Number guessing game
# The computer will think of a number between 0 and 20
# The user should make a guess
# The computer 

# How it should work:

# Guess a number between 0 and 20 10
# too high!

# Guess a number between 0 and 20 5
# too high!

# Guess a number between 0 and 20 2
# Correct

# Useful:

#           from random import randint

#           while True:
#               .....


# https://docs.python.org/3/library/random.html#random.randint
# https://docs.python.org/3.9/index.html





