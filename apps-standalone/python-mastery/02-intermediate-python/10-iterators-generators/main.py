"""
Comprehensive Iterators & Generators Demo

This module demonstrates:
1. Custom iterator implementation
2. Generator functions
3. Generator expressions
4. itertools module examples
5. Memory efficiency comparisons
"""

import itertools
import sys

# ========== CUSTOM ITERATOR CLASS ==========
"""
Custom Countdown Iterator:
- Implements __iter__ and __next__
- Raises StopIteration when done
- Manages its own state
"""


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value


# ========== GENERATOR FUNCTIONS ==========
"""
Generator Functions:
- Use yield instead of return
- Maintain state between calls
- Automatically implement iterator protocol
"""


def fibonacci_generator(limit):
    """Generates Fibonacci sequence up to limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def countdown_generator(start):
    """Generator version of countdown."""
    while start > 0:
        yield start
        start -= 1


# ========== GENERATOR EXPRESSIONS ==========
"""
Generator Expressions:
- Similar to list comprehensions but lazy
- Memory efficient for large sequences
"""


def demonstrate_generator_expressions():
    """Shows generator expression vs list comprehension."""
    # List comprehension (eager evaluation)
    squares_list = [x**2 for x in range(10000)]

    # Generator expression (lazy evaluation)
    squares_gen = (x**2 for x in range(10000))

    print(f"List memory: {sys.getsizeof(squares_list)} bytes")
    print(f"Generator memory: {sys.getsizeof(squares_gen)} bytes")


# ========== ITERTOOLS EXAMPLES ==========
"""
itertools Module:
- Tools for creating and combining iterators
- Memory efficient operations
"""


def demonstrate_itertools():
    """Shows common itertools functions."""
    # 1. Infinite iterators
    print("\n=== INFINITE ITERATORS ===")
    counter = itertools.count(start=5, step=2)  # 5, 7, 9, ...
    cycler = itertools.cycle("ABC")  # A, B, C, A, B, C, ...
    repeater = itertools.repeat(10, times=3)  # 10, 10, 10

    print(f"Count sample: {next(counter)}, {next(counter)}")
    print(f"Cycle sample: {next(cycler)}, {next(cycler)}")
    print(f"Repeat sample: {list(repeater)}")

    # 2. Combinatoric iterators
    print("\n=== COMBINATORICS ===")
    print("Combinations (order doesn't matter):")
    print(list(itertools.combinations("ABCD", 2)))  # AB, AC, AD, BC, BD, CD

    print("\nPermutations (order matters):")
    print(list(itertools.permutations("ABC", 2)))  # AB, AC, BA, BC, CA, CB

    print("\nCartesian product:")
    print(list(itertools.product("AB", "12")))  # A1, A2, B1, B2

    # 3. Chaining and filtering
    print("\n=== CHAINING/FILTERING ===")
    print("Chained iterators:")
    print(list(itertools.chain("ABC", "DEF")))  # A, B, C, D, E, F

    print("\nCompressed data (filter with boolean mask):")
    print(list(itertools.compress("ABCDEF", [1, 0, 1, 0, 1, 1])))  # A, C, E, F

    # 4. Grouping and windowing
    print("\n=== GROUPING ===")
    data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("C", 5)]
    for key, group in itertools.groupby(data, lambda x: x[0]):
        print(f"{key}: {list(group)}")

    print("\nSliding window (3 items at a time):")
    print(list(itertools.islice(itertools.count(), 5)))  # First 5 numbers
    print(list(itertools.pairwise("ABCDE")))  # AB, BC, CD, DE


# ========== MAIN DEMO ==========
if __name__ == "__main__":
    print("=== CUSTOM ITERATOR ===")
    for num in Countdown(5):
        print(f"Countdown: {num}")

    print("\n=== FIBONACCI GENERATOR ===")
    fib = fibonacci_generator(100)
    print(f"First 5 Fibonacci numbers: {[next(fib) for _ in range(5)]}")

    print("\n=== GENERATOR EXPRESSIONS ===")
    demonstrate_generator_expressions()

    demonstrate_itertools()
