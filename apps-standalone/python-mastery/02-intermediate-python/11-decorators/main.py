"""
Python Decorators Comprehensive Demo

This script demonstrates four key decorator patterns:
1. Basic function decorator (logging/timing)
2. Decorator with arguments (repeat functionality)
3. Class-based decorator (memoization/caching)
4. Practical validation decorator

Each section includes:
- Implementation of the decorator
- Example usage
- Explanation of key concepts
"""

import time
from functools import wraps
from datetime import datetime

# ========== BASIC DECORATORS ==========


def simple_decorator(func):
    """
    Basic decorator that adds timing and logging to functions

    Key features:
    - Wraps the original function to preserve metadata
    - Adds pre-call and post-call behavior
    - Measures and reports execution time
    """

    @wraps(func)  # Critical: preserves original function's __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        # Pre-function call: log the invocation
        print(f"Calling {func.__name__} at {datetime.now()}")

        # Time the function execution
        start = time.perf_counter()
        result = func(*args, **kwargs)  # Call the original function
        end = time.perf_counter()

        # Post-function call: report timing
        print(f"{func.__name__} executed in {end-start:.4f}s")
        return result

    return wrapper


@simple_decorator
def calculate_sum(n):
    """Calculate sum of first n natural numbers"""
    return sum(range(n + 1))


# ========== DECORATORS WITH ARGUMENTS ==========


def repeat(num_times):
    """
    Decorator factory that takes arguments

    This demonstrates how to create decorators that accept
    their own configuration parameters.
    The outer function (repeat) takes decorator arguments,
    the middle (decorator) takes the function to decorate,
    and the inner (wrapper) does the actual wrapping.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Execute the function multiple times
            # Note: only returns the last result
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(num_times=3)
def greet(name):
    """Greet someone (demonstrates repeated execution)"""
    print(f"Hello {name}!")


# ========== CLASS DECORATORS ==========


class CacheDecorator:
    """
    Memoization decorator implemented as a class

    Shows how to:
    - Use classes as decorators
    - Implement method call interception
    - Maintain state between calls (cache)
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}
        wraps(func)(self)  # Preserve original metadata

    def __call__(self, *args):
        """Called when the decorated function is invoked"""
        if args in self.cache:
            print(f"Cache hit for {args}")
            return self.cache[args]

        # Compute and cache if not found
        result = self.func(*args)
        self.cache[args] = result
        return result


@CacheDecorator
def fibonacci(n):
    """Calculate nth Fibonacci number (demonstrates caching)"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ========== REAL-WORLD EXAMPLES ==========


def validate_input(*validators):
    """
    Decorator factory for input validation

    Takes validation functions as arguments and applies them
    to the decorated function's inputs.
    Shows practical use of:
    - Decorator factories
    - Runtime argument validation
    - Flexible parameter checking
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check each argument against its validator
            for i, (arg, validator) in enumerate(zip(args, validators)):
                if not validator(arg):
                    raise ValueError(f"Invalid argument at position {i}: {arg}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def is_positive(x):
    """Simple validator: checks if number is positive"""
    return x > 0


@validate_input(is_positive, is_positive)
def rectangle_area(length, width):
    """Calculate area of rectangle (requires positive dimensions)"""
    return length * width


# ========== MAIN DEMO ==========

if __name__ == "__main__":
    print("=== BASIC DECORATOR ===")
    print(f"Sum result: {calculate_sum(1000)}")

    print("\n=== DECORATOR WITH ARGUMENTS ===")
    greet("Alice")

    print("\n=== CLASS DECORATOR (CACHING) ===")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Fibonacci(10) again: {fibonacci(10)}")  # Cache hit

    print("\n=== VALIDATION DECORATOR ===")
    try:
        print(f"Area: {rectangle_area(5, 3)}")
        print(f"Area: {rectangle_area(-1, 3)}")  # Should raise
    except ValueError as e:
        print(f"Validation error: {e}")
