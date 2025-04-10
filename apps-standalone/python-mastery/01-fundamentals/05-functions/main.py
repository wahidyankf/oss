"""
Python Functions Demo

Key concepts demonstrated:
1. Basic function definition
2. Parameter passing methods
3. Return values
4. Scope rules (LEGB)
5. Lambda functions
6. Docstrings
"""


# 1. Basic Function Definition
def greet(name):
    """Simple greeting function with docstring"""
    return f"Hello, {name}!"


print("=== BASIC FUNCTION ===")
print(greet("Alice"))


# 2. Parameter Passing Methods
def describe_pet(pet_name, animal_type="dog"):
    """
    Demonstrates:
    - Positional arguments
    - Keyword arguments
    - Default parameters
    """
    return f"I have a {animal_type} named {pet_name}."


print("\n=== PARAMETER PASSING ===")
print(describe_pet("Fido"))  # Default animal_type
print(describe_pet("Whiskers", "cat"))  # Positional
print(describe_pet(animal_type="hamster", pet_name="Harry"))  # Keyword


# 3. Variable-length Arguments
def make_pizza(size, *toppings, **details):
    """Demonstrates *args and **kwargs"""
    print(f"\nMaking a {size} pizza:")
    print("Toppings:", toppings)
    print("Details:", details)


print("\n=== VARIABLE ARGUMENTS ===")
make_pizza("large", "mushrooms", "olives", delivery=True, time="30min")


# 4. Return Values
def get_formatted_name(first, last, middle=""):
    """Return a neatly formatted full name."""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"


print("\n=== RETURN VALUES ===")
print(get_formatted_name("John", "Doe"))
print(get_formatted_name("John", "Doe", "Middle"))

# 5. Scope Rules (LEGB)
print("\n=== SCOPE RULES ===")
global_var = "global"


def scope_demo():
    enclosing_var = "enclosing"

    def inner_func():
        local_var = "local"
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_var}")
        print(f"Built-in: {len([1,2,3])}")  # len is built-in

    inner_func()


scope_demo()

# 6. Lambda Functions
print("\n=== LAMBDA FUNCTIONS ===")
double = lambda x: x * 2
print("Double of 5:", double(5))

# Sorting with lambda
names = [("Alice", "Smith"), ("Bob", "Johnson"), ("Charlie", "Brown")]
sorted_names = sorted(names, key=lambda name: name[1])  # Sort by last name
print("Sorted by last name:", sorted_names)
