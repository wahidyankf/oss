"""
Python Operators Masterclass

This enhanced demo provides:
1. Complete coverage of all Python operator categories
2. Practical examples with clear output
3. Special cases and edge behaviors explained
4. Operator precedence rules with visual examples
5. Real-world use cases for each operator type
"""

# ========== ARITHMETIC OPERATORS ==========
"""
Arithmetic Operators:
+ : Addition (also string/list concatenation)
- : Subtraction (also set difference)
* : Multiplication (also string/list repetition)
/ : True division (always returns float)
// : Floor division (returns integer)
% : Modulus (remainder after division)
** : Exponentiation (power of)

Special Cases:
- Division by zero handling
- Mixed numeric type operations
- Operator overloading in custom classes
"""
print("=== ARITHMETIC OPERATORS ===")
a, b = 15, 4

# Basic arithmetic
print(f"{a} + {b} = {a + b}")  # 19
print(f"{a} - {b} = {a - b}")  # 11
print(f"{a} * {b} = {a * b}")  # 60

# Division types
print(f"{a} / {b} = {a / b}")  # 3.75 (true division)
print(f"{a} // {b} = {a // b}")  # 3 (floor division)
print(f"{a} % {b} = {a % b}")  # 3 (remainder)
print(f"{a} ** {b} = {a ** b}")  # 50625 (15^4)

# Special cases
try:
    print(f"{a} / 0 = {a / 0}")  # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")

# Mixed type operations
print(f"5 / 2 = {5 / 2}")  # 2.5 (float)
print(f"5 // 2.0 = {5 // 2.0}")  # 2.0 (float result)

# ========== COMPARISON OPERATORS ==========
"""
Comparison Operators:
== : Equal to
!= : Not equal to
> : Greater than
< : Less than
>= : Greater than or equal
<= : Less than or equal

Features:
- Chained comparisons (1 < x < 10)
- Works with all comparable types
- Returns boolean (True/False)
"""
print("\n=== COMPARISON OPERATORS ===")

# Numeric comparisons
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} > {b}: {a > b}")  # True

# Chained comparisons
x = 7
print(f"1 < {x} < 10: {1 < x < 10}")  # True

# String comparisons (lexicographical)
print(f"'apple' == 'orange': {'apple' == 'orange'}")  # False
print(f"'apple' < 'orange': {'apple' < 'orange'}")  # True

# ========== LOGICAL OPERATORS ==========
"""
Logical Operators:
and : Both must be True
or : Either must be True
not : Inverts the boolean

Key Behaviors:
- Short-circuit evaluation
- Truthy/falsy values
- Operator precedence
"""
print("\n=== LOGICAL OPERATORS ===")

# Basic usage
print(f"True and False: {True and False}")  # False
print(f"True or False: {True or False}")  # True
print(f"not True: {not True}")  # False


# Short-circuit examples
def check():
    print("Function called!")
    return True


print("\nShort-circuit demo:")
print("False and check():", False and check())  # check() not called
print("True or check():", True or check())  # check() not called

# Truthy/falsy values
print("\nTruthy/Falsy examples:")
print(f"bool(0): {bool(0)}")  # False
print(f"bool(42): {bool(42)}")  # True
print(f"bool(''): {bool('')}")  # False
print(f"bool('hello'): {bool('hello')}")  # True

# ========== ASSIGNMENT OPERATORS ==========
"""
Assignment Operators:
= : Basic assignment
+= : Add and assign
-= : Subtract and assign
*= : Multiply and assign
/= : Divide and assign
//= : Floor divide and assign
%= : Modulus and assign
**= : Exponent and assign

Usage:
- In-place modifications
- Works with mutable/immutable types
"""
print("\n=== ASSIGNMENT OPERATORS ===")

# Basic assignment
counter = 0
print(f"Initial counter: {counter}")

# Augmented assignments
counter += 5  # counter = counter + 5
print(f"After += 5: {counter}")

counter *= 2  # counter = counter * 2
print(f"After *= 2: {counter}")

counter **= 2  # counter = counter squared
print(f"After **= 2: {counter}")

# List operations
items = [1, 2, 3]
items += [4, 5]  # Extends list
print(f"Extended list: {items}")

# ========== MEMBERSHIP OPERATORS ==========
"""
Membership Operators:
in : True if value exists in sequence
not in : True if value doesn't exist

Works with:
- Strings, lists, tuples, sets, dicts
- Custom containers with __contains__
"""
print("\n=== MEMBERSHIP OPERATORS ===")

# List membership
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")  # True
print(f"'mango' not in fruits: {'mango' not in fruits}")  # True

# String membership
print(f"'a' in 'banana': {'a' in 'banana'}")  # True

# Dictionary membership (checks keys)
person = {"name": "Alice", "age": 30}
print(f"'name' in person: {'name' in person}")  # True
print(f"'Alice' in person: {'Alice' in person}")  # False (checks keys)

# ========== IDENTITY OPERATORS ==========
"""
Identity Operators:
is : True if same object in memory
is not : True if different objects

Key Points:
- Different from equality (==)
- None comparisons should use 'is'
- Small integers (-5 to 256) may be cached
"""
print("\n=== IDENTITY OPERATORS ===")

# List identity vs equality
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is list3: {list1 is list3}")  # True (same object)

# None comparisons
value = None
print(f"value is None: {value is None}")  # Preferred way

# Integer caching (implementation detail)
a = 256
b = 256
print(f"256 is 256: {a is b}")  # True (cached)

c = 257
d = 257
print(f"257 is 257: {c is d}")  # False (not cached)

# ========== OPERATOR PRECEDENCE ==========
"""
Operator Precedence Rules:
1. Parentheses () - highest precedence
2. Exponentiation **
3. *, /, //, %
4. +, -
5. Comparison operators
6. Logical not
7. Logical and
8. Logical or
"""
print("\n=== OPERATOR PRECEDENCE ===")

# Example calculation
result = 3 + 5 * 2**3 / 4 - 1
# Evaluation order:
# 1. 2 ** 3 = 8
# 2. 5 * 8 = 40
# 3. 40 / 4 = 10.0
# 4. 3 + 10.0 = 13.0
# 5. 13.0 - 1 = 12.0
print(f"3 + 5 * 2 ** 3 / 4 - 1 = {result}")

# Controlling precedence with parentheses
result = (3 + 5) * (2 ** (3 / 4) - 1)
print(f"(3 + 5) * (2 ** (3 / 4) - 1) = {result:.2f}")

# Logical operator precedence
print("\nLogical operator precedence:")
print(
    "True or False and False:", True or False and False
)  # Equivalent to True or (False and False)
print("(True or False) and False:", (True or False) and False)

# ========== REAL-WORLD EXAMPLES ==========
print("\n=== REAL-WORLD USAGE ===")

# Membership in conditionals
username = "admin"
valid_users = ["admin", "root", "user1"]
if username in valid_users:
    print(f"{username} has access")

# Chained comparisons for range checking
temperature = 22
if 20 <= temperature <= 25:
    print("Comfortable temperature")

# Augmented assignment in loops
total = 0
for i in range(1, 6):
    total += i
print(f"Sum of 1-5: {total}")


# Identity check for sentinel values
def process(data=None):
    if data is None:
        data = []
    data.append("processed")
    return data


print("Process result:", process())
