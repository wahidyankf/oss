"""
Python Operators Demo

Key concepts demonstrated:
1. Arithmetic operators
2. Comparison operators
3. Logical operators
4. Assignment operators
5. Membership operators
6. Identity operators
7. Operator precedence
"""

# 1. Arithmetic Operators
print("=== ARITHMETIC OPERATORS ===")
a, b = 10, 3
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # True division
print(f"{a} // {b} = {a // b}")  # Floor division
print(f"{a} % {b} = {a % b}")  # Modulus
print(f"{a} ** {b} = {a ** b}")  # Exponentiation

# 2. Comparison Operators
print("\n=== COMPARISON OPERATORS ===")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# 3. Logical Operators
print("\n=== LOGICAL OPERATORS ===")
x, y = True, False
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# 4. Assignment Operators
print("\n=== ASSIGNMENT OPERATORS ===")
c = 5
print(f"Original c: {c}")
c += 2  # c = c + 2
print(f"After += 2: {c}")
c *= 3  # c = c * 3
print(f"After *= 3: {c}")

# 5. Membership Operators
print("\n=== MEMBERSHIP OPERATORS ===")
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in {fruits}: {"banana" in fruits}")
print(f"'mango' not in {fruits}: {"mango" not in fruits}")

# 6. Identity Operators
print("\n=== IDENTITY OPERATORS ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is list3: {list1 is list3}")  # True (same object)

# 7. Operator Precedence
print("\n=== OPERATOR PRECEDENCE ===")
result = 10 + 3 * 2**2
print(f"10 + 3 * 2 ** 2 = {result}")  # 22 not 52
print("Order: Exponentiation > Multiplication > Addition")
