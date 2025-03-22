---
title: 'Python'
date: 2025-03-19T07:16:00+07:00
draft: false
weight: 1
---

This comprehensive guide covers Python's core concepts, standard library features, and concurrency models (threading, multiprocessing, and asynchronous programming).

## Python Fundamentals

### Installation and Setup

- **Download Python**: Visit [python.org](https://python.org) to download the latest version
- **Check Installation**:
  ```bash
  python --version  # or python3 --version
  ```
- **Python Interactive Shell**:
  ```bash
  python  # or python3
  ```
- **Run Python Script**:
  ```bash
  python script.py  # or python3 script.py
  ```

### Python Syntax

- **Indentation**: Python uses indentation (typically 4 spaces) for code blocks

  ```python
  # Correct indentation
  if True:
      print("Indented correctly")

  # Incorrect indentation will cause an error
  if True:
  print("This will raise an IndentationError")
  ```

- **Comments**:

  ```python
  # Single line comment

  """
  Multi-line comment
  or docstring
  """
  ```

- **Line Continuation**:

  ```python
  # Using backslash
  total = 1 + 2 + 3 + \
          4 + 5

  # Using parentheses, brackets, or braces
  total = (1 + 2 + 3 +
          4 + 5)
  ```

## Data Types and Variables

### Variable Assignment

- **Basic Assignment**:

  ```python
  x = 10  # Integer
  name = "Python"  # String
  is_valid = True  # Boolean
  ```

- **Multiple Assignment**:

  ```python
  x, y, z = 1, 2, 3
  ```

- **Swap Values**:
  ```python
  a, b = 5, 10
  a, b = b, a  # Now a = 10, b = 5
  ```

### Numbers

- **Integer (int)**:

  ```python
  x = 10
  y = -5
  big_num = 1_000_000  # Underscore for readability
  ```

- **Float**:

  ```python
  x = 10.5
  y = -0.25
  scientific = 1.5e2  # Scientific notation (150.0)
  ```

- **Complex**:

  ```python
  z = 2 + 3j  # Complex number with real part 2 and imaginary part 3
  real_part = z.real  # 2.0
  imag_part = z.imag  # 3.0
  ```

- **Number Operations**:

  ```python
  # Basic operations
  sum_result = 10 + 20  # Addition
  difference = 20 - 10  # Subtraction
  product = 5 * 4  # Multiplication
  quotient = 20 / 5  # Division (returns float)
  floor_division = 20 // 3  # Floor division (returns int)
  remainder = 20 % 3  # Modulus (remainder)
  power = 2 ** 3  # Exponentiation

  # Math functions
  import math
  pi_value = math.pi
  sin_value = math.sin(math.pi/2)
  sqrt_value = math.sqrt(16)  # 4.0
  ```

### Strings

- **String Creation**:

  ```python
  s1 = 'Single quotes'
  s2 = "Double quotes"
  s3 = '''Triple quotes
  for multi-line strings'''
  ```

- **String Indexing and Slicing**:

  ```python
  text = "Python"
  first_char = text[0]  # 'P'
  last_char = text[-1]  # 'n'
  substring = text[1:4]  # 'yth'
  reversed_text = text[::-1]  # 'nohtyP'
  ```

- **String Methods**:

  ```python
  text = "  Python Programming  "

  # Case methods
  upper_text = text.upper()  # "  PYTHON PROGRAMMING  "
  lower_text = text.lower()  # "  python programming  "
  title_text = text.title()  # "  Python Programming  "

  # Whitespace methods
  stripped_text = text.strip()  # "Python Programming"

  # Search and replace
  replaced_text = text.replace("Python", "Java")  # "  Java Programming  "
  position = text.find("Pro")  # 9

  # Splitting and joining
  words = text.strip().split()  # ["Python", "Programming"]
  joined_text = "-".join(words)  # "Python-Programming"
  ```

- **String Formatting**:

  ```python
  # f-strings (Python 3.6+)
  name = "Alice"
  age = 30
  message = f"{name} is {age} years old"

  # format() method
  message = "{} is {} years old".format(name, age)

  # % operator
  message = "%s is %d years old" % (name, age)
  ```

### Booleans

- **Boolean Values**:

  ```python
  is_valid = True
  is_completed = False
  ```

- **Truthy and Falsy Values**:

  ```python
  # Falsy values
  falsy_values = [False, None, 0, "", [], {}, ()]

  # Everything else is truthy
  truthy_values = [True, 1, -1, "text", [0], {"key": "value"}]
  ```

- **Boolean Operations**:

  ```python
  a = True
  b = False

  and_result = a and b  # False
  or_result = a or b  # True
  not_result = not a  # False
  ```

### Type Conversion

- **Explicit Type Conversion**:

  ```python
  # To int
  int_from_str = int("10")  # 10
  int_from_float = int(10.5)  # 10 (truncates)

  # To float
  float_from_str = float("10.5")  # 10.5
  float_from_int = float(10)  # 10.0

  # To string
  str_from_int = str(10)  # "10"
  str_from_float = str(10.5)  # "10.5"
  ```

- **Type Checking**:

  ```python
  x = 10
  y = "Hello"

  type_of_x = type(x)  # <class 'int'>
  is_int = isinstance(x, int)  # True
  is_str = isinstance(y, str)  # True
  ```

## Control Flow

### Conditional Statements

- **If Statement**:

  ```python
  x = 10

  if x > 0:
      print("Positive")
  ```

- **If-Else Statement**:

  ```python
  x = -5

  if x > 0:
      print("Positive")
  else:
      print("Non-positive")
  ```

- **If-Elif-Else Statement**:

  ```python
  x = 0

  if x > 0:
      print("Positive")
  elif x < 0:
      print("Negative")
  else:
      print("Zero")
  ```

- **Conditional Expression (Ternary Operator)**:
  ```python
  x = 10
  message = "Positive" if x > 0 else "Non-positive"
  ```

### Loops

- **For Loop**:

  ```python
  # Iterate through a range
  for i in range(5):  # 0, 1, 2, 3, 4
      print(i)

  # Iterate through a list
  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(fruit)

  # Enumerate for index and value
  for index, fruit in enumerate(fruits):
      print(f"{index}: {fruit}")
  ```

- **While Loop**:

  ```python
  # Simple while loop
  count = 0
  while count < 5:
      print(count)
      count += 1

  # Break example
  count = 0
  while True:
      print(count)
      count += 1
      if count >= 5:
          break
  ```

- **Loop Control**:

  ```python
  # break - exit the loop
  for i in range(10):
      if i == 5:
          break
      print(i)  # Prints 0, 1, 2, 3, 4

  # continue - skip current iteration
  for i in range(10):
      if i % 2 == 0:
          continue
      print(i)  # Prints 1, 3, 5, 7, 9

  # else clause (executes when loop completes normally)
  for i in range(5):
      print(i)
  else:
      print("Loop completed")  # This runs if the loop finishes without a break
  ```

- **Nested Loops**:

  ```python
  # Multiplication table
  for i in range(1, 4):
      for j in range(1, 4):
          print(f"{i} * {j} = {i*j}")
  ```

- **List Comprehensions**:

  ```python
  # Create a list of squares
  squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

  # With condition
  even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

  # Nested
  matrix = [[i*j for j in range(3)] for i in range(3)]
  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
  ```

## Functions

### Function Definition and Calling

- **Basic Function**:

  ```python
  def greet(name):
      """This function greets the person with the given name"""
      return f"Hello, {name}!"

  # Calling the function
  message = greet("Alice")  # "Hello, Alice!"
  ```

- **Default Parameters**:

  ```python
  def greet(name, greeting="Hello"):
      """Greet with customizable greeting message"""
      return f"{greeting}, {name}!"

  # Different ways to call
  greet("Alice")  # "Hello, Alice!"
  greet("Alice", "Hi")  # "Hi, Alice!"
  ```

- **Keyword Arguments**:

  ```python
  def create_profile(name, age, city):
      """Create a user profile with the given information"""
      return f"{name} is {age} years old from {city}"

  # Using keyword arguments
  profile = create_profile(name="Alice", age=30, city="New York")
  profile = create_profile(age=30, city="New York", name="Alice")  # Order doesn't matter
  ```

- **Variable Number of Arguments**:

  ```python
  # *args for variable positional arguments
  def sum_all(*numbers):
      """Sum all the numbers passed as arguments"""
      return sum(numbers)

  result = sum_all(1, 2, 3, 4)  # 10

  # **kwargs for variable keyword arguments
  def print_info(**kwargs):
      """Print all the key-value pairs passed as arguments"""
      for key, value in kwargs.items():
          print(f"{key}: {value}")

  print_info(name="Alice", age=30, city="New York")
  ```

### Function Scope

- **Local and Global Variables**:

  ```python
  x = 10  # Global variable

  def func():
      y = 5  # Local variable
      print(x)  # Can access global variable
      print(y)  # Can access local variable

  func()
  print(x)  # Can access global variable
  # print(y)  # NameError: 'y' is not defined
  ```

- **Modifying Global Variables**:

  ```python
  x = 10

  def func():
      global x  # Declare global to modify
      x = 20

  func()
  print(x)  # 20
  ```

### Lambda Functions

- **Simple Lambda**:

  ```python
  # Regular function
  def add(x, y):
      return x + y

  # Equivalent lambda function
  add = lambda x, y: x + y

  result = add(5, 3)  # 8
  ```

- **Lambda with Higher-Order Functions**:

  ```python
  numbers = [1, 2, 3, 4, 5]

  # Map - apply function to each item
  squares = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

  # Filter - keep only items that match condition
  evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

  # Sorted with key
  pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
  sorted_pairs = sorted(pairs, key=lambda pair: pair[0])  # [(1, 'one'), (2, 'two'), (3, 'three')]
  ```

### Function Decorators

- **Basic Decorator**:

  ```python
  def my_decorator(func):
      """A decorator that adds behavior before and after a function call"""
      def wrapper():
          print("Before function call")
          func()
          print("After function call")
      return wrapper

  @my_decorator
  def say_hello():
      print("Hello!")

  say_hello()
  # Output:
  # Before function call
  # Hello!
  # After function call
  ```

- **Decorator with Arguments**:

  ```python
  def my_decorator(func):
      """A decorator that works with functions that take arguments"""
      def wrapper(*args, **kwargs):
          print("Before function call")
          result = func(*args, **kwargs)
          print("After function call")
          return result
      return wrapper

  @my_decorator
  def add(x, y):
      return x + y

  result = add(5, 3)  # 8
  ```

## Data Structures

### Lists

- **List Creation**:

  ```python
  # Empty list
  empty_list = []
  empty_list = list()

  # List with items
  numbers = [1, 2, 3, 4, 5]
  mixed = [1, "string", True, None, [1, 2]]  # Lists can contain different types
  ```

- **List Operations**:

  ```python
  numbers = [1, 2, 3, 4, 5]

  # Accessing elements
  first = numbers[0]  # 1
  last = numbers[-1]  # 5

  # Slicing - get a subset of the list
  subset = numbers[1:4]  # [2, 3, 4]
  reversed_list = numbers[::-1]  # [5, 4, 3, 2, 1]

  # Modifying
  numbers[0] = 10  # [10, 2, 3, 4, 5]

  # Length
  length = len(numbers)  # 5
  ```

- **List Methods**:

  ```python
  numbers = [1, 2, 3]

  # Adding elements
  numbers.append(4)  # [1, 2, 3, 4]
  numbers.insert(1, 10)  # [1, 10, 2, 3, 4]
  numbers.extend([5, 6])  # [1, 10, 2, 3, 4, 5, 6]

  # Removing elements
  numbers.remove(10)  # [1, 2, 3, 4, 5, 6]
  popped = numbers.pop()  # 6, numbers = [1, 2, 3, 4, 5]
  popped_index = numbers.pop(1)  # 2, numbers = [1, 3, 4, 5]
  numbers.clear()  # []

  # Finding elements
  numbers = [1, 2, 3, 2, 4]
  index = numbers.index(2)  # 1 (first occurrence)
  count = numbers.count(2)  # 2 (appears twice)

  # Sorting
  numbers.sort()  # [1, 2, 2, 3, 4]
  numbers.sort(reverse=True)  # [4, 3, 2, 2, 1]
  numbers.reverse()  # [1, 2, 2, 3, 4]
  ```

- **List Comprehensions**:

  ```python
  # Basic list comprehension
  squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

  # With condition
  even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

  # With if-else
  parity = ["even" if x % 2 == 0 else "odd" for x in range(5)]
  # ['even', 'odd', 'even', 'odd', 'even']
  ```

### Tuples

- **Tuple Creation**:

  ```python
  # Empty tuple
  empty_tuple = ()
  empty_tuple = tuple()

  # Tuple with items
  numbers = (1, 2, 3, 4, 5)
  mixed = (1, "string", True, None)

  # Single-item tuple (note the comma)
  single_item = (1,)  # Without the comma, it would be an integer
  ```

- **Tuple Operations**:

  ```python
  coordinates = (10, 20, 30)

  # Accessing elements
  x = coordinates[0]  # 10

  # Slicing
  subset = coordinates[1:]  # (20, 30)

  # Concatenation
  combined = coordinates + (40, 50)  # (10, 20, 30, 40, 50)

  # Unpacking
  x, y, z = coordinates  # x=10, y=20, z=30
  ```

- **Tuple Methods**:

  ```python
  numbers = (1, 2, 3, 2, 4)

  # Finding elements
  index = numbers.index(2)  # 1 (first occurrence)
  count = numbers.count(2)  # 2 (appears twice)
  ```

- **Tuple vs List**:

  ```python
  # Tuples are immutable - cannot be changed after creation
  t = (1, 2, 3)
  # t[0] = 10  # TypeError: 'tuple' object does not support item assignment

  # Lists are mutable - can be modified
  l = [1, 2, 3]
  l[0] = 10  # [10, 2, 3]
  ```

### Dictionaries

- **Dictionary Creation**:

  ```python
  # Empty dictionary
  empty_dict = {}
  empty_dict = dict()

  # Dictionary with items
  person = {
      "name": "Alice",
      "age": 30,
      "city": "New York"
  }

  # Using dict() constructor
  person = dict(name="Alice", age=30, city="New York")
  ```

- **Dictionary Operations**:

  ```python
  person = {"name": "Alice", "age": 30, "city": "New York"}

  # Accessing elements
  name = person["name"]  # "Alice"

  # Using get (safer, provides default)
  age = person.get("age")  # 30
  country = person.get("country", "Unknown")  # "Unknown" (default for missing key)

  # Modifying
  person["age"] = 31
  person["country"] = "USA"  # Add new key-value pair

  # Length
  length = len(person)  # 4
  ```

- **Dictionary Methods**:

  ```python
  person = {"name": "Alice", "age": 30}

  # Adding/updating items
  person.update({"city": "New York", "age": 31})

  # Removing items
  removed_age = person.pop("age")  # 31
  removed_item = person.popitem()  # ('city', 'New York') - removes and returns last item

  # Getting all keys, values, items
  keys = list(person.keys())  # ['name']
  values = list(person.values())  # ['Alice']
  items = list(person.items())  # [('name', 'Alice')]

  # Clearing
  person.clear()  # {}
  ```

- **Dictionary Comprehensions**:

  ```python
  # Basic dictionary comprehension
  squares = {x: x**2 for x in range(5)}
  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

  # With condition
  even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
  ```

### Sets

- **Set Creation**:

  ```python
  # Empty set (note: {} creates an empty dict)
  empty_set = set()

  # Set with items
  numbers = {1, 2, 3, 4, 5}
  mixed = {1, "string", True}  # Sets can have different types

  # Creating from other iterables
  from_list = set([1, 2, 3, 2, 1])  # {1, 2, 3} - duplicates are removed
  ```

- **Set Operations**:

  ```python
  a = {1, 2, 3, 4}
  b = {3, 4, 5, 6}

  # Union - all elements from both sets
  union = a | b  # {1, 2, 3, 4, 5, 6}
  union = a.union(b)

  # Intersection - elements common to both sets
  intersection = a & b  # {3, 4}
  intersection = a.intersection(b)

  # Difference - elements in first set but not in second
  difference = a - b  # {1, 2}
  difference = a.difference(b)

  # Symmetric difference - elements in either set but not in both
  sym_diff = a ^ b  # {1, 2, 5, 6}
  sym_diff = a.symmetric_difference(b)

  # Subset/superset
  is_subset = a <= b  # False
  is_superset = a >= b  # False
  ```

- **Set Methods**:

  ```python
  numbers = {1, 2, 3}

  # Adding elements
  numbers.add(4)  # {1, 2, 3, 4}
  numbers.update([4, 5, 6])  # {1, 2, 3, 4, 5, 6}

  # Removing elements
  numbers.remove(6)  # Raises KeyError if not found
  numbers.discard(7)  # No error if not found
  popped = numbers.pop()  # Removes and returns an arbitrary element
  numbers.clear()  # {}
  ```

- **Set Comprehensions**:

  ```python
  # Basic set comprehension
  squares = {x**2 for x in range(5)}
  # {0, 1, 4, 9, 16}

  # With condition
  even_squares = {x**2 for x in range(10) if x % 2 == 0}
  # {0, 4, 16, 36, 64}
  ```

## Object-Oriented Programming

### Classes and Objects

- **Class Definition**:

  ```python
  class Person:
      """A class representing a person with a name and age"""

      def __init__(self, name, age):
          """Initialize a new Person with name and age"""
          self.name = name
          self.age = age

      def greet(self):
          """Return a greeting message from this person"""
          return f"Hello, my name is {self.name}"

  # Creating an object (instance of the class)
  alice = Person("Alice", 30)

  # Accessing attributes
  name = alice.name  # "Alice"

  # Calling methods
  greeting = alice.greet()  # "Hello, my name is Alice"
  ```

- **Class and Instance Variables**:

  ```python
  class Person:
      species = "Homo sapiens"  # Class variable - shared by all instances

      def __init__(self, name):
          self.name = name  # Instance variable - unique to each instance

  alice = Person("Alice")
  bob = Person("Bob")

  # Access class variable
  print(Person.species)  # "Homo sapiens"
  print(alice.species)   # "Homo sapiens"

  # Modify class variable
  Person.species = "Human"
  print(bob.species)     # "Human"

  # Create instance variable with same name
  alice.species = "Individual"  # This creates a new instance variable, doesn't modify the class variable
  print(alice.species)   # "Individual"
  print(bob.species)     # "Human"
  ```

### Inheritance

- **Basic Inheritance**:

  ```python
  class Animal:
      """Base class for animals"""
      def __init__(self, name):
          self.name = name

      def speak(self):
          """Make the animal speak"""
          return "Some sound"

  class Dog(Animal):
      """Dog class that inherits from Animal"""
      def speak(self):
          """Override the speak method"""
          return "Woof!"

  class Cat(Animal):
      """Cat class that inherits from Animal"""
      def speak(self):
          """Override the speak method"""
          return "Meow!"

  # Creating objects
  dog = Dog("Buddy")
  cat = Cat("Whiskers")

  # Method overriding
  dog_sound = dog.speak()  # "Woof!"
  cat_sound = cat.speak()  # "Meow!"
  ```

- **Multiple Inheritance**:

  ```python
  class Flyable:
      """Class for things that can fly"""
      def fly(self):
          return "Flying..."

  class Swimmable:
      """Class for things that can swim"""
      def swim(self):
          return "Swimming..."

  class Duck(Animal, Flyable, Swimmable):
      """Duck class inheriting from Animal, Flyable, and Swimmable"""
      def speak(self):
          return "Quack!"

  # Creating object
  duck = Duck("Donald")

  # Accessing methods from all parent classes
  duck_sound = duck.speak()  # "Quack!"
  duck_fly = duck.fly()      # "Flying..."
  duck_swim = duck.swim()    # "Swimming..."
  ```

- **Method Resolution Order (MRO)**:

  ```python
  class A:
      def method(self):
          return "A"

  class B(A):
      def method(self):
          return "B"

  class C(A):
      def method(self):
          return "C"

  class D(B, C):
      pass

  # MRO determines which method is called
  d = D()
  result = d.method()  # "B" (follows inheritance order)

  # View MRO
  print(D.__mro__)  # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
  ```

### Special (Magic/Dunder) Methods

- **Common Special Methods**:

  ```python
  class Point:
      """A class representing a point in 2D space"""
      def __init__(self, x, y):
          """Initialize point with x and y coordinates"""
          self.x = x
          self.y = y

      def __str__(self):
          """Return string representation of Point"""
          return f"Point({self.x}, {self.y})"

      def __repr__(self):
          """Return detailed string representation of Point"""
          return f"Point({self.x}, {self.y})"

      def __eq__(self, other):
          """Compare if two Points are equal"""
          if not isinstance(other, Point):
              return False
          return self.x == other.x and self.y == other.y

      def __add__(self, other):
          """Add two Points together"""
          return Point(self.x + other.x, self.y + other.y)

      def __len__(self):
          """Return 'length' of point (distance from origin)"""
          return int((self.x ** 2 + self.y ** 2) ** 0.5)

  # Using special methods
  p1 = Point(3, 4)
  p2 = Point(1, 2)

  print(p1)            # "Point(3, 4)" (calls __str__)
  equality = p1 == p2  # False (calls __eq__)
  sum_point = p1 + p2  # Point(4, 6) (calls __add__)
  distance = len(p1)   # 5 (calls __len__)
  ```

### Properties and Descriptors

- **Using Properties**:

  ```python
  class Circle:
      """A class representing a circle with a radius"""
      def __init__(self, radius):
          self._radius = radius  # Use underscore for "private" attribute

      @property
      def radius(self):
          """Getter for radius property"""
          return self._radius

      @radius.setter
      def radius(self, value):
          """Setter for radius property with validation"""
          if value <= 0:
              raise ValueError("Radius must be positive")
          self._radius = value

      @property
      def diameter(self):
          """Calculate diameter from radius"""
          return self.radius * 2

      @property
      def area(self):
          """Calculate area from radius"""
          return 3.14159 * self.radius ** 2

  # Using properties
  circle = Circle(5)

  # Getting properties
  radius = circle.radius    # 5
  diameter = circle.diameter  # 10
  area = circle.area        # ~78.54

  # Setting property with validation
  circle.radius = 10        # Works fine
  # circle.radius = -5      # Raises ValueError
  ```

## File Operations

### Text File I/O

- **Reading Files**:

  ```python
  # Reading entire file
  with open('file.txt', 'r') as file:
      content = file.read()  # Read entire file as a string

  # Reading line by line
  with open('file.txt', 'r') as file:
      lines = file.readlines()  # List of lines with newline characters

  # Iterating line by line (memory efficient)
  with open('file.txt', 'r') as file:
      for line in file:  # File object is iterable
          print(line.strip())  # Remove trailing newline
  ```

- **Writing Files**:

  ```python
  # Writing string to file (overwrites)
  with open('file.txt', 'w') as file:
      file.write("Hello, World!")

  # Writing multiple lines
  lines = ["Line 1", "Line 2", "Line 3"]
  with open('file.txt', 'w') as file:
      file.write('\n'.join(lines))  # Join lines with newline

  # Appending to file
  with open('file.txt', 'a') as file:
      file.write("\nAppended line")
  ```

### Binary File I/O

- **Reading/Writing Binary Files**:

  ```python
  # Reading binary file
  with open('image.jpg', 'rb') as file:
      data = file.read()  # Read as bytes

  # Writing binary file
  with open('copy.jpg', 'wb') as file:
      file.write(data)  # Write bytes
  ```

### File and Directory Operations

- **File Paths**:

  ```python
  import os

  # Join paths properly for any OS
  path = os.path.join('folder', 'subfolder', 'file.txt')

  # Get components
  directory = os.path.dirname(path)  # 'folder/subfolder'
  filename = os.path.basename(path)  # 'file.txt'
  name, extension = os.path.splitext(filename)  # ('file', '.txt')

  # Check file properties
  exists = os.path.exists(path)  # True if file exists
  is_file = os.path.isfile(path)  # True if it's a file
  is_dir = os.path.isdir(path)  # True if it's a directory
  ```

- **Directory Operations**:

  ```python
  import os

  # List directory contents
  files = os.listdir('folder')  # List of filenames

  # Create directory
  os.mkdir('new_folder')  # Create single directory
  os.makedirs('path/to/nested/folder', exist_ok=True)  # Create nested directories

  # Remove files and directories
  os.remove('file.txt')  # Delete file
  os.rmdir('empty_folder')  # Delete empty directory
  ```

- **Path Operations with pathlib (modern)**:

  ```python
  from pathlib import Path

  # Create path objects
  path = Path('folder') / 'subfolder' / 'file.txt'  # Path concatenation

  # Path components
  directory = path.parent  # Path object for parent directory
  filename = path.name  # 'file.txt'
  stem = path.stem  # 'file'
  suffix = path.suffix  # '.txt'

  # Check properties
  exists = path.exists()  # True if path exists
  is_file = path.is_file()  # True if it's a file
  is_dir = path.is_dir()  # True if it's a directory

  # Directory operations
  files = list(Path('folder').iterdir())  # List of Path objects

  # Create/remove directories
  Path('new_folder').mkdir(exist_ok=True)  # Create directory
  Path('new_folder').rmdir()  # Remove directory
  ```

## Error Handling

### Try-Except Blocks

- **Basic Exception Handling**:

  ```python
  try:
      x = 1 / 0  # This will raise a ZeroDivisionError
  except:
      print("An error occurred")  # Catch any exception
  ```

- **Handling Specific Exceptions**:

  ```python
  try:
      value = int("abc")  # This will raise a ValueError
  except ValueError:
      print("Invalid integer")
  except ZeroDivisionError:
      print("Division by zero")
  ```

- **Handling Multiple Exceptions**:

  ```python
  try:
      value = int("abc")
  except (ValueError, TypeError):  # Catch either ValueError or TypeError
      print("Conversion error")
  ```

- **Else and Finally Clauses**:
  ```python
  try:
      value = int("123")
  except ValueError:
      print("Invalid integer")
  else:
      print("No exceptions occurred")  # Runs if no exceptions
  finally:
      print("This always executes")  # Always runs
  ```

### Raising Exceptions

- **Raising Exceptions**:

  ```python
  def divide(a, b):
      """Divide a by b"""
      if b == 0:
          raise ZeroDivisionError("Cannot divide by zero")
      return a / b

  # Custom error message
  name = "Alice"
  if len(name) > 10:
      raise ValueError(f"Name too long: {name}")
  ```

- **Re-raising Exceptions**:
  ```python
  try:
      x = 1 / 0
  except ZeroDivisionError:
      print("Logging error...")
      raise  # Re-raises the caught exception
  ```

### Custom Exceptions

- **Creating Custom Exceptions**:

  ```python
  class CustomError(Exception):
      """Base class for custom exceptions"""
      pass

  class ValueTooSmallError(CustomError):
      """Raised when value is too small"""
      def __init__(self, value, min_value):
          self.value = value
          self.min_value = min_value
          self.message = f"Value {value} is smaller than minimum {min_value}"
          super().__init__(self.message)

  # Using custom exception
  def validate(value, min_value):
      """Validate that value is at least min_value"""
      if value < min_value:
          raise ValueTooSmallError(value, min_value)
      return value

  try:
      validate(5, 10)
  except ValueTooSmallError as e:
      print(e.message)
  ```

### Context Managers

- **Using Context Managers**:

  ```python
  # File handling with context manager
  with open('file.txt', 'r') as file:
      content = file.read()
  # File is automatically closed

  # Multiple context managers
  with open('input.txt', 'r') as in_file, open('output.txt', 'w') as out_file:
      content = in_file.read()
      out_file.write(content.upper())
  ```

- **Creating Context Managers**:

  ```python
  # Using a class
  class MyContext:
      """A simple context manager class"""
      def __enter__(self):
          print("Entering context")
          return self

      def __exit__(self, exc_type, exc_val, exc_tb):
          print("Exiting context")
          # Return True to suppress exceptions
          return False

  # Using the contextlib module
  from contextlib import contextmanager

  @contextmanager
  def my_context():
      """A simple context manager function"""
      print("Entering context")
      try:
          yield  # This is where the nested code runs
      finally:
          print("Exiting context")

  # Using the context manager
  with MyContext() as ctx:
      print("Inside context")

  with my_context():
      print("Inside context")
  ```

## Modules and Packages

### Understanding Python Modules

- **What are Modules?**
  Modules are files containing Python code. They can define functions, classes, and variables that you can use in other Python programs. Modules help organize code into logical units, making it more maintainable and reusable.

### Importing Modules

- **Basic Imports**:

  ```python
  # Import entire module
  import math
  result = math.sqrt(16)  # 4.0

  # Import specific items
  from math import sqrt, pi
  result = sqrt(16)  # 4.0

  # Import with alias
  import math as m
  result = m.sqrt(16)  # 4.0

  # Import all (not recommended)
  from math import *
  result = sqrt(16)  # 4.0
  ```

- **Importing Packages**:

  ```python
  # Import package
  import os.path
  name = os.path.basename('/path/to/file.txt')  # 'file.txt'

  # Import from package
  from os import path
  name = path.basename('/path/to/file.txt')  # 'file.txt'
  ```

### Creating Modules

- **Creating a Simple Module**:

  ```python
  # mymodule.py
  def greet(name):
      """Function to greet a person by name"""
      return f"Hello, {name}!"

  PI = 3.14159

  class Person:
      """Class representing a person"""
      def __init__(self, name):
          self.name = name

  # Using the module
  import mymodule
  message = mymodule.greet("Alice")
  ```

- **Module `__name__`**:

  ```python
  # mymodule.py
  def greet(name):
      """Function to greet a person by name"""
      return f"Hello, {name}!"

  # Code that runs only when executed directly
  if __name__ == "__main__":
      print("Module executed directly")
      print(greet("World"))
  ```

### Creating Packages

- **Package Structure**:

  ```
  mypackage/
  ├── __init__.py        # Makes directory a package
  ├── module1.py         # Module within package
  ├── module2.py         # Another module
  └── subpackage/        # Subpackage
      ├── __init__.py    # Makes subdirectory a package
      └── module3.py     # Module within subpackage
  ```

- **`__init__.py` File**:

  ```python
  # mypackage/__init__.py
  from . import module1
  from . import module2
  from .subpackage import module3

  # Define what gets imported with "from mypackage import *"
  __all__ = ['module1', 'module2']
  ```

- **Relative Imports**:
  ```python
  # mypackage/module1.py
  from . import module2  # Import sibling module
  from .subpackage import module3  # Import from subpackage
  from .. import other_package  # Import from parent package
  ```

## Python Internals

### Execution Model

Python's execution model follows several key steps when running code:

- **Parsing**: Python reads your code and checks for syntax errors
- **Compilation**: Your code is compiled to bytecode (.pyc files)
- **Interpretation**: The Python virtual machine (PVM) executes the bytecode

```python
def greet(name):
    """Greet a person by name"""
    message = f"Hello, {name}!"
    return message

result = greet("Alice")
print(result)  # Output: Hello, Alice!

```

**Key Concepts:**

1. **Interpreted Language**: Python code is executed line by line by the interpreter, making it more flexible but potentially slower than compiled languages.

2. **Dynamic Typing**: Python determines variable types at runtime rather than compile time.

   ```python
   x = 5       # x is an integer
   x = "hello" # x is now a string
   ```

3. **Name Binding**: In Python, variables are just names that refer to objects in memory.
   ```python
   a = [1, 2, 3]  # 'a' refers to a list object in memory
   b = a          # 'b' now refers to the same list object
   b.append(4)    # modifies the object
   print(a)       # [1, 2, 3, 4] - 'a' also reflects the change
   ```

### Memory Management

Python manages memory automatically through its built-in garbage collection mechanisms:

1. **Reference Counting**: Each object has a reference count (how many variables refer to it). When the count reaches zero, the object is garbage collected.

2. **Cycle Detection**: To handle circular references, Python uses a cycle detector to find and collect unreachable objects periodically.

```python
import sys

a = "hello"
print(sys.getrefcount(a) - 1)  # Subtract 1 because getrefcount() creates another reference

b = a
print(sys.getrefcount(a) - 1)  # Count increases

b = None
print(sys.getrefcount(a) - 1)  # Count decreases
```

**Memory Allocation:**

- Python's memory manager handles allocation of memory for Python objects
- Small objects (< 512 bytes) use a special allocator for efficiency
- Large objects use the system's malloc() function

**Garbage Collection:**

```python
import gc

gc.collect()

print(gc.get_count())

gc.disable()
gc.enable()
```

### Global Interpreter Lock (GIL)

The GIL is a mutex (lock) that allows only one thread to execute Python bytecode at a time. This means that even in multi-threaded applications, Python can only execute one thread at a time.

**Important Implications:**

1. **CPU-bound Tasks**: For CPU-intensive operations, threads cannot execute in true parallel on multiple CPU cores due to the GIL.

2. **I/O-bound Tasks**: For I/O operations (file, network, etc.), the GIL is released while waiting, so threaded I/O operations can still benefit from concurrency.

3. **Workarounds**:
   - Use `multiprocessing` instead of `threading` for CPU-bound tasks
   - Use `asyncio` for I/O-bound tasks
   - Use C extensions that release the GIL for CPU-intensive operations

```python
import threading
import time

def cpu_bound_task(n):
    """A CPU-intensive function"""
    count = 0
    for i in range(n):
        count += i
    return count

start = time.time()
cpu_bound_task(10000000)
cpu_bound_task(10000000)
end = time.time()
print(f"Sequential time: {end - start:.2f} seconds")

start = time.time()
t1 = threading.Thread(target=cpu_bound_task, args=(10000000,))
t2 = threading.Thread(target=cpu_bound_task, args=(10000000,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"Threaded time: {end - start:.2f} seconds")

import multiprocessing as mp

start = time.time()
p1 = mp.Process(target=cpu_bound_task, args=(10000000,))
p2 = mp.Process(target=cpu_bound_task, args=(10000000,))
p1.start()
p2.start()
p1.join()
p2.join()
end = time.time()
print(f"Multiprocessing time: {end - start:.2f} seconds")
```

**When is the GIL Released?**

- During I/O operations (file, network, etc.)
- During `time.sleep()`
- When executing C extensions that explicitly release the GIL
- In some standard library functions (e.g., certain operations in `numpy`)

### Threading

- **Basic Threading**:

  ```python
  import threading
  import time

  def worker(name):
      """Function for a worker thread"""
      print(f"Worker {name} starting")
      time.sleep(2)  # Simulate some work
      print(f"Worker {name} finished")

  # Create threads
  threads = []
  for i in range(3):
      # Create a thread with a target function and arguments
      t = threading.Thread(target=worker, args=(i,))
      threads.append(t)
      t.start()  # Start the thread

  # Wait for all threads to complete
  for t in threads:
      t.join()

  print("All workers finished")
  ```

- **Thread Synchronization**:

  ```python
  import threading
  import time

  # Shared resource
  counter = 0
  counter_lock = threading.Lock()  # Create a lock object

  def increment():
      """Increment the counter safely using a lock"""
      global counter
      for _ in range(100000):
          with counter_lock:  # Thread-safe operation
              counter += 1

  # Create threads
  threads = []
  for _ in range(10):
      t = threading.Thread(target=increment)
      threads.append(t)
      t.start()

  # Wait for all threads to complete
  for t in threads:
      t.join()

  print(f"Final counter value: {counter}")  # Should be 1,000,000
  ```

- **Thread Communication with Event**:

  ```python
  import threading
  import time

  # Event for thread communication
  event = threading.Event()

  def waiter():
      """Wait for an event to be set"""
      print("Waiter: Waiting for event...")
      event.wait()  # Block until event is set
      print("Waiter: Event received, proceeding")

  def setter():
      """Set the event after a delay"""
      print("Setter: Sleeping for 2 seconds...")
      time.sleep(2)
      print("Setter: Setting event")
      event.set()  # Set the event, unblocking all waiters

  # Create threads
  t1 = threading.Thread(target=waiter)
  t2 = threading.Thread(target=setter)

  # Start threads
  t1.start()
  t2.start()

  # Wait for threads to finish
  t1.join()
  t2.join()

  print("All threads completed")
  ```

- **Thread Pool with `concurrent.futures`**:

  ```python
  from concurrent.futures import ThreadPoolExecutor
  import time

  def task(name):
      """A simple task for the thread pool"""
      print(f"Task {name} starting")
      time.sleep(1)  # Simulate some work
      return f"Task {name} result"

  # Using a thread pool
  with ThreadPoolExecutor(max_workers=3) as executor:
      # Submit tasks to the pool
      futures = [executor.submit(task, i) for i in range(5)]

      # Get results as they complete
      for future in futures:
          print(future.result())

      # Alternative: map function
      results = list(executor.map(task, range(5)))
      print(results)
  ```

- **Thread-Local Storage**:

  ```python
  import threading

  # Thread-local storage
  local_data = threading.local()

  def worker(name):
      """Worker that uses thread-local storage"""
      # Set thread-local data
      local_data.name = name

      # Access thread-local data
      print(f"Worker {local_data.name} running")

  # Create threads
  threads = []
  for i in range(3):
      t = threading.Thread(target=worker, args=(f"Thread-{i}",))
      threads.append(t)
      t.start()

  # Wait for all threads to complete
  for t in threads:
      t.join()
  ```

### Multiprocessing

- **Basic Multiprocessing**:

  ```python
  from multiprocessing import Process
  import os

  def worker(name):
      """Function for a worker process"""
      print(f"Worker {name} starting, PID: {os.getpid()}")
      # CPU-bound task goes here
      print(f"Worker {name} finished")

  if __name__ == '__main__':
      # IMPORTANT: Always protect the entry point with if __name__ == '__main__'
      # for multiprocessing to work properly, especially on Windows

      processes = []
      for i in range(3):
          p = Process(target=worker, args=(i,))
          processes.append(p)
          p.start()

      for p in processes:
          p.join()

      print("All workers finished")
  ```

- **Process Pool**:

  ```python
  from multiprocessing import Pool

  def process_data(x):
      """Process a piece of data (CPU-intensive task)"""
      # Simulate CPU-intensive task
      return x * x

  if __name__ == '__main__':
      # Create a pool of worker processes
      with Pool(processes=4) as pool:
          # Process data in parallel
          data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          results = pool.map(process_data, data)  # Parallel map
          print(results)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

          # Alternative: imap for processing results as they complete
          for result in pool.imap(process_data, data):
              print(result)
  ```

- **Shared Memory**:

  ```python
  from multiprocessing import Process, Value, Array

  def increment(counter):
      """Increment a shared counter"""
      for _ in range(100):
          # Automatic locking with Value object
          with counter.get_lock():
              counter.value += 1

  def modify_array(arr):
      """Modify a shared array"""
      for i in range(len(arr)):
          arr[i] *= 2

  if __name__ == '__main__':
      # Shared value between processes
      counter = Value('i', 0)  # 'i' is for integer

      # Shared array
      arr = Array('i', [1, 2, 3, 4, 5])

      # Create processes
      p1 = Process(target=increment, args=(counter,))
      p2 = Process(target=increment, args=(counter,))
      p3 = Process(target=modify_array, args=(arr,))

      # Start and join processes
      p1.start()
      p2.start()
      p3.start()

      p1.join()
      p2.join()
      p3.join()

      print(f"Final counter value: {counter.value}")  # Should be 200
      print(f"Final array: {list(arr)}")  # Should be [2, 4, 6, 8, 10]
  ```

- **Process Communication with Queues**:

  ```python
  from multiprocessing import Process, Queue
  import time

  def producer(queue):
      """Produce items and put them in the queue"""
      for i in range(5):
          item = f"Item {i}"
          queue.put(item)  # Add item to queue
          print(f"Producer: {item}")
          time.sleep(0.5)

  def consumer(queue):
      """Consume items from the queue"""
      while True:
          try:
              item = queue.get(timeout=2)  # Get item with timeout
              print(f"Consumer: {item}")
          except:
              # Queue is empty and timeout reached
              break

  if __name__ == '__main__':
      # Create shared queue
      queue = Queue()

      # Create processes
      p1 = Process(target=producer, args=(queue,))
      p2 = Process(target=consumer, args=(queue,))

      # Start and join processes
      p1.start()
      p2.start()

      p1.join()
      p2.join()

      print("All processes finished")
  ```

### Asynchronous Programming

- **Basics of Async/Await**:

  ```python
  import asyncio

  async def hello_world():
      """Simple async function"""
      print("Hello")
      await asyncio.sleep(1)  # Non-blocking sleep
      print("World")

  # Run the async function
  asyncio.run(hello_world())
  ```

- **Running Multiple Tasks**:

  ```python
  import asyncio

  async def task1():
      """First async task"""
      await asyncio.sleep(1)  # Simulate I/O operation
      return "Task 1 result"

  async def task2():
      """Second async task"""
      await asyncio.sleep(2)  # Simulate I/O operation
      return "Task 2 result"

  async def main():
      """Main async function to run multiple tasks"""
      # Run tasks concurrently
      results = await asyncio.gather(task1(), task2())
      # Both tasks run in parallel, total time is max(1, 2) = 2 seconds
      print(results)  # ["Task 1 result", "Task 2 result"]

      # Alternative: create and await tasks explicitly
      t1 = asyncio.create_task(task1())
      t2 = asyncio.create_task(task2())
      await t1
      await t2
      print(f"{t1.result()}, {t2.result()}")

  # Run the main async function
  asyncio.run(main())
  ```

- **Async Context Managers and Iterators**:

  ```python
  import asyncio

  class AsyncTimer:
      """Async context manager for timing"""
      async def __aenter__(self):
          """Enter the async context"""
          self.start = asyncio.get_event_loop().time()
          return self

      async def __aexit__(self, exc_type, exc_val, exc_tb):
          """Exit the async context"""
          end = asyncio.get_event_loop().time()
          print(f"Time taken: {end - self.start:.2f} seconds")

  class AsyncCounter:
      """Async iterator that counts up to max_count"""
      def __init__(self, max_count):
          self.max_count = max_count
          self.count = 0

      def __aiter__(self):
          """Return the async iterator object"""
          return self

      async def __anext__(self):
          """Get the next value or raise StopAsyncIteration"""
          if self.count >= self.max_count:
              raise StopAsyncIteration
          self.count += 1
          await asyncio.sleep(0.1)  # Simulate async operation
          return self.count

  async def main():
      """Main function demonstrating async features"""
      # Using async context manager
      async with AsyncTimer():
          await asyncio.sleep(1)

      # Using async iterator
      async for count in AsyncCounter(5):
          print(count)  # 1, 2, 3, 4, 5

  # Run the main async function
  asyncio.run(main())
  ```

- **Handling Async Exceptions**:

  ```python
  import asyncio

  async def risky_task():
      """Task that might raise an exception"""
      await asyncio.sleep(1)
      raise ValueError("Something went wrong!")

  async def main():
      """Handle exceptions in async code"""
      try:
          await risky_task()
      except ValueError as e:
          print(f"Caught exception: {e}")

      # Alternative: with asyncio.gather
      try:
          await asyncio.gather(risky_task(), risky_task())
      except ValueError as e:
          print(f"Caught exception from gather: {e}")

      # To get exceptions as results instead of raising them
      results = await asyncio.gather(
          risky_task(),
          risky_task(),
          return_exceptions=True
      )
      for result in results:
          if isinstance(result, Exception):
              print(f"Task resulted in exception: {result}")

  # Run the main async function
  asyncio.run(main())
  ```

- **Real-World Async Example (HTTP Requests)**:

  ```python
  import asyncio
  import aiohttp  # You would need to install this: pip install aiohttp

  async def fetch_url(session, url):
      """Fetch a URL asynchronously"""
      async with session.get(url) as response:
          return await response.text()

  async def fetch_multiple_urls(urls):
      """Fetch multiple URLs concurrently"""
      async with aiohttp.ClientSession() as session:
          # Create tasks for each URL
          tasks = [fetch_url(session, url) for url in urls]
          # Await all tasks to complete
          results = await asyncio.gather(*tasks)
          return results

  async def main():
      """Main function to demonstrate async HTTP requests"""
      urls = [
          "https://example.com",
          "https://python.org",
          "https://github.com"
      ]
      results = await fetch_multiple_urls(urls)
      for url, html in zip(urls, results):
          print(f"Fetched {url}: {len(html)} characters")

  # Note: To run this example, you need to install aiohttp
  # Run the main async function
  # asyncio.run(main())
  ```

## Standard Libraries

### `datetime` Module

- **Date and Time Objects**:

  ```python
  from datetime import datetime, date, time, timedelta

  # Current date and time
  now = datetime.now()
  today = date.today()

  # Creating date/time objects
  birthday = date(1990, 1, 1)
  meeting = time(14, 30, 0)  # 2:30 PM
  event = datetime(2023, 12, 31, 23, 59, 59)

  # Date arithmetic
  tomorrow = today + timedelta(days=1)
  two_hours_later = now + timedelta(hours=2)

  # Formatting
  formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # '2023-01-01 12:34:56'

  # Parsing
  parsed = datetime.strptime("2023-01-01", "%Y-%m-%d")
  ```

### `collections` Module

- **Specialized Collections**:

  ```python
  from collections import Counter, defaultdict, deque, namedtuple

  # Counter - count occurrences of elements
  words = ["apple", "banana", "apple", "orange", "banana", "apple"]
  word_counts = Counter(words)
  most_common = word_counts.most_common(2)  # [('apple', 3), ('banana', 2)]

  # defaultdict - dictionary with default factory
  word_categories = defaultdict(list)  # Default value is empty list
  word_categories["fruits"].append("apple")  # No KeyError for new keys

  # deque (double-ended queue)
  queue = deque(["a", "b", "c"])
  queue.append("d")  # Add to right: deque(['a', 'b', 'c', 'd'])
  queue.appendleft("z")  # Add to left: deque(['z', 'a', 'b', 'c', 'd'])

  # namedtuple - tuple with named fields
  Person = namedtuple("Person", ["name", "age", "city"])
  alice = Person("Alice", 30, "New York")
  name = alice.name  # "Alice"
  ```

### `json` Module

- **JSON Serialization**:

  ```python
  import json

  # Python object to JSON string
  data = {"name": "Alice", "age": 30, "city": "New York"}
  json_string = json.dumps(data, indent=2)  # Pretty-print with indentation

  # JSON string to Python object
  parsed_data = json.loads(json_string)

  # Writing JSON to file
  with open("data.json", "w") as file:
      json.dump(data, file, indent=2)

  # Reading JSON from file
  with open("data.json", "r") as file:
      loaded_data = json.load(file)
  ```

### `re` Module

- **Regular Expressions**:

  ```python
  import re

  text = "The quick brown fox jumps over the lazy dog. The dog sleeps."

  # Search - find first match
  match = re.search(r"fox", text)
  if match:
      print("Found at position:", match.start())

  # Match at beginning
  match = re.match(r"The", text)  # Only matches at start of string

  # Find all occurrences
  matches = re.findall(r"The", text)  # ['The', 'The']

  # Split
  parts = re.split(r"\.", text)  # Split by period

  # Replace
  new_text = re.sub(r"dog", "cat", text)  # Replace dog with cat

  # Compile for reuse
  pattern = re.compile(r"\w+")  # Match words
  words = pattern.findall(text)  # List of all words
  ```

### `os` and `sys` Modules

- **OS Operations**:

  ```python
  import os

  # Current working directory
  cwd = os.getcwd()

  # Environment variables
  home = os.environ.get('HOME')  # Access env variable safely

  # Join paths correctly for any OS
  path = os.path.join('folder', 'subfolder', 'file.txt')

  # Run system command
  os.system('echo "Hello"')  # Execute shell command
  ```

- **System Information**:

  ```python
  import sys

  # Python version
  version = sys.version

  # Command line arguments
  args = sys.argv  # List of arguments

  # Module search path
  paths = sys.path  # Where Python looks for modules

  # Exit program
  sys.exit(0)  # 0 means successful exit
  ```

### `logging` Module

- **Basic Logging**:

  ```python
  import logging

  # Configure logging
  logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      filename='app.log'
  )

  # Log messages at different levels
  logging.debug('Debug message')  # Won't show (level is INFO)
  logging.info('Info message')
  logging.warning('Warning message')
  logging.error('Error message')
  logging.critical('Critical message')
  ```

- **Creating a Custom Logger**:

  ```python
  import logging

  # Create logger
  logger = logging.getLogger('my_app')
  logger.setLevel(logging.DEBUG)

  # Create handler
  handler = logging.FileHandler('app.log')
  handler.setLevel(logging.INFO)

  # Create formatter
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)

  # Add handler to logger
  logger.addHandler(handler)

  # Use logger
  logger.debug('Debug message')
  logger.info('Info message')
  ```

### `itertools` Module

- **Combinatorial Iterators**:

  ```python
  import itertools

  # Combinations - order doesn't matter
  combinations = list(itertools.combinations([1, 2, 3, 4], 2))
  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

  # Permutations - order matters
  permutations = list(itertools.permutations([1, 2, 3], 2))
  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

  # Cartesian product
  product = list(itertools.product([1, 2], ['a', 'b']))
  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
  ```

- **Infinite Iterators**:

  ```python
  # Count (start, step)
  counter = itertools.count(start=10, step=5)
  for _ in range(5):
      print(next(counter))  # 10, 15, 20, 25, 30

  # Cycle - repeat elements
  cycler = itertools.cycle(['A', 'B', 'C'])
  for _ in range(5):
      print(next(cycler))  # A, B, C, A, B

  # Repeat - repeat single element
  repeater = itertools.repeat('X', 3)  # Repeat 'X' 3 times
  for item in repeater:
      print(item)  # X, X, X
  ```

## Working with External Libraries

### Understanding Python Package Management

Python's package ecosystem is vast and powerful. The standard library provides essential functionality, but external libraries extend Python's capabilities for specialized tasks. Here's how to work with them:

### Installing External Libraries

- **Using pip (Python's Package Installer)**:

  ```bash
  # Basic installation
  pip install package_name

  # Install specific version
  pip install package_name==1.2.3

  # Upgrade existing package
  pip install --upgrade package_name

  # Install from requirements file
  pip install -r requirements.txt
  ```

- **Managing Package Dependencies**:

  ```bash
  # Generate requirements file from installed packages
  pip freeze > requirements.txt

  # List installed packages
  pip list

  # Show package information
  pip show package_name

  # Uninstall package
  pip uninstall package_name
  ```

### Using Virtual Environments

- **Creating a Virtual Environment**:

  ```bash
  # Create a virtual environment
  python -m venv myenv

  # Activate virtual environment
  # On Windows:
  myenv\Scripts\activate

  # On macOS/Linux:
  source myenv/bin/activate

  # Deactivate
  deactivate
  ```

- **Benefits of Virtual Environments**:
  1. **Isolation**: Each project can have its own dependencies
  2. **Dependency Management**: Avoid conflicts between package versions
  3. **Clean Environment**: Start with only the packages you need
  4. **Reproducibility**: Easy to recreate the environment on another machine

### Finding and Evaluating Packages

- **Sources for Python Packages**:

  1. **PyPI (Python Package Index)**: The official repository (https://pypi.org)
  2. **GitHub**: Many libraries are hosted on GitHub
  3. **Documentation**: Official project documentation sites

- **Evaluating Package Quality**:
  1. **Activity**: When was it last updated?
  2. **Community**: How many people use it? Are issues addressed?
  3. **Documentation**: Is it well-documented with examples?
  4. **Testing**: Does it have tests? What's the coverage?
  5. **License**: Is the license compatible with your project?

### Common External Library Categories

- **Web Development**: Django, Flask, FastAPI
- **Data Science**: NumPy, Pandas, Matplotlib, scikit-learn
- **Machine Learning**: TensorFlow, PyTorch, Keras
- **Web Scraping**: Beautiful Soup, Scrapy, Selenium
- **Database Access**: SQLAlchemy, psycopg2, PyMySQL
- **Testing**: pytest, unittest, nose
- **Automation**: Ansible, Fabric
- **GUI Development**: Tkinter, PyQt, wxPython
