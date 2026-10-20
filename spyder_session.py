#             /^\/^\
#           _|__|  O|
# \/     /~     \_/ \
#   \____|__________/  \
#         \_______      \
#                 `\     \                 \
#                   |     |                  \
#                   /      /                    \
#                 /     /                       \\
#               /      /                         \ \
#               /     /                            \  \
#             /     /             _----_            \   \
#           /     /           _-~      ~-_         |   |
#           (      (        _-~    _--_    ~-_     _/   |
#           \      ~-____-~    _-~    ~-_    ~-_-~    /
#             ~-_           _-~          ~-_       _-~
#                 ~--______-~                ~-___-~

#                   _                               __
#     /\           | |                             / _|
#    /  \   _ __   | |__   ___  _   _ _ __    ___ | |_
#   / /\ \ | '_ \  | '_ \ / _ \| | | | '__|  / _ \|  _|
#  / ____ \| | | | | | | | (_) | |_| | |    | (_) | |
# /_/    \_\_| |_| |_| |_|\___/ \__,_|_|     \___/|_|


#  _____       _   _
# |  __ \     | | | |
# | |__) |   _| |_| |__   ___  _ __
# |  ___/ | | | __| '_ \ / _ \| '_ \
# | |   | |_| | |_| | | | (_) | | | |
# |_|    \__, |\__|_| |_|\___/|_| |_|
#         __/ |
#         |___/

# Version 1.3.0

# This file is a Python source file called "spyder_session.py"
# It is meant to showcase important parts of Python 3 syntax

# Text starting with # like this one is a comment and is ignored by Python.

# There are two ways to interact with Python, interactively or by
# saving a text file with the extension ".py" like this file.

# Working interactively in Spyder:

# Run examples in order so that their variables have been defined.
# Select an entire function, loop, or if/elif/else statement, including all
# its indented lines, before executing it. Use four spaces per indentation
# level; do not mix tabs and spaces.

# The indentation groups the code in a code block.
# Defining a function stores its instructions; calling it runs them.
# After editing a function, execute its definition again before calling it.
# If a result seems inconsistent, check for variables left over from earlier
# work. Restarting the kernel clears them; then rerun the needed definitions.
# Intentional error examples are commented out. Try them one at a time.


# Let's get used to using the interpreter interactively:

r"""
 _   _                 _
| \ | |_   _ _ __ ___ | |__   ___ _ __ ___
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| |\  | |_| | | | | | | |_) |  __/ |  \__ \
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |___/
"""
# Two common numeric data types are int and float.

# An integer number (type: int):
# select the number and click on the "Run current line or selection" button
# above.

5

type(5)

# A floating-point number (type ?)
# What is type()
# What is a type?

3.14159265359

type(3.14159265359)

# We can use simple arithmetic such as addition

2 + 2

# A mathematical expression (Python follows PEMDAS https://en.wikipedia.org/wiki/Order_of_operations)

50 - 5 * 6

# Division "/" returns a float, even for integer division.

(50 - 5 * 6) / 4

# The ** operator calculate powers

5 ** 2  # 5 squared

2 ** 7  # 2 to the power of 7

355 / 113    # Normal division, returns a float

355 // 113    # Floor division, rounds the quotient down

# The % modulo operator gives the remainder after dividing two
# one number by another.

# Example: 100 % 9 is equal to 1
# Because 100/9 is 11.11 ....
# The integer part of the quotient is 11
# 11 * 9 = 99, and 100-99 is 1

100 % 9

# Another example: 14 mod 12 equals 2.
# This because 14/12 = 1 with a remainder of 2.

355 % 113  # Why is this 16?

5 % 2 # = 1 because 2 fits into 5 twice, leaving a remainder of 1

9 % 3 # = 0 because 3 fits into 9 three times evenly, leaving no remainder

10 % 4 # = 2 because 4 fits into 10 twice, leaving 2 left over.

# Checking if number % 2 == 0 tells you if a number is even (remainder 0)
# or odd (remainder 1)

33 % 2  # uneven
34 % 2  # even

# Gotcha!

-2 % 2  # not what we expect... this does not work for negative numbers.


