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
        raise ZeroDivisionError("Cannot divide by zero.")

def exp(a, b):
    return a**b


def subtract(a, b):
    return a - b

def logarithm(a, b):
    try:
        if a <= 0 or a == 1:
            raise ValueError
        if b <= 0:
            raise ValueError
        return math.log(b, a)
    except ValueError:
        raise ValueError("Invalid input for logarithm.")


def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of a negative number.")

def hypotenuse(a, b):
    return math.hypot(a, b)
