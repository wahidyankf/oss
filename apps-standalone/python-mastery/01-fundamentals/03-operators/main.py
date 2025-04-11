"""
Python Operators Comprehensive Demo

This heavily commented example demonstrates:
1. All Python operator categories with explanations
2. Practical examples with clear output
3. Special cases and edge behaviors
4. Operator precedence rules

Key Concepts Covered:
- Arithmetic operations and numeric behaviors
- Comparison and logical operator chaining
- Assignment operator variations
- Membership and identity testing
"""

# ========== ARITHMETIC OPERATORS ==========
"""
Basic math operations:
+ : Addition
- : Subtraction
* : Multiplication
/ : True division (always returns float)
// : Floor division (returns integer)
% : Modulus (remainder)
** : Exponentiation
"""
print("=== ARITHMETIC OPERATORS ===")
a, b = 10, 3  # Initialize test values
print(f"{a} + {b} = {a + b}")  # 13
print(f"{a} - {b} = {a - b}")  # 7
print(f"{a} * {b} = {a * b}")  # 30
print(f"{a} / {b} = {a / b:.2f}")  # 3.33 (float division)
print(f"{a} // {b} = {a // b}")  # 3 (integer division)
print(f"{a} % {b} = {a % b}")  # 1 (remainder)
print(f"{a} ** {b} = {a ** b}")  # 1000 (10 cubed)

# ========== COMPARISON OPERATORS ==========
"""
Comparison operators return booleans:
== : Equal to
!= : Not equal to
> : Greater than
< : Less than
>= : Greater than or equal
<= : Less than or equal

Note: Chained comparisons like 1 < x < 10 are valid
"""
print("\n=== COMPARISON OPERATORS ===")
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} > {b}: {a > b}")  # True
print(f"{a} < {b}: {a < b}")  # False
print(f"{a} >= {b}: {a >= b}")  # True
print(f"{a} <= {b}: {a <= b}")  # False

# ========== LOGICAL OPERATORS ==========
"""
Logical operators work with booleans:
and : Both must be True
or : Either must be True
not : Inverts the boolean

Short-circuit evaluation:
- and stops at first False
- or stops at first True
"""
print("\n=== LOGICAL OPERATORS ===")
x, y = True, False
print(f"{x} and {y}: {x and y}")  # False
print(f"{x} or {y}: {x or y}")  # True
print(f"not {x}: {not x}")  # False

# ========== ASSIGNMENT OPERATORS ==========
"""
Shorthand assignment operators:
+= : Add and assign
-= : Subtract and assign
*= : Multiply and assign
/= : Divide and assign
//= : Floor divide and assign
%= : Modulus and assign
**= : Exponent and assign
"""
print("\n=== ASSIGNMENT OPERATORS ===")
num = 5
num += 3  # Equivalent to num = num + 3
print(f"After += 3: {num}")
num **= 2  # Square the number
print(f"After **= 2: {num}")

# ========== MEMBERSHIP OPERATORS ==========
"""
Membership operators:
in : True if value exists in sequence
not in : True if value doesn't exist

Works with strings, lists, tuples, dicts, etc.
"""
print("\n=== MEMBERSHIP OPERATORS ===")
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")  # True
print(f"'mango' not in fruits: {'mango' not in fruits}")  # True

# ========== IDENTITY OPERATORS ==========
"""
Identity operators:
is : True if same object (memory address)
is not : True if different objects

Different from == which checks equality
"""
print("\n=== IDENTITY OPERATORS ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)

# ========== OPERATOR PRECEDENCE ==========
"""
Operator precedence determines evaluation order:
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
result = 5 + 3 * 2**2  # Evaluates as 5 + (3 * (2**2)) = 17
print(f"5 + 3 * 2 ** 2 = {result}")