r"""
 __     __         _       _     _                           ___  _     _           _
 \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___    ___  _ __   / _ \| |__ (_) ___  ___| |_ ___
  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|  / _ \| '__| | | | | '_ \| |/ _ \/ __| __/ __|
   \ V / (_| | |  | | (_| | |_) | |  __/\__ \ | (_) | |    | |_| | |_) | |  __/ (__| |_\__ \
    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/  \___/|_|     \___/|_.__// |\___|\___|\__|___/
                                                                     |__/
"""

# The equal sign (=) is used to **assign** a
# value to a **variable name**.

# The name keeps its value until you reassign or delete it.

rectangle_width = 3

# No result is displayed before the next interactive prompt

rectangle_width

rectangle_height = 4

# We can do calculations with variables

area = rectangle_width * rectangle_height

area

rectangle_width = 4  # We can assign a new value that replaces the old value

rectangle_width

area  # this should not change the area

area = rectangle_width * rectangle_height # we can calculate the area again.

area  # Display the new value calculated on the previous line

# try to access an undefined variable "n":

# remove the "#" on the line below and execute the line to test.
# n


# Other data types
# We learned that Python has int and float to represent numbers.
# Additionally, Python has the following data types:

# - str             Text
# - list            An ordered collection of objects
# - dict            A dictionary

# There are the additional data types "tuple" and "set", but we
# will leave them for now.

r"""
 _____ _        _                __      _         __
/  ___| |      (_)              / /     | |        \ \
\ `--.| |_ _ __ _ _ __   __ _  | |   ___| |_ _ __   | |
 `--. \ __| '__| | '_ \ / _` | | |  / __| __| '__|  | |
/\__/ / |_| |  | | | | | (_| | | |  \__ \ |_| |     | |
\____/ \__|_|  |_|_| |_|\__, | | |  |___/\__|_|     | |
                         __/ |  \_\                /_/
                        |___/
"""


# A string is useful for holding text
# it is made using "" or '' or """

mystring = "This is a text"

mystring = 'This is a text'

mystring = 'This is the "best" text'

mystring = "This is the 'best' text"

# mystring = "This is the "best" text"    # does not work!

mystring      # This will give us the content of "mystring"

r"""
  ____  _ _      _
 / ___|| (_) ___(_)_ __   __ _
 \___ \| | |/ __| | '_ \ / _` |
  ___) | | | (__| | | | | (_| |
 |____/|_|_|\___|_|_| |_|\__, |
                         |___/
"""

# We can look at each character in a string. This is called indexing.
# Positive indexing starts at 0; negative indices count from the end.

mystring = "Thisisatext"

mystring[0]

mystring[2]

#  Thisisatext        indexing starts with 0 in Python.
#  01234567891        letters 0 .. 10  (total 11)
#            0

mystring[-1]

# Negative indices: -1 is the last character; -11 is the first here.

# Character: T---h---i--s--i--s--a--t--e--x--t
# Index:    -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

mystring[-11]

# We can look at parts of a string (a "slice").

mystring[4:7]

# Note that the coordinates are [including: excluding]
# We can look at the second through the second-to-last characters.

mystring[1:-1]

multiline = """This text
has two lines"""

# a new line is denoted by “\n”, also called a line feed

multiline

# We can add two strings

mystring + mystring

# String methods: working with DNA copied from a document
# A method is called with a dot after the object, followed by parentheses.

# A method is a function that belongs to an object.

# An Object is the actual data container that lives in your
# computer's memory. It contains the actual value (like 5 or "apple"),
# a specific data type, and a unique identity (memory address).
# In Python, everything is an object.

copied_dna = "  atgcca  "

copied_dna.strip()  # Removes whitespace at the ends, not internal spaces
copied_dna          # Still contains the original spaces and lowercase letters

clean_dna = copied_dna.strip()
clean_dna.upper()  # Returns a new string; clean_dna itself is unchanged
clean_dna

clean_dna = clean_dna.upper()  # Save the new value by assigning it
clean_dna                      # Expected: "ATGCCA"

# Strings are immutable: their individual characters cannot be changed.
# Uncomment the line below and execute the line to see a TypeError:
# clean_dna[0] = "G"

