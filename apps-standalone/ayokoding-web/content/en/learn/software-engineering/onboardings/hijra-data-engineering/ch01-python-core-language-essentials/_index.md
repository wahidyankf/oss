---
title: '01 - Python Core Language Essentials'
date: 2025-04-17T07:20:00+07:00
draft: false
weight: 2
---

## Overview

This chapter covers fundamental Python concepts that form the foundation of data engineering code. We'll learn how to write clean, maintainable code for data pipelines by focusing on:

- Python syntax and data types
- Control flow (if statements and loops)
- Functions for reusable code
- Data structures for organizing information
- String manipulation for formatting data
- List comprehensions for concise data transformation
- Essential modules from the standard library

This 52-minute session will give you the core Python skills needed for data engineering work.

Let's start building your Python toolkit for data engineering!

## 1. Python Syntax and Data Types

### Variables and Assignment

Variables are containers for storing data values. In Python, you don't need to declare variable types - the interpreter automatically determines the type.

```python
# Assign a value to a variable
count = 10  # An integer
price = 19.99  # A floating-point number
name = "Sales Report"  # A string
is_valid = True  # A boolean

# Python allows you to reassign variables to different types
count = "Ten"  # Now count is a string

# Print variables to see their values
print("count:", count)  # count: Ten
print("price:", price)  # price: 19.99
print("name:", name)  # name: Sales Report
print("is_valid:", is_valid)  # is_valid: True
```

### Basic Data Types

Python has several built-in data types with specific implementation characteristics:

```python
# Integers - whole numbers without decimal points
quantity = 42
year = 2023

# Floating-point numbers - numbers with decimal points
price = 19.99
discount_rate = 0.15

# Strings - text enclosed in quotes (single or double)
product_name = "Data Engineering Toolkit"
category = 'Software'
multiline_text = """This is a
multiline string that can
span multiple lines"""

# Booleans - True or False values, useful for conditions
is_available = True
has_discount = False

# None - represents the absence of a value
next_shipment = None

# Print variable types
print("Type of quantity:", type(quantity))  # Type of quantity: <class 'int'>
print("Type of price:", type(price))  # Type of price: <class 'float'>
print("Type of product_name:", type(product_name))  # Type of product_name: <class 'str'>
print("Type of is_available:", type(is_available))  # Type of is_available: <class 'bool'>
print("Type of next_shipment:", type(next_shipment))  # Type of next_shipment: <class 'NoneType'>
```

**Implementation details:**

1. **Integers (int)**:

   - Python integers have unlimited precision (they can be arbitrarily large)
   - Implemented using variable-length arrays of digits in base 2³⁰
   - Small integers (-5 to 256) are pre-allocated for efficiency
   - Memory usage grows with the size of the integer
   - Operations between very large integers can be slower

   ```python
   # Unlimited precision example
   very_large = 2**100  # 1267650600228229401496703205376 (over 30 digits)
   print("Very large integer:", very_large)  # Very large integer: 1267650600228229401496703205376
   ```

2. **Floating-point (float)**:

   - Implemented using C's double precision floating-point format (IEEE 754)
   - Typically 64 bits with ~15-17 significant digits of precision
   - Floating-point math can have precision issues for certain calculations
   - Not suitable for exact decimal calculations (like money) due to binary representation

   ```python
   # Precision limitation example
   result = 0.1 + 0.2
   print("0.1 + 0.2 =", result)  # 0.1 + 0.2 = 0.30000000000000004, not exactly 0.3
   ```

3. **Strings (str)**:

   - Implemented as immutable sequences of Unicode code points
   - Each character is stored using 1, 2, or 4 bytes depending on the character range
   - String operations create new string objects (strings cannot be modified in-place)
   - String concatenation can be inefficient in loops (prefer join() for multiple concatenations)
   - Python optimizes memory by interning (reusing) commonly used strings

   ```python
   # String immutability example
   greeting = "Hello"
   # This doesn't modify the original string, it creates a new one
   new_greeting = greeting + " World"
   print("Original greeting:", greeting)  # Original greeting: Hello
   print("New greeting:", new_greeting)  # New greeting: Hello World
   ```

4. **Booleans (bool)**:

   - Implemented as a subclass of integers (True is 1, False is 0)
   - Only two possible values: True and False
   - Very memory efficient (typically just 24 bytes per boolean)
   - Can be used in arithmetic operations (True + True = 2)

   ```python
   # Booleans in arithmetic
   result = True + True + False
   print("True + True + False =", result)  # True + True + False = 2
   ```

5. **None (NoneType)**:

   - Represents the absence of a value or a null value
   - Singleton object - only one None object exists in memory
   - All variables assigned None point to the same object
   - Used as default return value for functions that don't explicitly return anything

   ```python
   # None is a singleton
   x = None
   y = None
   print("x is y:", x is y)  # x is y: True - they are the same object
   ```

### Basic Operators

Python supports various operators for computations and comparisons:

```python
# Arithmetic operators
a = 10
b = 3

addition = a + b
print("Addition:", addition)        # Addition: 13

subtraction = a - b
print("Subtraction:", subtraction)     # Subtraction: 7

multiplication = a * b
print("Multiplication:", multiplication)  # Multiplication: 30

division = a / b
print("Division:", division)        # Division: 3.3333... (returns a float)

floor_division = a // b
print("Floor division:", floor_division) # Floor division: 3 (integer division, rounds down)

remainder = a % b
print("Remainder:", remainder)       # Remainder: 1 (modulus - remainder after division)

exponent = a ** b
print("Exponent:", exponent)       # Exponent: 1000 (a raised to the power of b)

# Comparison operators - return boolean results
equals = a == b
print("a == b:", equals)         # a == b: False

not_equals = a != b
print("a != b:", not_equals)     # a != b: True

greater_than = a > b
print("a > b:", greater_than)    # a > b: True

less_than = a < b
print("a < b:", less_than)       # a < b: False

greater_or_equal = a >= b
print("a >= b:", greater_or_equal)  # a >= b: True

less_or_equal = a <= b
print("a <= b:", less_or_equal)     # a <= b: False

# Assignment operators
x = 5                   # Basic assignment
print("Initial x:", x)                 # Initial x: 5

x = x + 3               # Addition then assignment
print("After x = x + 3:", x)           # After x = x + 3: 8

x = x - 2               # Subtraction then assignment
print("After x = x - 2:", x)           # After x = x - 2: 6

x = x * 2               # Multiplication then assignment
print("After x = x * 2:", x)           # After x = x * 2: 12

x = x / 4               # Division then assignment
print("After x = x / 4:", x)           # After x = x / 4: 3.0

# Logical operators
is_valid = True
is_active = False

both_true = is_valid and is_active
print("is_valid and is_active:", both_true)  # is_valid and is_active: False (both must be True)

either_true = is_valid or is_active
print("is_valid or is_active:", either_true)  # is_valid or is_active: True (at least one must be True)

not_true = not is_valid
print("not is_valid:", not_true)  # not is_valid: False (inverts the boolean value)
```

