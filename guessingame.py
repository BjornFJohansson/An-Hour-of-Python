#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# João Almeida       
from random import randint
number = randint(0, 20)
while True:
    guess = int(input("Guess a number between 0 and 20: "))
    if guess > number:
        print("Too high!")
        if guess - number == 2:
            print("(Close)")
        elif guess - number == 1:
            print("(Very Close)")
    elif guess < number:
        print("Too low!")
        if number - guess == 2:
            print("(Close)")
        elif number - guess == 1:
            print("(Very Close)")
    else:
        print("Correct!")
        break