clean_dna.count("C")           # Expected: 2
clean_dna.replace("A", "a")    # Expected: "aTGCCa"; replaces every A
clean_dna.startswith("ATG")    # Expected: True
clean_dna                      # Still "ATGCCA"

# count counts non-overlapping occurrences of a substring.
"AAAA".count("AA")             # Expected: 2, not 3

# Checkpoint: predict copied_dna and clean_dna before displaying them.

# Useful! String formatting with f-strings

name = "Zé"
number = 12345

myfstring = f"My name is {name} and my number is {number}"
myfstring


r"""
  _     _     _
 | |   (_)___| |_
 | |   | / __| __|
 | |___| \__ \ |_
 |_____|_|___/\__|

"""

# A list is good for holding an ordered collection of objects.
# A list can be made using square brackets []
# Lists and strings are similar in many ways, but a list can hold any object.
# Strings contain only text characters.

# We can mix objects of different types in a list:

mylist = [1, "Item1", 3.14, "pizza"]

mylist

# We can look at each element in a list

mylist[1]

# We can also look at parts of a list (a "slice")
# This concept is the same as the one for strings before.
# list slice ->  mylist[start:stop:step]

mylist[0:2]    # Lists have zero-based indexing, just like strings

mylist[1:3]

mylist[1:-1]  # Slicing works the same as for strings

# look in the link below for more information
# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types

# Slice     [start:stop:step]

mylist[::2] # We can look at every second element.

mylist[::-1] # We can turn the list around using a negative step.

# We can delete a list element using the command "del"

del mylist[1]

mylist + mylist # We can add two lists together

# We can add a list element using the method "append"

mylist.append("newitem")


r"""
  ____  _      _   _
 |  _ \(_) ___| |_(_) ___  _ __   __ _ _ __ _   _
 | | | | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
 | |_| | | (__| |_| | (_) | | | | (_| | |  | |_| |
 |____/|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
                                            |___/

"""

# A dictionary (data type: dict) is a collection of keys and values
# We can mix data types for both keys and values. Keys must be hashable
# (for example, strings or numbers; lists cannot be dictionary keys).

mydict = {"rain": "chuva", "umbrella": "guarda-chuva"}

mydict["umbrella"]

mydict2 = {"Key 1": "Value 1", 2: 3, "pi": 3.14}

mydict2["Key 1"]
mydict2[2]

mydict["e"] = 2.718  # This is how you can add a dictionary value.


r"""
  _                 _
 | |__   ___   ___ | | ___  __ _ _ __
 | '_ \ / _ \ / _ \| |/ _ \/ _` | '_ \
 | |_) | (_) | (_) | |  __/ (_| | | | |
 |_.__/ \___/ \___/|_|\___|\__,_|_| |_|

"""


# A boolean variable is either True or False

True
False

# Important, True and False are case sensitive
# true and false have no meaning.

# boolean statements:

1==1 # This is a very common error "=" vs "=="; Assignment vs test for equivalence

1==2

1>2

2>1

1>=1

1<=1

2>=1

2<=1

"a" == "a"  # is "a" equal to "a"?

"a" == "b"

"a" == "A"

"a".upper() == "A".upper() # works!
"a".lower() == "A".lower() # works!

# Membership tests: "in" and "not in" return True or False.
# In a string, membership checks for a substring, not just one character.

"G" in "ACGT"          # Expected: True
"N" not in "ACGT"      # Expected: True
"ATG" in "CCATGAA"     # Expected: True
"ATG" in "atg"         # Expected: False; comparisons are case-sensitive

# In a list, membership checks for an element.
"sample_B" in ["sample_A", "sample_B"]  # Expected: True

# In a dictionary, membership checks the keys.
"rain" in mydict       # Expected: True
"chuva" in mydict      # Expected: False; chuva is a value here

# != means "not equal".
"A" != "T"             # Expected: True


# Boolean operators

True and True

True and False

True or True

True or False

False or True

False or False

not True

True and not True

True or not True

r"""
  _____                 _   _
 |  ___|   _ _ __   ___| |_(_) ___  _ __  ___
 | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/

 """



