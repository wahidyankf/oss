# Python Iterators and Generators - Comprehensive Guide

## Overview

Understanding iteration is fundamental to writing efficient and Pythonic code. This project demonstrates Python's iteration patterns including custom iterators, generators, and the powerful `itertools` module.

## Concepts Demonstrated

### 1. Custom Iterators (`Countdown` class)

- **Purpose**: Manually implement the iterator protocol
- **Key Features**:

  ```python
  class Countdown:
      def __iter__(self):
          self.current = self.start
          return self

      def __next__(self):
          if self.current <= 0:
              raise StopIteration
          value = self.current
          self.current -= 1
          return value
  ```

### 2. Generator Functions

- **Purpose**: Create iterators using `yield`
- **Example**:
  ```python
  def fibonacci_generator():
      a, b = 0, 1
      while True:
          yield a
          a, b = b, a + b
  ```

### 3. Generator Expressions

- **Purpose**: Memory-efficient alternative to list comprehensions
- **Example**:
  ```python
  gen_expr = (x**2 for x in range(1000000))  # Doesn't store in memory
  ```

### 4. `itertools` Module

- **Purpose**: Pre-built efficient iteration tools
- **Examples**:

  ```python
  from itertools import count, cycle, combinations

  # Infinite counting
  counter = count(start=10, step=2)

  # All possible pairs
  pairs = combinations(['a', 'b', 'c'], 2)
  ```

### 5. Memory Efficiency

- **Demonstration**:

  ```python
  import sys

  list_comp = [x**2 for x in range(1000)]
  gen_expr = (x**2 for x in range(1000))

  print(f"List size: {sys.getsizeof(list_comp)} bytes")
  print(f"Generator size: {sys.getsizeof(gen_expr)} bytes")
  ```

## Key Concepts

- **Iterator Protocol**: `__iter__()` and `__next__()` methods
- **Lazy Evaluation**: Values generated on-demand
- **State Management**: Position tracking in sequences
- `StopIteration`: Signals end of iteration
- **Memory Efficiency**: Generators vs lists
- **Composable Iterators**: Building complex iteration logic

## How to Run

1. Navigate to the project directory
2. Execute:
   ```bash
   python main.py
   ```
3. Output includes:
   - Custom iterator countdown
   - Generated Fibonacci sequence
   - Memory size comparisons
   - `itertools` demonstrations

## Implementation Details

The demo script (`main.py`) contains:

1. Complete iterator protocol implementation
2. Generator function examples
3. Memory efficiency comparisons
4. Practical `itertools` usage
5. Well-commented code explanations

For deeper understanding, examine:

- The `__iter__` and `__next__` methods
- Generator function flow control
- Memory usage measurements
- `itertools` function combinations
