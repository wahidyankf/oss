"""
Python Core Data Types & Operations Demo

Covers:
1. Numeric types (int, float, complex)
2. Sequence types (str, list, tuple)
3. Mapping type (dict)
4. Set type
5. Boolean and None
6. Common operations and methods
7. Mutability vs Immutability
8. String formatting (f-strings)
"""

# 1. Numeric Types
print("\n=== NUMERIC TYPES ===")
integer = 42
float_num = 3.14
complex_num = 2 + 3j
print(f"Integer: {integer}, type: {type(integer)}")
print(f"Float: {float_num}, type: {type(float_num)}")
print(f"Complex: {complex_num}, type: {type(complex_num)}")

# 2. Sequence Types
print("\n=== SEQUENCE TYPES ===")
# Strings
message = "Hello Python"
print(f"String: {message}, type: {type(message)}")
print(f"Split: {message.split()}")  # Common string method
print(f"Slice: {message[0:5]}")  # Slicing

# Lists (mutable)
colors = ["red", "green", "blue"]
print(f"\nList: {colors}, type: {type(colors)}")
colors.append("yellow")  # Modifies list in-place
print(f"After append: {colors}")
print(f"Slice: {colors[1:]}")

# Tuples (immutable)
dimensions = (1920, 1080)
print(f"\nTuple: {dimensions}, type: {type(dimensions)}")
# dimensions[0] = 2560  # Would raise TypeError

# 3. Mapping Type (dict)
print("\n=== MAPPING TYPE ===")
user = {"name": "Alice", "age": 30, "is_admin": False}
print(f"Dict: {user}, type: {type(user)}")
print(f"Get name: {user.get('name')}")  # Safe access
user["email"] = "alice@example.com"  # Add new key
print(f"After update: {user}")

# 4. Set Type
print("\n=== SET TYPE ===")
primes = {2, 3, 5, 7, 11}
print(f"Set: {primes}, type: {type(primes)}")
primes.add(13)  # Add element
print(f"After add: {primes}")
print(f"Is 7 prime? {7 in primes}")  # Fast membership test

# 5. Boolean and None
print("\n=== BOOLEAN & NONE ===")
is_valid = True
no_value = None
print(f"Boolean: {is_valid}, type: {type(is_valid)}")
print(f"None: {no_value}, type: {type(no_value)}")

# 6. Mutability Examples
print("\n=== MUTABILITY ===")
# Lists are mutable
numbers = [1, 2, 3]
numbers[0] = 10
print(f"Mutable list: {numbers}")

# Strings are immutable
# message[0] = 'h'  # Would raise TypeError

# 7. String Formatting (f-strings)
print("\n=== STRING FORMATTING ===")
name = "Bob"
score = 95.5
print(f"{name} scored {score:.1f}% on the test")

# Run with: python3 data_types_demo.py
