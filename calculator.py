"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
   return a + b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return 0# raise ZeroDivisionError if a == 0

def exp(a, b):
    return a**b


def subtract(a, b):
    return a - b

def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        return 0

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return 0

def hypotenuse(a, b):
    return math.hypot(a, b)