## 2. Control Flow

Control flow allows you to make decisions and repeat actions in your code.

### Conditional Statements (if/elif/else)

```python
# Basic if statement
price = 45

if price > 50:
    print("This is an expensive item")
else:
    print("This is not an expensive item")  # This will print: This is not an expensive item

# if-else statement
inventory = 5

if inventory > 0:
    print("Item status:", "In stock")  # Item status: In stock
else:
    print("Item status:", "Out of stock")

# if-elif-else chain for multiple conditions
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} gets grade: {grade}")  # Score 85 gets grade: B

# Nested if statements
is_member = True
purchase_amount = 120

if is_member:
    if purchase_amount > 100:
        discount = 0.15
    else:
        discount = 0.10
else:
    if purchase_amount > 100:
        discount = 0.05
    else:
        discount = 0

final_price = purchase_amount * (1 - discount)
print(f"Member: {is_member}, Purchase: ${purchase_amount}, Discount: {discount*100}%, Final price: ${final_price}")
# Member: True, Purchase: $120, Discount: 15.0%, Final price: $102.0
```

### Loops

Loops allow you to repeat actions multiple times.

#### For Loops

```python
# Looping through a range of numbers (0 to 4)
print("Numbers from 0 to 4:")
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4 (one number per line)

# Looping with a start, stop, and step (1 to 9, counting by 2)
print("Odd numbers from 1 to 9:")
for i in range(1, 10, 2):
    print(i)  # Prints: 1, 3, 5, 7, 9 (one number per line)

# Looping through elements in a list
fruits = ["apple", "banana", "cherry"]
print("Fruits I like:")
for fruit in fruits:
    print(f"I like {fruit}s")  # Prints: I like apples, I like bananas, I like cherrys

# Looping through characters in a string
name = "Python"
print("Letters in Python:")
for character in name:
    print(character)  # Prints: P, y, t, h, o, n (one letter per line)

# Looping through key-value pairs in a dictionary
product = {"name": "Laptop", "price": 999, "brand": "TechCo"}
print("Product details:")
for key, value in product.items():
    print(f"{key}: {value}")  # Prints: name: Laptop, price: 999, brand: TechCo (one pair per line)
```

#### While Loops

```python
# Basic while loop
count = 0
print("Counting with while loop:")
while count < 5:
    print(count)  # Prints: 0, 1, 2, 3, 4 (one number per line)
    count = count + 1  # Increment count

# While loop with a break statement
number = 0
print("While loop with break:")
while True:
    print(number)  # Prints: 0, 1, 2, 3, 4 (then stops)
    number = number + 1
    if number >= 5:
        break  # Exits the loop when number reaches 5

# While loop with continue statement
count = 0
print("Only odd numbers:")
while count < 10:
    count = count + 1
    if count % 2 == 0:  # If count is even
        continue  # Skip the rest of the loop body
    print(count)  # Prints: 1, 3, 5, 7, 9 (one number per line)
```

## 3. Functions

Functions are reusable blocks of code that perform specific tasks. They help organize code and avoid repetition.

### Defining and Calling Functions

```python
# Basic function definition
def greet():
    print("Hello, Data Engineer!")

# Call the function
print("Calling greet() function:")
greet()  # Prints: Hello, Data Engineer!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

print("\nCalling greet_person() with different arguments:")
greet_person("Alice")  # Prints: Hello, Alice!
greet_person("Bob")    # Prints: Hello, Bob!

# Function with multiple parameters
def calculate_total(price, quantity, tax_rate=0.1):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

# Call with positional arguments
total1 = calculate_total(19.99, 5)
print(f"\nTotal with default tax: ${total1:.2f}")  # Total with default tax: $109.95

# Call with keyword arguments
total2 = calculate_total(price=24.99, quantity=3, tax_rate=0.05)
print(f"Total with 5% tax: ${total2:.2f}")  # Total with 5% tax: $78.72

# Call with mixed arguments (positional first, then keyword)
total3 = calculate_total(29.99, 2, tax_rate=0.08)
print(f"Total with 8% tax: ${total3:.2f}")  # Total with 8% tax: $64.78
```

### Function Return Values

```python
# Function that returns a value
def square(x):
    return x * x

result = square(5)
print(f"Square of 5: {result}")  # Square of 5: 25

# Function that returns multiple values
def get_dimensions():
    length = 10
    width = 5
    height = 2
    return length, width, height

# Unpack the returned values into separate variables
l, w, h = get_dimensions()
print(f"Dimensions - Length: {l}, Width: {w}, Height: {h}")
# Dimensions - Length: 10, Width: 5, Height: 2

# Or capture as a tuple
dimensions = get_dimensions()
print(f"Dimensions as tuple: {dimensions}")  # Dimensions as tuple: (10, 5, 2)
volume = dimensions[0] * dimensions[1] * dimensions[2]
print(f"The volume is {volume}")  # The volume is 100
```

### Function Scope

```python
# Variables defined inside functions are local to that function
def calculate_discount(price, rate):
    discount = price * rate  # Local variable
    return price - discount

discounted_price = calculate_discount(100, 0.2)
print(f"Discounted price: ${discounted_price}")  # Discounted price: $80.0

# This would raise an error because discount is not defined outside the function
# print(discount)  # NameError: name 'discount' is not defined

# Global variables can be accessed inside functions
total_sales = 0

def add_sale(amount):
    # To modify a global variable, you must declare it with 'global'
    global total_sales
    total_sales = total_sales + amount
    return total_sales

print("Adding sales:")
print("After adding $50:", add_sale(50))  # After adding $50: 50
print("After adding $25:", add_sale(25))  # After adding $25: 75
print("Final total_sales:", total_sales)   # Final total_sales: 75
```

## 4. Data Structures

Python has several built-in data structures to help organize data. Understanding their underlying implementation is crucial for using them effectively in data engineering.

### Lists

Lists are ordered, mutable collections that can hold items of different types.

**Implementation details:**

- Lists are implemented as dynamic arrays that resize automatically
- Elements are stored contiguously in memory
- Accessing elements by index is very fast (O(1) - constant time)
- Adding or removing elements from the end is usually fast (O(1))
- Adding or removing elements from the beginning or middle is slower (O(n) - linear time) as it requires shifting elements
- Memory overhead is relatively low but slightly higher than tuples

