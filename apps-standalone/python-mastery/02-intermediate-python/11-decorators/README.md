# Python Decorator Patterns - Comprehensive Guide

## Overview

Decorators are a powerful and expressive feature in Python used to modify or enhance functions or methods in a clean and readable way. This project demonstrates four key decorator patterns through practical examples.

## Patterns Demonstrated

### 1. Basic Function Decorator (`simple_decorator`)

- **Purpose**: Adds behavior before and after function execution
- **Example Use Case**: Logging function calls, timing execution
- **Key Features**:
  ```python
  @wraps(func)  # Preserves function metadata
  def wrapper(*args, **kwargs):
      # Pre-call logic (logging/timing)
      result = func(*args, **kwargs)
      # Post-call logic
      return result
  ```

### 2. Decorator with Arguments (`repeat`)

- **Purpose**: Creates configurable decorators
- **Example Use Case**: Repeating function execution
- **Implementation**:
  ```python
  @repeat(num_times=3)
  def greet(name):
      print(f"Hello {name}!")
  ```

### 3. Class-Based Decorator (`CacheDecorator`)

- **Purpose**: Maintains state across calls
- **Example Use Case**: Memoization/caching
- **Key Features**:

  ```python
  class CacheDecorator:
      def __init__(self, func):
          self.cache = {}  # State maintained

      def __call__(self, *args):
          if args in self.cache:
              return self.cache[args]  # Cache hit
  ```

### 4. Validation Decorator (`validate_input`)

- **Purpose**: Runtime argument validation
- **Example Use Case**: Ensuring positive inputs
- **Implementation**:
  ```python
  @validate_input(is_positive, is_positive)
  def rectangle_area(length, width):
      return length * width
  ```

## Key Concepts

- **`@` Syntax**: Clean application of decorators
- **`functools.wraps`**: Preserves function metadata
- **Decorator Factories**: Functions that return decorators
- **Stateful Decorators**: Using classes to maintain state
- **Argument Handling**: Works with `*args` and `**kwargs`

## How to Run

1. Navigate to the project directory
2. Execute:
   ```bash
   python main.py
   ```
3. Expected output includes:
   - Timed function execution
   - Repeated greetings
   - Cache hits for Fibonacci
   - Validation errors for negative inputs

## Implementation Details

The demo script (`main.py`) contains:

1. Complete implementations of all decorators
2. Well-commented code explaining each pattern
3. Practical examples demonstrating real-world usage
4. Interactive demo when run directly

For deeper understanding, examine:

- The decorator definitions
- How each preserves function metadata
- The call patterns in the demo section