# functions (built-in)
# A function groups reusable code. It can accept input (arguments)
# and return a result; if no return value is specified, it returns None.

# Just like a mathematical function, for example:

#   f(x) = 2x + 3 = y

# The type function is very useful when looking for errors.
# It returns the data type of an object.

mystring = "This is a text."

type(mystring)
type(rectangle_width)

# The type function returns a result that we can save in a variable

x = type(mystring)

x

# The built in "print" function displays text and returns None.
# Important! Common source of error

print("Hello!")

y = print("Hello!")

y

# The len function gets us the length of a list or a str

basket = ['bread', 'butter', 'milk']

len(basket)

# length of a string

mystring

len(mystring)

# The input function asks the user for input and returns it as a string.

z = input("Write something here:")

z

y = print("Write something here:")

# Observe the difference: z holds the input string, while y is None.

# The sorted function returns a new sorted list, even if its input is a string.
# It does not change the original collection.

mylist2 = [3,4,1,2,9]

sorted(mylist2)

mylist2.sort()    # This is an important example of a method that changes the object!

mylist2

# We can also sort a list of strings:

sorted(["Zé", "Ana"])

# The list function makes a list from an iterable, such as a string:

zzz = list("qwerty")

# Lists are mutable, so we can change one element like this:

zzz[3] = "X"

zzz

# str(zzz) returns a representation of the list, including brackets and quotes.
# It does not join the characters into a single word.

str(zzz)

# Instead we have to use the string join method:

"".join(zzz)

# This may seem strange, but it actually makes sense

# The range function returns a range type object
# This is useful for a sequence of integers; the stop value is excluded.

list(range(10))

range(1, 10)

int(3.14)

str(3.14)

str(3.14) + str(3.14)

float("3.14")

int("314")



r"""
  _   _                                          _        _____                 _   _
 | | | | ___  _ __ ___   ___ _ __ ___   __ _  __| | ___  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___
 | |_| |/ _ \| '_ ` _ \ / _ \ '_ ` _ \ / _` |/ _` |/ _ \ | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 |  _  | (_) | | | | | |  __/ | | | | | (_| | (_| |  __/ |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
 |_| |_|\___/|_| |_| |_|\___|_| |_| |_|\__,_|\__,_|\___| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/

 """

# There are also user-defined functions.
# We can package our own code in a function so that we can reuse it.
# height and width are parameters; the value of triangle_area is returned.

# my_function <- function() { # create a function with the name my_function in R
#   print("Hello World!")
#   return(value)
# }

# triangle and triangle_bad are two user-defined functions:

def triangle(height, width):              # a function name cannot have spaces.
    triangle_area = height * width / 2    # This is a **code block**.
    return triangle_area                  # Return something from the function.

def triangle_bad(height, width):
    triangle_area = height * width / 2
    print(triangle_area)
    return

# The second function "triangle_bad" represents a common mistake.
# It seems to produce a result since the print function gives an output
# but the function returns None because the return statement has no value.

aaa = triangle(30, 40)

bbb = triangle_bad(30, 40)

# compare the content of variables aaa and bbb!

# The **code block** is an important concept.
# That is how Python knows what code belongs to the function.
# Remember this idea, it will be important later.
# triangle_area, height and width are **local variables**
# They are not defined outside the function. Run each line below separately
# to see the intentional NameError; then continue with the next section:

# Test these (remove the #):

# triangle_area
# height
# width

# Reading a function stub: pass does nothing

def label_sample(sample):
    """Return a sample name with the prefix 'Sample: '."""
    pass


# sample: str describes the expected input type; -> str describes the result.
# Type hints document expectations; they do not enforce or convert types.
# The triple-quoted text inside the function is its documentation (docstring).
# pass is a placeholder that does nothing. With no return, the result is None.

print("Expected after implementation: Sample: yeast | Result:", label_sample("yeast"))
help(label_sample)  # Displays the docstring and function signature

# To implement this stub, replace pass with:
#     return "Sample: " + sample
# Then select and execute the whole definition again before repeating the call.
# In the project, list[int] means a list of integers, and str | None means
# either a string or None. None represents the absence of a result.

print("Expected: True | Result:", label_sample("yeast") is None)
# The last example describes the unfinished stub, not its intended final result.