```python
# Creating a list
fruits = ["apple", "banana", "cherry", "date"]
print("Original fruits list:", fruits)  # Original fruits list: ['apple', 'banana', 'cherry', 'date']

# Accessing elements (indexing starts at 0)
first_fruit = fruits[0]  # "apple"
last_fruit = fruits[-1]  # "date" (negative indexing starts from the end)
print("First fruit:", first_fruit)  # First fruit: apple
print("Last fruit:", last_fruit)   # Last fruit: date

# Slicing a list [start:stop:step]
middle_fruits = fruits[1:3]  # ["banana", "cherry"] (stop index is exclusive)
every_other = fruits[::2]    # ["apple", "cherry"] (step of 2)
print("Middle fruits (index 1-2):", middle_fruits)  # Middle fruits (index 1-2): ['banana', 'cherry']
print("Every other fruit:", every_other)  # Every other fruit: ['apple', 'cherry']

# Modifying lists
fruits[1] = "blueberry"  # Replace an element
print("After replacing banana:", fruits)  # After replacing banana: ['apple', 'blueberry', 'cherry', 'date']

fruits.append("elderberry")  # Add to the end
print("After appending elderberry:", fruits)  # After appending elderberry: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

fruits.insert(1, "blackberry")  # Insert at index 1
print("After inserting blackberry at index 1:", fruits)  # After inserting blackberry at index 1: ['apple', 'blackberry', 'blueberry', 'cherry', 'date', 'elderberry']

removed_fruit = fruits.pop()  # Remove and return the last element
print("Removed fruit with pop():", removed_fruit)  # Removed fruit with pop(): elderberry
print("List after pop():", fruits)  # List after pop(): ['apple', 'blackberry', 'blueberry', 'cherry', 'date']

fruits.remove("cherry")  # Remove a specific element by value
print("After removing cherry:", fruits)  # After removing cherry: ['apple', 'blackberry', 'blueberry', 'date']

del fruits[0]  # Delete an element by index
print("After deleting index 0:", fruits)  # After deleting index 0: ['blackberry', 'blueberry', 'date']

# List length
num_fruits = len(fruits)
print("Number of fruits remaining:", num_fruits)  # Number of fruits remaining: 3

# Check if an item exists in the list
has_apple = "apple" in fruits
print("Is apple in the list?", has_apple)  # Is apple in the list? False

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2]
print("Original numbers:", numbers)  # Original numbers: [3, 1, 4, 1, 5, 9, 2]

numbers.sort()  # Sort in place
print("After sorting:", numbers)  # After sorting: [1, 1, 2, 3, 4, 5, 9]

numbers.reverse()  # Reverse in place
print("After reversing:", numbers)  # After reversing: [9, 5, 4, 3, 2, 1, 1]

count_of_1 = numbers.count(1)
print("Count of 1 in the list:", count_of_1)  # Count of 1 in the list: 2
```

### Dictionaries

Dictionaries are collections of key-value pairs, perfect for representing structured data.

**Implementation details:**

- Dictionaries are implemented as hash tables (hash maps)
- Keys must be hashable (immutable) types like strings, numbers, or tuples of immutable objects
- Looking up, adding, or removing items by key is very fast (O(1) - constant time)
- Dictionaries are unordered in Python before 3.6, and ordered by insertion from Python 3.7 onward
- Dictionary keys must be unique
- Memory overhead is higher than lists, as each entry requires storage for both key and value
- Dictionaries are optimized for fast key lookup when you don't know the position of an item

```python
# Creating a dictionary
product = {
    "name": "Laptop",
    "price": 999,
    "brand": "TechCo",
    "in_stock": True
}
print("Product dictionary:", product)
# Product dictionary: {'name': 'Laptop', 'price': 999, 'brand': 'TechCo', 'in_stock': True}

# Accessing values
product_name = product["name"]
print("Product name:", product_name)  # Product name: Laptop

# Alternative access with .get() (avoids KeyError if key doesn't exist)
category = product.get("category", "Electronics")  # Returns "Electronics" as default
print("Category (using get with default):", category)  # Category (using get with default): Electronics

# Modifying dictionaries
product["price"] = 899  # Change a value
print("After changing price:", product)
# After changing price: {'name': 'Laptop', 'price': 899, 'brand': 'TechCo', 'in_stock': True}

product["category"] = "Computers"  # Add a new key-value pair
print("After adding category:", product)
# After adding category: {'name': 'Laptop', 'price': 899, 'brand': 'TechCo', 'in_stock': True, 'category': 'Computers'}

product.update({"color": "Silver", "weight": "2.5 kg"})  # Add multiple key-value pairs
print("After update with multiple pairs:", product)
# After update with multiple pairs: {'name': 'Laptop', 'price': 899, 'brand': 'TechCo', 'in_stock': True, 'category': 'Computers', 'color': 'Silver', 'weight': '2.5 kg'}

# Removing items
removed_price = product.pop("price")  # Remove and return the value
print("Removed price:", removed_price)  # Removed price: 899
print("Dictionary after pop:", product)
# Dictionary after pop: {'name': 'Laptop', 'brand': 'TechCo', 'in_stock': True, 'category': 'Computers', 'color': 'Silver', 'weight': '2.5 kg'}

del product["in_stock"]  # Remove a key-value pair
print("Dictionary after del:", product)
# Dictionary after del: {'name': 'Laptop', 'brand': 'TechCo', 'category': 'Computers', 'color': 'Silver', 'weight': '2.5 kg'}

# Dictionary methods
keys = product.keys()  # Get all keys
print("Dictionary keys:", list(keys))  # Dictionary keys: ['name', 'brand', 'category', 'color', 'weight']

values = product.values()  # Get all values
print("Dictionary values:", list(values))  # Dictionary values: ['Laptop', 'TechCo', 'Computers', 'Silver', '2.5 kg']

items = product.items()  # Get all key-value pairs as tuples
print("Dictionary items:", list(items))
# Dictionary items: [('name', 'Laptop'), ('brand', 'TechCo'), ('category', 'Computers'), ('color', 'Silver'), ('weight', '2.5 kg')]

# Check if a key exists
has_brand = "brand" in product
print("Does dictionary have 'brand' key?", has_brand)  # Does dictionary have 'brand' key? True
```

### Tuples

Tuples are ordered, immutable collections, useful for fixed data.

**Implementation details:**

- Tuples are implemented as fixed-size arrays
- Being immutable (unchangeable after creation), they're more memory-efficient than lists
- Accessing elements by index is very fast (O(1) - constant time)
- Since tuples can't be modified after creation, they're hashable and can be used as dictionary keys
- Tuples are typically used for heterogeneous data (different types), while lists are often used for homogeneous data
- Tuple operations are generally faster than equivalent list operations

