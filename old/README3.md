
# An-Hour-of-Python

Steve Jobs once [said](https://youtu.be/IY7EsTnUSxY?t=2) “Everybody in this country should learn to program a computer, because it teaches you how to think”.

I fully agree with this, programming is just not a way to solve problems or get things done. As you progress to gain more knowledge, you will see how your coding skills can affect the ways you think. After all, if you know a problem well enough to describe it to a computer, you probably know it better than most. This [TED talk](https://youtu.be/xfBWk4nw440?t=24) (10 min) sums up the argument in a nice way. The speaker has a website [here](https://christian.gen.co/you-should-learn-to-program).

Python i a general programming language, the world's most popular programming language in 2019 and its popularity has [only increased since](https://pypl.github.io/PYPL.html). Python is especially popular in the fields of [data science](https://en.wikipedia.org/wiki/Data_science) and [bioinformatics](https://en.wikipedia.org/wiki/Bioinformatics), two fields that should be of interest to a student of biology.

Python is known to have a simple compact syntax and easily readable code since it contains few special characters, such as semicolons.

Compare the two programs below, the first one in C++, another popular coding language and then the same program in Python.

### C++

```C++
// This C++ program prints Hello, World!
#include <iostream>

int main()
{
    std::cout << "Hello, World! \n";
    return 0;
}
```

### Python

```python
# This Python program prints Hello, World!
print("Hello, World! \n")
```

Because of its simplicity, Python is suitable for beginners and for people who do not code every day (like me). It is suitable both for scripts for automation of some repetitive task but also for complex software with graphical interfaces.

One of the most important advantages of Python is the large size of its community, since this means that you can often find questions and answers to your coding problems by a simply searching with google.

Python is used for everything from

- Graphical User Interface ([gui](https://github.com/BjornFJohansson/seguid_calculator)) for sequence checksums.
- Stock and cryptocurrency trading ([video](https://youtu.be/GdlFhF6gjKo)).
- Population dynamics ([blog](https://towardsdatascience.com/building-population-models-in-python-57f9e174d27d))
- Reading data from a commercial temperature data logger ([package](https://github.com/civic/elitech-datareader)).
- Controlling the height of a standing desk [code](https://pypi.org/project/idasen) [video](https://youtu.be/LEXQOhEzVhE?t=404).

We will spend one hour learning the basics of Python using simple examples. The exercises are aimed at complete beginners with no previous programming experience.

The tutor will demonstrate the basic data
types and repetition and decision making in the logical flow of a program.We will use the [Spyder](https://www.spyder-ide.org) integrated development environment (IDE). At the end we will code some simple examples relevant to biology/bioinformatics.

Python will be used to search sequence data on Genbank using pydna and
formalize a simple cloning procedure.

### Exercises

The Spyder editor was installed with the Anaconda distribution that you should have installed before this class ([See instructions here](ddd)).

Start Spyder from the start menu of your computer.

![](Spyder)

Spyder has two important parts, the text editor to the left and the

```
# Using Python interactively
Calculations in spyder
data types


other useful data types
int
str
list
dict
tuple and set
functions
print()
user defined
The first program "Hello_World.py" manipulate text read/write files Command line input

### Assignment, variables and calculations https://www.stavros.io/tutorials/python

    myvar = 1
    other = 2
    mycar + other

### Import libraries for more functions

    from math import pi
    pi

### Data types

    sample = [1, ["another", "list"], ("a", "tuple")]
    mylist = ["List item 1", 2, 3.14]
    mylist[0] = "List item 1 again" # We're changing the item.
    mylist[-1] = 3.21 # Here, we refer to the last item.
    mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
    mydict["pi"] = 3.15 # This is how you change dictionary values.
    mytuple = (1, 2, 3)
    myfunction = len
    print(myfunction(mylist))

### Slice

    mylist = ["List item 1", 2, 3.14]

    print(mylist[:])

    print(mylist[0:2])

    print(mylist[-3:-1])

    print(mylist[1:])

    # Adding a third parameter, "step" will have Python step in
    # N item increments, rather than 1.
    # E.g., this will return the first item, then go to the third and
    # return that (so, items 0 and 2 in 0-indexing).

    print(mylist[::2])

### Flow control statements are if, for, and while.

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


### Functions


    # Same as def funcvar(x): return x + 1
    funcvar = lambda x: x + 1
    >>> print(funcvar(1))
    2

    # an_int and a_string are optional, they have default values
    # if one is not passed (2 and "A default string", respectively).
    def passing_example(a_list, an_int=2, a_string="A default string"):
        a_list.append("A new item")
        an_int = 4
        return a_list, an_int, a_string

    >>> my_list = [1, 2, 3]
    >>> my_int = 10
    >>> print(passing_example(my_list, my_int))
    ([1, 2, 3, 'A new item'], 4, "A default string")
    >>> my_list
    [1, 2, 3, 'A new item']
    >>> my_int
    10




```
https://replit.com