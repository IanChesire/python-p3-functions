#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")
greet("Chief")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default('Bee')

def add(num1, num2):
    return num1 + num2
add(5, 6)

def halve(number):
    return number / 2
halve(7)