```python
# Creating a tuple
dimensions = (10, 20, 30)  # Width, height, depth
print("Dimensions tuple:", dimensions)  # Dimensions tuple: (10, 20, 30)

# Creating a single-element tuple (note the comma)
single_item = (42,)  # Without the comma, it would be a number in parentheses
print("Single-element tuple:", single_item)  # Single-element tuple: (42,)
print("Type of single_item:", type(single_item))  # Type of single_item: <class 'tuple'>

# Accessing elements
width = dimensions[0]  # 10
print("Width from tuple:", width)  # Width from tuple: 10

# Tuple unpacking
width, height, depth = dimensions
print(f"Unpacked dimensions - Width: {width}, Height: {height}, Depth: {depth}")
# Unpacked dimensions - Width: 10, Height: 20, Depth: 30

# Tuples are immutable - this would raise an error
# dimensions[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Tuple methods
coordinates = (4, 5, 4, 1, 4)
count_of_4 = coordinates.count(4)
print("Count of 4 in coordinates:", count_of_4)  # Count of 4 in coordinates: 3

index_of_5 = coordinates.index(5)
print("Index of 5 in coordinates:", index_of_5)  # Index of 5 in coordinates: 1
```

### Sets

Sets are unordered collections of unique elements, useful for removing duplicates and membership testing.

**Implementation details:**

