"""
Python Syntax, Semantics & Environment Demo

Key concepts demonstrated:
1. Dynamic typing
2. Indentation-based blocks
3. Naming conventions
4. Basic syntax elements
"""

# 1. Dynamic typing example
# Variables don't have fixed types, they can change type

print("\n=== DYNAMIC TYPING ===")

# Integer
a = 5  # integer
print(f"a is {a}, type: {type(a)}")

# String
a = "hello"  # now a string
print(f"a is {a}, type: {type(a)}")

# List
a = [1, 2, 3]  # now a list
print(f"a is {a}, type: {type(a)}")


# 2. Indentation-based blocks (vs braces in other languages)

print("\n=== INDENTATION-BASED BLOCKS ===")


def greet(name):
    # This indented block is part of the function
    if name:  # Another indented block for the if statement
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")


# Proper indentation is required
greet("Alice")
greet("")

# 3. Naming conventions

print("\n=== NAMING CONVENTIONS ===")

# Variables/functions: snake_case
my_variable = 42


def my_function():
    pass


# Constants: UPPER_SNAKE_CASE
MAX_CONNECTIONS = 5
PI_APPROXIMATION = 3.14159


# Classes: PascalCase
class MyClass:
    pass


# 4. Basic syntax elements

print("\n=== BASIC SYNTAX ELEMENTS ===")

# Comments start with #
""" Multi-line
    comments use triple quotes """

# Basic operators
x = 5 + 3 * 2  # Follows operator precedence
print(f"5 + 3 * 2 = {x}")

# String formatting (f-strings)
name = "Bob"
age = 25
print(f"{name} is {age} years old")

# List comprehensions
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Environment note: This assumes Python 3.6+ for f-strings
# Run with: python3 syntax_demo.py