# Import modules for more functions and other useful things.
# Modules can contain functions, constants, classes, and other code.

# The import statement:

import math

math.pi

math.log(2)

# see the content of "math" here
# https://docs.python.org/3/library/math.html#math.pi

# We can also import one thing at a time:
from math import pi

pi

# The Zen of Python:
import this

# Modules are practical if you do not want to have everything in the same
# file.
r"""
______ _
|  ___| |
| |_  | | _____      __
|  _| | |/ _ \ \ /\ / /
| |   | | (_) \ V  V /
\_|   |_|\___/ \_/\_/

"""

### Program flow control statements are "for", "if" and "while".

# for (x in 1:10) {    # This is a loop in R
#   print(x)
# }

for x in range(10):          # The same loop in Python
    print(x)

# Repetition with the for statement
# Let's bring back our list from before:

mylist

for element in mylist: # for accepts list, string, dict and other "container" types.
    print(element)     # code blocks are treated as a group of code.


for element in range(5): # range supplies a sequence of integers without making a list.
    print(element)


range(10)
list(range(10)) # list is another built-in function


for letter in "python": # we can loop over the letters in a string
    print(letter)

# Let's bring back our dict from before:
mydict

for key in mydict: # We can loop over the keys in a dictionary.
    print(key)

# The "if" statement

if 3 > 2:
    print("Three is bigger")  # This is a
    print("than two.")         # code block
elif 3 < 2:
    print("Three is smaller than two.")  # This is another code block
else:
    print("This should never happen!")

# elif is a contraction of "else - if"
# An if statement has one if, zero or more elif clauses, and an optional else.

# "if" tests whether a condition is true; these comparisons return True or False.

True
False

# Combining loops, conditions, and functions for biological data
# The next examples practise techniques you can reuse in project01.py.

# Building a result: collect the lengths of several DNA fragments.


def fragment_lengths(fragments):
    """Return one length for each fragment, in the same order."""
    lengths = []                  # Start a fresh list for each call
    for fragment in fragments:
        lengths.append(len(fragment))
    return lengths                # Outside the loop: return after ALL fragments


print("Expected: [3, 4, 0] | Result:", fragment_lengths(["ATG", "CCAA", ""]))
print("Expected: [] | Result:", fragment_lengths([]))
# If return were inside the loop, only the first fragment would be processed.
# append changes the list and returns None: do not write lengths = lengths.append(...).

# Conditions inside functions: select a result using a comparison.


def length_status(sequence, minimum):
    """Classify a fragment using a supplied minimum length."""
    if len(sequence) < minimum:
        return "too short"
    return "long enough"


print("Expected: too short | Result:", length_status("ATG", 4))
print("Expected: long enough | Result:", length_status("ATGC", 4))

# Early return: find the first fragment that meets a length threshold.


def first_long_fragment(fragments, minimum):
    """Return the first sufficiently long fragment, or None if none qualifies."""
    for fragment in fragments:
        if len(fragment) >= minimum:
            return fragment       # Exits the ENTIRE function, including the loop
    return None                   # Reached only after all fragments were checked


print("Expected: ATGC | Result:", first_long_fragment(["A", "ATGC", "GGGGG"], 4))
print("Expected: None | Result:", first_long_fragment(["A", "TT"], 4))
# break exits a loop; return exits a function.
# Checkpoint: why must return None be outside the loop?

# Counting with a loop: start at zero, then update the counter conditionally.

fragment_count = 0
for fragment in ["ATG", "A", "GGCC"]:
    if len(fragment) >= 3:
        fragment_count = fragment_count + 1

print("Expected: 2 | Result:", fragment_count)
# fragment_count += 1 is a shorter way to write the same increment.

# A stepped range: inspect every third position in a sequence.
# range(start, stop, step) excludes stop, just like slicing.

sequence = "ATGCCATA"
list(range(0, len(sequence), 3))  # Expected: [0, 3, 6]

for position in range(0, len(sequence), 3):
    print(position, sequence[position])  # Expected: 0 A, then 3 C, then 6 T

# Checkpoint: what changes if the start is 1? What if the sequence is empty?
# When extracting triplets, check for an incomplete triplet at the end.