- Sets are implemented using hash tables, similar to dictionaries but without values
- Elements must be hashable (immutable) types
- Looking up, adding, or removing items is very fast (O(1) - constant time)
- Sets automatically eliminate duplicates (each element can appear only once)
- Sets are unordered (elements don't have a defined position)
- Sets support efficient mathematical operations like union, intersection, and difference
- Sets are optimized for testing membership ("does this element exist?") and eliminating duplicates

```python
# Creating a set
unique_visitors = {"user1", "user2", "user3", "user1"}  # Note: duplicates are automatically removed
print("Unique visitors set:", unique_visitors)  # Unique visitors set: {'user1', 'user2', 'user3'}
# Note: The order may be different when you run the code

# Creating an empty set (can't use {} as that creates an empty dictionary)
empty_set = set()
print("Empty set:", empty_set)  # Empty set: set()
print("Type of empty_set:", type(empty_set))  # Type of empty_set: <class 'set'>

# Set operations
unique_visitors.add("user4")  # Add an element
print("After adding user4:", unique_visitors)  # After adding user4: {'user1', 'user2', 'user3', 'user4'}

unique_visitors.remove("user2")  # Remove an element (raises KeyError if not found)
print("After removing user2:", unique_visitors)  # After removing user2: {'user1', 'user3', 'user4'}

unique_visitors.discard("user5")  # Remove if present (no error if not found)
print("After discarding user5 (which wasn't in the set):", unique_visitors)
# After discarding user5 (which wasn't in the set): {'user1', 'user3', 'user4'}

# Set methods
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("set1:", set1)  # set1: {1, 2, 3, 4, 5}
print("set2:", set2)  # set2: {4, 5, 6, 7, 8}

union = set1 | set2  # set1.union(set2) - All elements from both sets
print("Union of set1 and set2:", union)  # Union of set1 and set2: {1, 2, 3, 4, 5, 6, 7, 8}

intersection = set1 & set2  # set1.intersection(set2) - Elements common to both sets
print("Intersection of set1 and set2:", intersection)  # Intersection of set1 and set2: {4, 5}

difference = set1 - set2  # set1.difference(set2) - Elements in set1 but not in set2
print("Difference (set1 - set2):", difference)  # Difference (set1 - set2): {1, 2, 3}

symmetric_difference = set1 ^ set2  # set1.symmetric_difference(set2) - Elements in either set but not both
print("Symmetric difference of set1 and set2:", symmetric_difference)
# Symmetric difference of set1 and set2: {1, 2, 3, 6, 7, 8}

# Membership testing (very efficient)
is_present = 3 in set1
print("Is 3 in set1?", is_present)  # Is 3 in set1? True
```

## 5. String Manipulation

Strings are sequences of characters, and Python provides many ways to work with them.

### String Basics

```python
# String creation
single_quotes = 'Data Engineering'
double_quotes = "Python for Data"
triple_quotes = """This is a multi-line
string that spans multiple lines"""

print("String with single quotes:", single_quotes)  # String with single quotes: Data Engineering
print("String with double quotes:", double_quotes)  # String with double quotes: Python for Data
print("Multi-line string:", triple_quotes)
# Multi-line string: This is a multi-line
# string that spans multiple lines

# String concatenation
full_title = single_quotes + ": " + double_quotes
print("Concatenated string:", full_title)  # Concatenated string: Data Engineering: Python for Data

# String repetition
separator = "-" * 20  # Creates a string of 20 hyphens
print("Separator:", separator)  # Separator: --------------------

# String indexing and slicing
text = "Python"
first_char = text[0]  # "P"
last_char = text[-1]  # "n"
substring = text[1:4]  # "yth" (characters at positions 1, 2, and 3)

print("Original string:", text)  # Original string: Python
print("First character:", first_char)  # First character: P
print("Last character:", last_char)  # Last character: n
print("Substring [1:4]:", substring)  # Substring [1:4]: yth
```

### String Methods

```python
# Common string methods
text = "  Data Engineering with Python  "
print("Original text:", repr(text))  # Original text: '  Data Engineering with Python  '

# Removing whitespace
trimmed = text.strip()
print("After strip():", repr(trimmed))  # After strip(): 'Data Engineering with Python'

left_trimmed = text.lstrip()
print("After lstrip():", repr(left_trimmed))  # After lstrip(): 'Data Engineering with Python  '

right_trimmed = text.rstrip()
print("After rstrip():", repr(right_trimmed))  # After rstrip(): '  Data Engineering with Python'

# Case conversion
upper_case = text.upper()
print("After upper():", upper_case)  # After upper():   DATA ENGINEERING WITH PYTHON

lower_case = text.lower()
print("After lower():", lower_case)  # After lower():   data engineering with python

title_case = text.title()
print("After title():", title_case)  # After title():   Data Engineering With Python

# Finding and replacing
position = text.find("Python")
print("Position of 'Python':", position)  # Position of 'Python': 23

replaced = text.replace("Python", "SQL")
print("After replacing 'Python' with 'SQL':", replaced)  # After replacing 'Python' with 'SQL':   Data Engineering with SQL

# Splitting and joining
words = trimmed.split()
print("After splitting trimmed text:", words)  # After splitting trimmed text: ['Data', 'Engineering', 'with', 'Python']

csv = "apple,banana,cherry"
fruits = csv.split(",")
print("After splitting CSV:", fruits)  # After splitting CSV: ['apple', 'banana', 'cherry']

joined = ", ".join(fruits)
print("After joining with comma+space:", joined)  # After joining with comma+space: apple, banana, cherry
```

### f-strings (formatted string literals)

f-strings provide an easy way to embed expressions inside string literals.

```python
# Basic f-string usage
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Hello, Alice! You are 30 years old.

# F-strings with expressions
price = 49.95
quantity = 3
total = price * quantity
invoice = f"""
INVOICE
========
Item price:    ${price:.2f}
Quantity:      {quantity}
-----------------------
Total:         ${total:.2f}
"""
print(invoice)
# INVOICE
# ========
# Item price:    $49.95
# Quantity:      3
# -----------------------
# Total:         $149.85

# F-strings with dictionaries
product = {"name": "Laptop", "price": 999.99}
product_info = f"Product: {product['name']}, Price: ${product['price']:.2f}"
print(product_info)  # Product: Laptop, Price: $999.99
```

## Micro-Project: Sales Data Analyzer

Now let's apply what we've learned to create a sales data analyzer. This micro-project will help reinforce Python fundamentals while solving a practical data problem.

### Project Objectives

Create a Python script that:

1. Works with a sample sales dataset
2. Calculates key metrics (total sales, average order value, top selling product)
3. Handles basic data cleaning (removing invalid entries, standardizing formats)
4. Generates formatted output showing the results

### Sample Dataset

Since we don't cover file handling until Chapter 2, we'll create a simple in-memory dataset:

```python
# Sample sales data (normally this would come from a CSV file)
# Format: [order_id, product_name, quantity, price_per_unit, date]
sales_data = [
    ["1001", "Laptop", "2", "999.99", "2023-01-15"],
    ["1002", "Mouse", "10", "24.99", "2023-01-16"],
    ["1003", "Keyboard", "5", "49.99", "2023-01-16"],
    ["1004", "Monitor", "3", "149.99", "2023-01-17"],
    ["1005", "Laptop", "1", "999.99", "2023-01-18"],
    ["1006", "Headphones", "4", "59.99", "2023-01-18"],
    ["1007", "Mouse", "5", "24.99", "2023-01-19"],
    ["1008", "", "2", "29.99", "2023-01-19"],  # Missing product name
    ["1009", "Keyboard", "0", "49.99", "2023-01-20"],  # Zero quantity
    ["1010", "Monitor", "2", "invalid_price", "2023-01-20"],  # Invalid price
    ["1011", "Laptop", "1", "899.99", "2023-01-21"]
]
```

### Acceptance Criteria

- Script runs without errors when provided the data
- Correctly calculates all required statistics (total sales, average order value, top product)
- Properly handles invalid entries (missing product names, zero quantities, invalid prices)
- Uses appropriate Python data structures (lists, dictionaries)
- Includes comments explaining the code's functionality
- Produces readable, formatted output

### Common Pitfalls

1. **String vs. numeric data confusion**:

   - Remember that all data in our sample is stored as strings
   - Convert strings to numeric types before performing calculations

2. **Not checking for invalid data**:

   - Always verify data is valid before using it in calculations
   - Check for empty strings, zero quantities, or values that can't be converted to numbers

3. **Using incorrect aggregation logic**:
   - Pay attention to how totals and averages should be calculated
   - For average order value, divide total revenue by number of valid orders

### Project Solution

```python
# Sales Data Analyzer
# A program to analyze sales data and calculate key metrics

def analyze_sales_data(sales_data):
    """
    Analyze the provided sales data and return key metrics.

    Args:
        sales_data: A list of sales records

    Returns:
        A dictionary containing calculated metrics
    """
    # Initialize variables to track metrics
    total_sales = 0
    valid_orders = 0
    product_sales = {}  # Dictionary to track sales by product

    # Process each sales record
    for record in sales_data:
        order_id, product_name, quantity_str, price_str, date = record

        # Basic data validation
        if not product_name:  # Check for missing product name
            print(f"Warning: Missing product name in order {order_id}. Skipping.")
            continue

        # Check if quantity is a valid number
        is_valid_quantity = True
        for char in quantity_str:
            if char not in "0123456789":
                is_valid_quantity = False
                break

        if not is_valid_quantity:
            print(f"Warning: Invalid quantity in order {order_id}. Skipping.")
            continue

        # Convert quantity to integer (safe now that we've checked it's valid)
        quantity = int(quantity_str)

        # Skip records with zero or negative quantity
        if quantity <= 0:
            print(f"Warning: Zero or negative quantity in order {order_id}. Skipping.")
            continue

        # Checking if price is a valid number (only digits and one decimal point)
        is_valid_price = True
        decimal_count = 0

        for char in price_str:
            if char == '.':
                decimal_count = decimal_count + 1
            elif char not in "0123456789":
                is_valid_price = False
                break

        if not is_valid_price or decimal_count > 1:
            print(f"Warning: Invalid price format in order {order_id}. Skipping.")
            continue

        # Convert price to float (safe now that we've checked it's in a valid format)
        price = float(price_str)

        # Calculate the order value
        order_value = quantity * price

        # Update total sales
        total_sales += order_value
        valid_orders += 1

        # Update product sales dictionary - initialize to 0 if product not seen before
        if product_name in product_sales:
            product_sales[product_name] = product_sales[product_name] + order_value
        else:
            product_sales[product_name] = order_value

    # Calculate the average order value
    if valid_orders > 0:
        average_order_value = total_sales / valid_orders
    else:
        average_order_value = 0

    # Find the top selling product
    top_product = ""
    top_product_sales = 0

    for product, sales in product_sales.items():
        if sales > top_product_sales:
            top_product = product
            top_product_sales = sales

    # Return the calculated metrics
    return {
        "total_sales": total_sales,
        "average_order_value": average_order_value,
        "valid_orders": valid_orders,
        "top_product": top_product,
        "top_product_sales": top_product_sales,
        "product_sales": product_sales
    }

def format_as_currency(amount):
    """Format a number as currency with $ symbol and 2 decimal places"""
    return f"${amount:.2f}"

# Formatting a number as currency
print("Formatted as currency:", format_as_currency(123.456))  # Formatted as currency: $123.46

# Sample sales data (normally this would come from a CSV file)
# Format: [order_id, product_name, quantity, price_per_unit, date]
sales_data = [
    ["1001", "Laptop", "2", "999.99", "2023-01-15"],
    ["1002", "Mouse", "10", "24.99", "2023-01-16"],
    ["1003", "Keyboard", "5", "49.99", "2023-01-16"],
    ["1004", "Monitor", "3", "149.99", "2023-01-17"],
    ["1005", "Laptop", "1", "999.99", "2023-01-18"],
    ["1006", "Headphones", "4", "59.99", "2023-01-18"],
    ["1007", "Mouse", "5", "24.99", "2023-01-19"],
    ["1008", "", "2", "29.99", "2023-01-19"],  # Missing product name
    ["1009", "Keyboard", "0", "49.99", "2023-01-20"],  # Zero quantity
    ["1010", "Monitor", "2", "invalid_price", "2023-01-20"],  # Invalid price
    ["1011", "Laptop", "1", "899.99", "2023-01-21"]
]

print("Sample of sales data (first 3 records):")
for i in range(3):
    print(f"  Record {i+1}: {sales_data[i]}")
# Sample of sales data (first 3 records):
#   Record 1: ['1001', 'Laptop', '2', '999.99', '2023-01-15']
#   Record 2: ['1002', 'Mouse', '10', '24.99', '2023-01-16']
#   Record 3: ['1003', 'Keyboard', '5', '49.99', '2023-01-16']

# Analyze the sales data
print("\nAnalyzing sales data...")
results = analyze_sales_data(sales_data)

# Display the results
print("\nAnalysis Results:")
print(f"Total Sales: {format_as_currency(results['total_sales'])}")  # e.g., Total Sales: $4,419.70
print(f"Number of Valid Orders: {results['valid_orders']}")          # e.g., Number of Valid Orders: 8
print(f"Average Order Value: {format_as_currency(results['average_order_value'])}")  # e.g., Average Order Value: $552.46

print(f"\nTop Selling Product: {results['top_product']}")  # e.g., Top Selling Product: Laptop
print(f"Top Product Sales: {format_as_currency(results['top_product_sales'])}")  # e.g., Top Product Sales: $2,899.97

print("\nSales by Product:")
for product, sales in sorted(results["product_sales"].items()):
    print(f"  - {product}: {format_as_currency(sales)}")
# Sales by Product:
#   - Headphones: $239.96
#   - Keyboard: $249.95
#   - Laptop: $2,899.97
#   - Monitor: $449.97
#   - Mouse: $374.85

# Generate a formatted report
report = f"""
SALES DATA ANALYSIS REPORT
===========================

Total Sales: {format_as_currency(results["total_sales"])}
Number of Valid Orders: {results["valid_orders"]}
Average Order Value: {format_as_currency(results["average_order_value"])}

Top Selling Product: {results["top_product"]}
Top Product Sales: {format_as_currency(results["top_product_sales"])}

Sales by Product:
"""

# Add each product's sales to the report
for product, sales in sorted(results["product_sales"].items()):
    report += f"  - {product}: {format_as_currency(sales)}\n"

# Print the report
print("\nFinal formatted report:")
print(report)
"""
Final formatted report:

SALES DATA ANALYSIS REPORT
===========================

Total Sales: $4,214.70
Number of Valid Orders: 8
Average Order Value: $526.84

Top Selling Product: Laptop
Top Product Sales: $2,899.97

Sales by Product:
  - Headphones: $239.96
  - Keyboard: $249.95
  - Laptop: $2,899.97
  - Monitor: $449.97
  - Mouse: $374.85
"""
```

### How to Run and Test the Solution

1. Copy the entire code to a Python file (e.g., `sales_analyzer.py`)
2. Run the file using Python: `python sales_analyzer.py`
3. The script will process the sample data, display warnings for invalid entries, and generate a formatted report of the sales metrics

### Real-World vs. Micro-Project Differences

In a real-world/production scenario, this solution would differ in several ways:

1. **Data source**:

   - Real-world: Read data from files, databases, or APIs
   - Micro-project: Using in-memory data

2. **Error handling**:

   - Real-world: More robust error handling with logging, retry mechanisms
   - Micro-project: Basic error checking and console warnings

3. **Performance optimization**:

   - Real-world: Optimized for large datasets (streaming, batch processing)
   - Micro-project: Simple loops and data structures sufficient for small samples

4. **Output formats**:

   - Real-world: Various output formats (CSV, database, API, dashboards)
   - Micro-project: Simple console output

5. **Testing**:
   - Real-world: Comprehensive unit tests, integration tests
   - Micro-project: Manual testing

## 6. List Comprehensions

List comprehensions provide a concise way to create and transform lists, making data transformation code more readable and efficient.

```python
# Basic list comprehension syntax: [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension with filtering: [expression for item in iterable if condition]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16]

# Equivalent to:
even_squares_traditional = []
for x in numbers:
    if x % 2 == 0:
        even_squares_traditional.append(x**2)

# List comprehension with string operations
names = ["Alice", "Bob", "Charlie", "David"]
# Using a loop instead of list comprehension (covered later in the chapter)
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE', 'DAVID']

# List comprehension with conditional expression
status = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(status)  # ['odd', 'even', 'odd', 'even', 'odd']

# Creating a list of dictionaries (common in data engineering)
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 24.99, 49.99]
inventory = [{"product": p, "price": pr} for p, pr in zip(products, prices)]
print(inventory)  # [{'product': 'Laptop', 'price': 999.99}, {'product': 'Mouse', 'price': 24.99}, {'product': 'Keyboard', 'price': 49.99}]
```

List comprehensions are especially useful in data engineering when transforming data structures or extracting specific information from complex datasets.

## 7. Standard Library Modules

Python's standard library provides many useful modules for common tasks. Here are some essential ones for data engineering:

```python
# Math module for mathematical operations
import math

radius = 5
circle_area = math.pi * radius**2
print(f"Circle area with radius {radius}:", circle_area)  # Circle area with radius 5: 78.53981633974483
print(f"Circle area (formatted):", f"{circle_area:.2f}")  # Circle area (formatted): 78.54

sqrt_value = math.sqrt(16)  # Square root
print(f"Square root of 16:", sqrt_value)  # Square root of 16: 4.0

# Datetime module for working with dates and times
import datetime

# Current date and time
now = datetime.datetime.now()
print(f"Current date and time:", now)  # Current date and time: 2023-04-17 15:30:45.123456 (your output will vary)

# Creating specific dates
event_date = datetime.datetime(2023, 12, 31, 23, 59, 59)
print(f"Event date:", event_date)  # Event date: 2023-12-31 23:59:59

# Date arithmetic
time_difference = event_date - now
print(f"Days until event:", time_difference.days)  # Days until event: 258 (your output will vary)

# OS module for operating system interactions
import os

# Current working directory
current_dir = os.getcwd()
print(f"Current directory:", current_dir)  # Current directory: /your/current/directory

# List files in a directory (we'll use the current directory)
files = os.listdir('.')  # '.' refers to the current directory
print(f"Files in current directory (first 5 if available):")
for i, file in enumerate(files[:5]):  # Only show up to 5 files for brevity
    print(f"  {i+1}. {file}")
# Files in current directory (first 5 if available):
#   1. example.py
#   2. data.txt
#   3. ...

# JSON module for working with JSON data
import json

# Converting Python objects to JSON strings
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "SQL", "Data Engineering"]
}

json_string = json.dumps(person, indent=2)
print(f"JSON representation of person object:")
print(json_string)
# JSON representation of person object:
# {
#   "name": "Alice",
#   "age": 30,
#   "city": "New York",
#   "skills": [
#     "Python",
#     "SQL",
#     "Data Engineering"
#   ]
# }

# Converting JSON string back to Python object
parsed_json = json.loads(json_string)
print(f"Name from parsed JSON:", parsed_json['name'])  # Name from parsed JSON: Alice
print(f"First skill from parsed JSON:", parsed_json['skills'][0])  # First skill from parsed JSON: Python

# Note: The csv and sqlite3 modules will be covered in later chapters
# when we discuss file handling and databases
```

These standard library modules provide essential functionality for working with mathematical computations, dates, file systems, and data formats - all common tasks in data engineering.

## Practice Exercises

Reinforce your Python fundamentals with these exercises:

### Exercise 1: Basic Data Types and Functions

Create a function to calculate the total price of items in a shopping cart:

- Takes parameters for a list of prices and a tax rate
- Returns the total including tax
- Test it with different inputs

### Exercise 2: List Comprehensions

Write a function that:

- Takes a list of product dictionaries (each with 'name' and 'price' keys)
- Returns a list of only the products with prices greater than $50
- Try implementing it both with a traditional for loop and with a list comprehension

### Exercise 3: Data Structures

Create a program that tracks daily sales using:

- A dictionary with dates as keys
- Lists of products sold as values
- Functions to add sales and calculate daily totals

### Exercise 4: Standard Library Challenge

Write a program using the datetime module that:

- Calculates and prints the current day of the week
- Determines the number of days until the end of the current month
- Formats the current date in "Month Day, Year" format

### Challenge Exercise: Enhanced Sales Analyzer

Extend the Sales Data Analyzer micro-project using list comprehensions to:

- Create a filtered list of valid sales records
- Group sales by product using a dictionary comprehension
- Format the output using string formatting

## Exercise Solutions

Here are solutions to the practice exercises. Try solving them yourself before looking at these solutions!

### Solution to Exercise 1: Basic Data Types and Functions

```python
def calculate_cart_total(prices, tax_rate):
    """
    Calculate the total price of items including tax.

    Args:
        prices: A list of prices
        tax_rate: The tax rate as a decimal (e.g., 0.08 for 8%)

    Returns:
        The total price including tax
    """
    # Calculate subtotal by adding all prices
    subtotal = 0
    for price in prices:
        subtotal = subtotal + price

    # Calculate tax amount
    tax_amount = subtotal * tax_rate

    # Calculate total
    total = subtotal + tax_amount

    return total

# Test with different inputs
cart1 = [10.99, 24.50, 5.95]
tax_rate1 = 0.08  # 8% tax

cart2 = [199.99, 99.50, 50.00, 17.85]
tax_rate2 = 0.06  # 6% tax

# Calculate and display results
total1 = calculate_cart_total(cart1, tax_rate1)
print(f"Cart 1 Items: {cart1}")  # Cart 1 Items: [10.99, 24.5, 5.95]
print(f"Tax Rate: {tax_rate1 * 100}%")  # Tax Rate: 8.0%
print(f"Total with tax: ${total1:.2f}")  # Total with tax: $44.80

total2 = calculate_cart_total(cart2, tax_rate2)
print(f"\nCart 2 Items: {cart2}")  # Cart 2 Items: [199.99, 99.5, 50.0, 17.85]
print(f"Tax Rate: {tax_rate2 * 100}%")  # Tax Rate: 6.0%
print(f"Total with tax: ${total2:.2f}")  # Total with tax: $389.58
```

### Solution to Exercise 2: List Comprehensions

```python
def find_expensive_products_loop(products, min_price):
    """
    Find products with prices greater than the minimum price using a traditional loop.

    Args:
        products: A list of product dictionaries with 'name' and 'price' keys
        min_price: The minimum price threshold

    Returns:
        A list of products with prices greater than min_price
    """
    expensive_products = []

    for product in products:
        if product["price"] > min_price:
            expensive_products.append(product)

    return expensive_products

def find_expensive_products_comprehension(products, min_price):
    """
    Find products with prices greater than the minimum price using a list comprehension.

    Args:
        products: A list of product dictionaries with 'name' and 'price' keys
        min_price: The minimum price threshold

    Returns:
        A list of products with prices greater than min_price
    """
    return [product for product in products if product["price"] > min_price]

# Test data
product_list = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 24.99},
    {"name": "Keyboard", "price": 49.99},
    {"name": "Monitor", "price": 149.99},
    {"name": "Headphones", "price": 79.99}
]

# Find products over $50
min_price = 50.0

# Using traditional loop
expensive_loop = find_expensive_products_loop(product_list, min_price)
print(f"Products over ${min_price} (using loop):")
for product in expensive_loop:
    print(f"  - {product['name']}: ${product['price']}")
# Products over $50.0 (using loop):
#   - Laptop: $999.99
#   - Monitor: $149.99
#   - Headphones: $79.99

# Using list comprehension
expensive_comprehension = find_expensive_products_comprehension(product_list, min_price)
print(f"\nProducts over ${min_price} (using list comprehension):")
for product in expensive_comprehension:
    print(f"  - {product['name']}: ${product['price']}")
# Products over $50.0 (using list comprehension):
#   - Laptop: $999.99
#   - Monitor: $149.99
#   - Headphones: $79.99

# Verifying both approaches give the same result
print(f"\nBoth approaches give the same result: {expensive_loop == expensive_comprehension}")
# Both approaches give the same result: True
```

### Solution to Exercise 3: Data Structures

```python
def create_sales_tracker():
    """Create and return an empty sales tracking dictionary."""
    return {}

def add_sale(sales_tracker, date, product):
    """
    Add a product sale to the given date.

    Args:
        sales_tracker: The sales tracking dictionary
        date: The date of the sale (string)
        product: The product that was sold
    """
    # If the date already exists in the tracker, append to its list
    if date in sales_tracker:
        sales_tracker[date].append(product)
    # Otherwise, create a new list with this product
    else:
        sales_tracker[date] = [product]

    return sales_tracker

def calculate_daily_totals(sales_tracker):
    """
    Calculate the number of sales for each day.

    Args:
        sales_tracker: The sales tracking dictionary

    Returns:
        A dictionary with dates as keys and total sales as values
    """
    daily_totals = {}

    for date, products in sales_tracker.items():
        daily_totals[date] = len(products)

    return daily_totals

# Test the sales tracker
tracker = create_sales_tracker()
print("Initial sales tracker:", tracker)  # Initial sales tracker: {}

# Add some sales
tracker = add_sale(tracker, "2023-01-15", "Laptop")
tracker = add_sale(tracker, "2023-01-15", "Mouse")
tracker = add_sale(tracker, "2023-01-16", "Keyboard")
tracker = add_sale(tracker, "2023-01-17", "Monitor")
tracker = add_sale(tracker, "2023-01-17", "Headphones")
tracker = add_sale(tracker, "2023-01-17", "Mouse")

print("\nSales tracker after adding sales:")
for date, products in tracker.items():
    print(f"  {date}: {products}")
# Sales tracker after adding sales:
#   2023-01-15: ['Laptop', 'Mouse']
#   2023-01-16: ['Keyboard']
#   2023-01-17: ['Monitor', 'Headphones', 'Mouse']

# Calculate daily totals
totals = calculate_daily_totals(tracker)
print("\nDaily sales totals:")
for date, total in totals.items():
    print(f"  {date}: {total} items")
# Daily sales totals:
#   2023-01-15: 2 items
#   2023-01-16: 1 items
#   2023-01-17: 3 items
```

### Solution to Exercise 4: Standard Library Challenge

```python
import datetime

# Get current date
current_date = datetime.datetime.now()
print(f"Current date and time: {current_date}")  # Current date and time: 2023-04-17 15:45:30.123456 (will vary)

# 1. Calculate and print the current day of the week
day_of_week = current_date.strftime("%A")  # %A gives full weekday name
print(f"1. Current day of the week: {day_of_week}")  # 1. Current day of the week: Monday (will vary)

# 2. Determine number of days until the end of the current month
# First, get the last day of the current month
year = current_date.year
month = current_date.month

# To get the last day of the month, we'll use the first day of next month and subtract one day
if month == 12:  # December
    next_month = datetime.datetime(year + 1, 1, 1)  # January 1 of next year
else:
    next_month = datetime.datetime(year, month + 1, 1)  # First day of next month

last_day_of_month = next_month - datetime.timedelta(days=1)
days_remaining = last_day_of_month.day - current_date.day

print(f"2. Days until the end of {current_date.strftime('%B')}: {days_remaining}")
# 2. Days until the end of April: 13 (will vary)

# 3. Format the current date as "Month Day, Year"
formatted_date = current_date.strftime("%B %d, %Y")
print(f"3. Formatted date: {formatted_date}")  # 3. Formatted date: April 17, 2023 (will vary)
```

### Solution to Challenge Exercise: Enhanced Sales Analyzer

```python
def is_valid_record(record):
    """Check if a sales record is valid."""
    order_id, product_name, quantity_str, price_str, date = record

    # Check for missing product name
    if not product_name:
        return False

    # Check if quantity is a valid number
    is_valid_quantity = True
    for char in quantity_str:
        if char not in "0123456789":
            is_valid_quantity = False
            break

    if not is_valid_quantity:
        return False

    # Convert quantity to integer
    quantity = int(quantity_str)

    # Check for zero or negative quantity
    if quantity <= 0:
        return False

    # Check if price is a valid number
    is_valid_price = True
    decimal_count = 0

    for char in price_str:
        if char == '.':
            decimal_count = decimal_count + 1
        elif char not in "0123456789":
            is_valid_price = False
            break

    if not is_valid_price or decimal_count > 1:
        return False

    return True

def analyze_sales_with_comprehensions(sales_data):
    """Analyze sales data using list comprehensions where appropriate."""
    # Filter valid records using list comprehension
    valid_records = [record for record in sales_data if is_valid_record(record)]

    print(f"Total records: {len(sales_data)}")  # Total records: 11
    print(f"Valid records: {len(valid_records)}")  # Valid records: 8

    # Calculate totals and group by product
    product_sales = {}

    for record in valid_records:
        _, product_name, quantity_str, price_str, _ = record
        quantity = int(quantity_str)
        price = float(price_str)

        # Calculate order value
        order_value = quantity * price

        # Group by product (using dictionary)
        if product_name in product_sales:
            product_sales[product_name] = product_sales[product_name] + order_value
        else:
            product_sales[product_name] = order_value

    # Calculate total sales and average order value
    total_sales = sum(quantity * float(price) for _, _, quantity, price, _ in
                      ([record[0], record[1], int(record[2]), record[3], record[4]]
                       for record in valid_records))

    average_order = total_sales / len(valid_records)

    # Find top product
    top_product = ""
    top_sales = 0

    for product, sales in product_sales.items():
        if sales > top_sales:
            top_product = product
            top_sales = sales

    # Generate a formatted report
    report = f"""
ENHANCED SALES ANALYSIS REPORT
=============================

Summary:
--------
Total Records: {len(sales_data)}
Valid Records: {len(valid_records)}
Total Sales: ${total_sales:.2f}
Average Order: ${average_order:.2f}

Top Product:
-----------
{top_product}: ${top_sales:.2f}

Sales by Product:
---------------
"""

    # Add product sales in descending order
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    for product, sales in sorted_products:
        report += f"{product}: ${sales:.2f}\n"

    return report

# Sample sales data (same as before)
sales_data = [
    ["1001", "Laptop", "2", "999.99", "2023-01-15"],
    ["1002", "Mouse", "10", "24.99", "2023-01-16"],
    ["1003", "Keyboard", "5", "49.99", "2023-01-16"],
    ["1004", "Monitor", "3", "149.99", "2023-01-17"],
    ["1005", "Laptop", "1", "999.99", "2023-01-18"],
    ["1006", "Headphones", "4", "59.99", "2023-01-18"],
    ["1007", "Mouse", "5", "24.99", "2023-01-19"],
    ["1008", "", "2", "29.99", "2023-01-19"],  # Missing product name
    ["1009", "Keyboard", "0", "49.99", "2023-01-20"],  # Zero quantity
    ["1010", "Monitor", "2", "invalid_price", "2023-01-20"],  # Invalid price
    ["1011", "Laptop", "1", "899.99", "2023-01-21"]
]

# Run the enhanced analyzer
enhanced_report = analyze_sales_with_comprehensions(sales_data)
print(enhanced_report)
"""
ENHANCED SALES ANALYSIS REPORT
=============================

Summary:
--------
Total Records: 11
Valid Records: 8
Total Sales: $4214.70
Average Order: $526.84

Top Product:
-----------
Laptop: $2899.97

Sales by Product:
---------------
Laptop: $2899.97
Monitor: $449.97
Mouse: $374.85
Keyboard: $249.95
Headphones: $239.96
"""
```

## Summary

In this chapter, we covered the fundamental building blocks of Python:

- Variables and basic data types (int, float, str, bool)
- Control flow statements (if/elif/else, for loops, while loops)
- Functions for code organization and reuse
- Data structures (lists, dictionaries, tuples, sets)
- String manipulation and formatting with f-strings
- List comprehensions for concise data transformations
- Standard library modules for common tasks (math, datetime, os, json)

These core concepts serve as the foundation for all data engineering work in Python. In the next chapter, we'll build on these basics to learn about file handling, error management, and more advanced data handling techniques.
