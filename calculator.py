"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
   return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return 0# raise ZeroDivisionError if a == 0

def log(a, b):
    try:
        math.log(a,b)
    except ValueError:
        return 0# use math library + raise ValueError

def exp(a, b):
    return a**b



