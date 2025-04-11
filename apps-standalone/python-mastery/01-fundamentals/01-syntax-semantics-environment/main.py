"""
Python Syntax, Semantics & Environment Demo

Key concepts demonstrated with detailed explanations:
1. Dynamic typing - Variables can change type dynamically
2. Indentation-based blocks - Python's unique scoping approach
3. Naming conventions - PEP 8 style guidelines
4. Basic syntax elements - Core language features
"""

# ========== 1. DYNAMIC TYPING ==========
# Python is dynamically typed - variable types are determined at runtime
# and can be changed during execution

print("\n=== DYNAMIC TYPING ===")

# Variable starts as integer
a = 5  # type: int
print(f"a is {a}, type: {type(a)}")  # Output shows integer type

# Same variable reassigned to string (dynamic typing demo)
a = "hello"  # type: ignore
print(f"a is {a}, type: {type(a)}")  # Shows type changed

# Reassigned again to list (dynamic typing demo)
a = [1, 2, 3]  # type: ignore
print(f"a is {a}, type: {type(a)}")  # Type changed again


# ========== 2. INDENTATION-BASED BLOCKS ==========
# Python uses indentation (whitespace) to define code blocks instead
# of curly braces {} like many other languages

print("\n=== INDENTATION-BASED BLOCKS ===")


def greet(name):
    """
    Function demonstrating indentation:
    - The entire function body is indented
    - Control structures within are further indented
    """
    if name:  # if block starts with indentation
        print(f"Hello, {name}!")  # if body indented further
    else:
        print("Hello, stranger!")  # else body at same level


# Function calls must be at proper indentation level
greet("Alice")  # Properly aligned with module-level code
greet("")


# ========== 3. NAMING CONVENTIONS ==========
# Python follows PEP 8 style guide for naming:

print("\n=== NAMING CONVENTIONS ===")

# Variables and functions use snake_case
my_variable = 42  # All lowercase with underscores


def my_function():  # Function names follow same convention
    pass


# Constants use UPPER_SNAKE_CASE
MAX_CONNECTIONS = 5  # Clearly indicates constant value
PI_APPROXIMATION = 3.14159


# Classes use PascalCase (also called CapitalizedCase)
class MyClass:  # Each word capitalized, no separators
    pass


# ========== 4. BASIC SYNTAX ELEMENTS ==========

print("\n=== BASIC SYNTAX ELEMENTS ===")

# Comments: Single line starts with #
""" 
Multi-line comments/documentation 
use triple quotes (technically docstrings)
"""

# Operators follow standard precedence
x = 5 + 3 * 2  # Multiplication before addition
print(f"5 + 3 * 2 = {x}")  # Output: 11 not 16

# Modern string formatting with f-strings (Python 3.6+)
name = "Bob"
age = 25
print(f"{name} is {age} years old")  # Variables embedded directly

# List comprehensions - concise way to create lists
squares = [x**2 for x in range(5)]  # Equivalent to map+lambda
print(f"Squares: {squares}")

# Environment note: Requires Python 3.6+ for f-strings
# Run with: python main.py