# Checking results: use examples where you know the answer in advance.

print("Expected: [2, 4] | Result:", fragment_lengths(["AT", "GGCC"]))
assert fragment_lengths(["AT", "GGCC"]) == [2, 4]
assert fragment_lengths([]) == []
assert length_status("ATGC", 4) == "long enough"
assert first_long_fragment(["A"], 4) is None

# An assert is silent when the condition is True. If False, it raises
# AssertionError. Uncomment this deliberately wrong expectation to see it:
# assert fragment_lengths(["AT"]) == [3]
# Use assertions to check your code, not to validate user input.
# Include a typical example, a boundary case, and an example with no match.

# Errors and input validation
# A traceback tells you where an error occurred. Read its final line for
# the error type and message, then inspect the indicated line in your code.
# NameError: a name is undefined. TypeError: an operation has the wrong type.
# ValueError: the input type is suitable, but its value is not allowed.
# IndexError: an index is outside the sequence. IndentationError: check spaces.


def checked_length_status(sequence, minimum):
    """Classify a fragment; reject a negative minimum length."""
    if minimum < 0:
        raise ValueError("minimum must be zero or greater")
    return length_status(sequence, minimum)  # Reuse a function already defined


print("Expected: long enough | Result:", checked_length_status("ATGC", 4))
# Try the invalid input separately to inspect its traceback:
# checked_length_status("ATGC", -1)

# Optional: handle an expected error with try/except so execution can continue.
# Select the entire try/except block before running it.
try:
    checked_length_status("ATGC", -1)
except ValueError as error:
    print("Expected: minimum must be zero or greater | Result:", error)

# Catch the specific error you expect. Other errors may indicate a coding bug.


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

# Python has no repeat - until construct

# More useful built-in functions:

# list & range

list("This is a string")

list(range(1, 10))

# input to get input from the user

myinput = input("write something here. ")

myinput


# Our first Python program
# copy and save the two lines below as a new file called HelloWorld.py

name = input("what is your name? ")
print("Hello", name, ":)")

r"""
__   __                  __ _          _                 _     _
\ \ / /                 / _(_)        | |               | |   | |
 \ V /___  _   _ _ __  | |_ _ _ __ ___| |_   _ __  _   _| |__ | |_ ___  _ __    _ __  _ __ ___   __ _ _ __ __ _ _ __ ___
  \ // _ \| | | | '__| |  _| | '__/ __| __| | '_ \| | | | '_ \| __/ _ \| '_ \  | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \
  | | (_) | |_| | |    | | | | |  \__ \ |_  | |_) | |_| | | | | || (_) | | | | | |_) | | | (_) | (_| | | | (_| | | | | | |
  \_/\___/ \__,_|_|    |_| |_|_|  |___/\__| | .__/ \__, |_| |_|\__\___/|_| |_| | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_|
                                            | |     __/ |                      | |               __/ |
                                            |_|    |___/                       |_|              |___/

"""

# Turning keyboard input into a number
# input always returns a string, even when the user types digits.

text_guess = "7"  # An example of what input would return
numeric_guess = int(text_guess)
print("Expected: 8 | Result:", numeric_guess + 1)

# Run this line separately when you are ready to type an integer:
# guess = int(input("Your guess: "))
# Entering text such as "seven" raises ValueError. To handle this, you can
# put the conversion inside try/except ValueError, as shown above.
# Checkpoint: why would text_guess + 1 fail?


# Programming task: Number guessing game

# The computer will think of a number between 0 and 20
# The user should then guess the number.
# The computer should evaluate each guess with "too high!",
# or "too low!", "Correct"
# The game should continue until the user has guessed the number.

# Example of how it should work:

# Guess a number between 0 and 20 10
# too high!

# Guess a number between 0 and 20 5
# too low!

# Guess a number between 0 and 20 7
# Correct

# Useful:

#     from random import randint
#
#     The randint function gives us an
#     integer between a and b, including both endpoints:
#     randint(0, 20)

#     https://docs.python.org/3/library/random.html#random.randint


#     while True:
#         .....
#
#     The while True loop is useful as it continues until we give a
#     break statement.
