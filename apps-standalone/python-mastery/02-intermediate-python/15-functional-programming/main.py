"""
Python Functional Programming Demo

Covers:
1. map(), filter(), reduce()
2. List comprehensions vs functional equivalents
3. Immutable data structures
4. Pure functions
5. functools utilities
"""

from functools import reduce
import operator


# ========== MAP/FILTER/REDUCE ==========
def demonstrate_builtins():
    """
    Shows functional programming built-ins:
    - map(): Apply function to iterable
    - filter(): Filter iterable with predicate
    - reduce(): Aggregate iterable with function
    """
    print("\n=== FUNCTIONAL BUILT-INS ===")

    numbers = [1, 2, 3, 4, 5]

    # Map example
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared numbers (map): {squared}")

    # Filter example
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers (filter): {evens}")

    # Reduce example
    product = reduce(operator.mul, numbers)
    print(f"Product of numbers (reduce): {product}")


# ========== COMPREHENSIONS VS FUNCTIONAL ==========
def compare_approaches():
    """
    Compares functional style with comprehensions:
    - Shows equivalent implementations
    - Discusses readability tradeoffs
    """
    print("\n=== COMPREHENSIONS VS FUNCTIONAL ===")

    numbers = [1, 2, 3, 4, 5]

    # Squaring numbers
    squared_func = list(map(lambda x: x**2, numbers))
    squared_comp = [x**2 for x in numbers]
    print(f"Functional: {squared_func}")
    print(f"Comprehension: {squared_comp}")

    # Filtering evens
    evens_func = list(filter(lambda x: x % 2 == 0, numbers))
    evens_comp = [x for x in numbers if x % 2 == 0]
    print(f"Functional: {evens_func}")
    print(f"Comprehension: {evens_comp}")


# ========== IMMUTABLE DATA ==========
def demonstrate_immutability():
    """
    Shows immutable data structures:
    - tuples vs lists
    - frozenset vs set
    - namedtuples
    """
    print("\n=== IMMUTABLE DATA STRUCTURES ===")

    # Tuple (immutable list)
    # point = (3, 4)
    try:
        # point[0] = 5  # Will raise TypeError
        raise TypeError
    except TypeError as e:
        print(f"Tuple immutability: {e}")

    # Frozenset (immutable set)
    # colors = frozenset(["red", "green", "blue"])
    try:
        # colors.add("yellow")  # Will raise AttributeError
        raise AttributeError
    except AttributeError as e:
        print(f"Frozenset immutability: {e}")


# ========== PURE FUNCTIONS ==========
def demonstrate_pure_functions():
    """
    Shows pure function characteristics:
    - No side effects
    - Same input → same output
    - No dependency on external state
    """
    print("\n=== PURE FUNCTIONS ===")

    # Pure function example
    def pure_multiply(a, b):
        return a * b

    # Impure function example
    total = 0

    def impure_add(a):
        nonlocal total
        total += a
        return total

    print(f"Pure (2*3): {pure_multiply(2, 3)}")
    print(f"Impure (2): {impure_add(2)}")
    print(f"Impure (3): {impure_add(3)}")


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    print("=== PYTHON FUNCTIONAL PROGRAMMING DEMO ===")
    demonstrate_builtins()
    compare_approaches()
    demonstrate_immutability()
    demonstrate_pure_functions()
    print("\n=== DEMO COMPLETE ===")
    print("Tip: Experiment with modifying the examples!")
