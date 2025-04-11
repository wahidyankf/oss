"""
Python Functions Comprehensive Demo

This heavily commented example demonstrates:
1. All Python function features
2. Practical examples with clear output
3. Parameter passing techniques
4. Scope and lifetime rules
5. Advanced function concepts

Key Concepts Covered:
- Function definition and invocation
- Parameter passing (positional, keyword, default)
- Variable-length arguments (*args, **kwargs)
- Return values and multiple returns
- Scope rules (LEGB)
- Lambda functions
- Decorators
- Type hints
"""

# ========== BASIC FUNCTION DEFINITION ==========
"""
Basic Function Components:
1. def keyword
2. Function name
3. Parameters (optional)
4. Docstring (optional but recommended)
5. Function body
6. return statement (optional)
"""
print("\n=== BASIC FUNCTION ===")


def greet(name):
    """
    Returns a greeting message.

    Args:
        name: The name to greet

    Returns:
        A formatted greeting string
    """
    return f"Hello, {name}!"


print(greet("Alice"))  # Function call

# ========== PARAMETER PASSING ==========
"""
Parameter Passing Methods:
1. Positional arguments (order matters)
2. Keyword arguments (order doesn't matter)
3. Default parameters (fallback values)
"""
print("\n=== PARAMETER PASSING ===")


def describe_pet(pet_name, animal_type="dog"):
    """
    Describes a pet with flexible parameter passing.

    Args:
        pet_name: The pet's name (positional)
        animal_type: Type of animal (keyword with default)
    """
    return f"I have a {animal_type} named {pet_name}."


# Different calling conventions
print(describe_pet("Fido"))  # Default animal_type
print(describe_pet("Whiskers", "cat"))  # Positional
print(describe_pet(animal_type="hamster", pet_name="Harry"))  # Keyword

# ========== VARIABLE-LENGTH ARGUMENTS ==========
"""
Variable Arguments:
- *args: Captures extra positional arguments as tuple
- **kwargs: Captures extra keyword arguments as dict
"""
print("\n=== VARIABLE ARGUMENTS ===")


def make_pizza(size, *toppings, **details):
    """
    Demonstrates flexible argument handling.

    Args:
        size: Pizza size (required)
        *toppings: Variable toppings
        **details: Additional order details
    """
    print(f"\nMaking a {size} pizza:")
    print("Toppings:", ", ".join(toppings))
    print("Details:", ", ".join(f"{k}:{v}" for k, v in details.items()))


make_pizza("large", "mushrooms", "olives", delivery="True", time="30min")

# ========== RETURN VALUES ==========
"""
Return Values:
- Can return any object type
- Multiple values returned as a tuple
- None returned if no return statement
"""
print("\n=== RETURN VALUES ===")


def get_formatted_name(first, last, middle=""):
    """Returns a formatted full name."""
    return f"{first} {middle} {last}".strip() if middle else f"{first} {last}"


print(get_formatted_name("John", "Doe"))
print(get_formatted_name("John", "Doe", "Middle"))

# ========== SCOPE RULES ==========
"""
Scope Hierarchy (LEGB):
1. Local
2. Enclosing
3. Global
4. Built-in
"""
print("\n=== SCOPE RULES ===")

global_var = "global"


def scope_demo():
    """Demonstrates Python's scope rules."""
    enclosing_var = "enclosing"

    def inner_func():
        local_var = "local"
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_var}")
        print(f"Built-in: {len([1,2,3])}")

    inner_func()


scope_demo()

# ========== LAMBDA FUNCTIONS ==========
"""
Lambda Functions:
- Anonymous single-expression functions
- Often used for short operations
- Common with map(), filter(), sorted()
"""
print("\n=== LAMBDA FUNCTIONS ===")

double = lambda x: x * 2
print("Double of 5:", double(5))

# Sorting with lambda
names = [("Alice", "Smith"), ("Bob", "Johnson"), ("Charlie", "Brown")]
sorted_names = sorted(names, key=lambda name: name[1])  # Sort by last name
print("Sorted by last name:", sorted_names)

# ========== DECORATORS ==========
"""
Decorators:
- Functions that modify other functions
- Use @ syntax for application
"""
print("\n=== DECORATORS ===")


def timer(func):
    """Decorator that times function execution."""
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end-start:.4f}s")
        return result

    return wrapper


@timer
def calculate_sum(n):
    """Calculates sum of first n numbers."""
    return sum(range(n + 1))


print("Sum:", calculate_sum(1000000))
