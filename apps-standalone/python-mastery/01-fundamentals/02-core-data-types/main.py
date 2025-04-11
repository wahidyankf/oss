"""
Python Core Data Types Comprehensive Demo

This heavily commented example demonstrates:
1. All fundamental Python data types
2. Practical examples with clear output
3. Mutability vs immutability
4. Type conversion and special cases

Key Concepts Covered:
- Numeric types (int, float, complex)
- Sequence types (str, list, tuple, bytes)
- Mapping type (dict)
- Set types (set, frozenset)
- Boolean and None
- Type conversion functions
"""

# ========== NUMERIC TYPES ==========
"""
Python's numeric types:
- int: Arbitrary precision integers (no size limit)
- float: Double-precision floating point (64-bit)
- complex: Complex numbers (real + imaginary parts)

Key Characteristics:
- All are immutable (operations create new objects)
- Support standard arithmetic operations
- Type conversion via int(), float(), complex()
"""
print("\n=== NUMERIC TYPES ===")
integer = 42  # Basic integer
float_num = 3.14  # Floating point number
complex_num = 2 + 3j  # Complex number (j for imaginary unit)

# Display types and values
print(f"Integer: {integer}, type: {type(integer)}")
print(f"Float: {float_num}, type: {type(float_num)}")
print(f"Complex: {complex_num}, type: {type(complex_num)}")

# ========== SEQUENCE TYPES ==========
"""
Sequence Types:
1. str: Immutable Unicode character sequences
2. list: Mutable ordered collections
3. tuple: Immutable ordered collections
4. bytes: Immutable byte sequences
5. bytearray: Mutable byte sequences

Common Operations:
- Indexing (0-based)
- Slicing [start:stop:step]
- Concatenation (+)
- Repetition (*)
- Membership testing (in)
"""
print("\n=== SEQUENCE TYPES ===")

# ----- Strings -----
"""
Strings:
- Immutable sequence of Unicode characters
- Support extensive methods for manipulation
- Single or double quotes (consistent in file)
"""
message = "Hello Python"
print(f"String: {message}, type: {type(message)}")
print(f"Split: {message.split()}")  # Split into words (list)
print(f"Slice: {message[0:5]}")  # Get first 5 characters

# ----- Lists -----
"""
Lists:
- Mutable ordered collections
- Heterogeneous (can mix types)
- Grow/shrink dynamically
"""
colors = ["red", "green", "blue"]
print(f"\nList: {colors}, type: {type(colors)}")
colors.append("yellow")  # Modifies in-place
print(f"After append: {colors}")
print(f"Slice: {colors[1:]}")  # All elements after first

# ----- Tuples -----
"""
Tuples:
- Immutable ordered collections
- Faster than lists
- Often used for fixed data
"""
dimensions = (1920, 1080)
print(f"\nTuple: {dimensions}, type: {type(dimensions)}")
# dimensions[0] = 2560  # Would raise TypeError (immutable)

# ========== MAPPING TYPE (DICT) ==========
"""
Dictionaries:
- Mutable key-value mappings
- Keys must be hashable (immutable types)
- Unordered until Python 3.7+, insertion-ordered after
"""
print("\n=== MAPPING TYPE ===")
user = {"name": "Alice", "age": 30, "is_admin": False}
print(f"Dict: {user}, type: {type(user)}")
print(f"Name: {user['name']}")  # Access by key
user["email"] = "alice@example.com"  # Add new key-value pair
print(f"After update: {user}")

# ========== SET TYPES ==========
"""
Set Types:
- set: Mutable unordered collections of unique elements
- frozenset: Immutable version of set
- Elements must be hashable (immutable types)
"""
print("\n=== SET TYPES ===")
primes = {2, 3, 5, 7, 11}
print(f"Set: {primes}, type: {type(primes)}")
primes.add(13)  # Modifies in-place
print(f"After add: {primes}")
print(f"Is 7 prime? {7 in primes}")  # Fast membership test

# ========== BOOLEAN & NONE ==========
"""
Boolean and None:
- Boolean: True or False
- None: Special value for absence of value
"""
print("\n=== BOOLEAN & NONE ===")
is_valid = True
no_value = None
print(f"None: {no_value}, type: {type(no_value)}")

# ========== TYPE CONVERSION ==========
"""
Type Conversion:
- Explicit conversion between types
- Common functions: int(), float(), str(), list(), etc.
- Some conversions may lose information
"""
print("\n=== TYPE CONVERSION ===")
num_str = "123"
print(f"String to int: {int(num_str)}, type: {type(int(num_str))}")
print(f"Int to float: {float(integer)}, type: {type(float(integer))}")
print(f"List to tuple: {tuple(colors)}, type: {type(tuple(colors))}")
