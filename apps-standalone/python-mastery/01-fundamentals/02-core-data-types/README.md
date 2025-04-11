# Python Core Data Types - Comprehensive Guide

## Overview

This project demonstrates Python's fundamental built-in data types through practical examples, covering their properties, operations, and key characteristics like mutability.

## Data Types Covered

### 1. Numeric Types

- **int**: Arbitrary-precision integers
  ```python
  x = 10  # Positive integer
  y = -5  # Negative integer
  ```
- **float**: Double-precision floating point
  ```python
  pi = 3.14159
  ```
- **complex**: Numbers with real/imaginary parts
  ```python
  z = 3 + 4j
  ```

### 2. Sequence Types

- **str**: Immutable Unicode strings
  ```python
  name = "Python"
  ```
- **list**: Mutable ordered sequences
  ```python
  colors = ['red', 'green', 'blue']
  ```
- **tuple**: Immutable ordered sequences
  ```python
  coordinates = (10.0, 20.5)
  ```

### 3. Mapping Type

- **dict**: Key-value mappings
  ```python
  person = {'name': 'Alice', 'age': 30}
  ```

### 4. Set Types

- **set**: Mutable unordered unique collections
  ```python
  unique_numbers = {1, 2, 3}
  ```

### 5. Boolean Type

- **bool**: Truth values (True/False)
  ```python
  is_valid = True
  ```

### 6. None Type

- **NoneType**: Absence of value
  ```python
  result = None
  ```

## Key Concepts

- **Mutability**:
  - Mutable: list, dict, set
  - Immutable: int, float, str, tuple
- **Common Operations**:
  - Sequence indexing/slicing
  - Dictionary key access
  - Set membership testing
- **Type Conversion**:
  ```python
  str(42)    # '42'
  int('10')  # 10
  ```

## How to Run

1. Navigate to the project directory
2. Execute:
   ```bash
   python main.py
   ```
3. Output demonstrates:
   - All core data types
   - Common operations
   - Mutability examples
   - Type conversions

## Implementation Details

The demo script (`main.py`) contains:

1. Comprehensive examples for each type
2. Well-commented code explanations
3. Practical demonstrations
4. Memory usage comparisons

For deeper understanding, examine:

- Mutability demonstrations
- Type conversion examples
- Sequence operations
- Dictionary/set use cases

## Best Practices

1. **Choose Appropriate Types**:
   - Lists for ordered, mutable sequences
   - Tuples for fixed data structures
   - Sets for unique element collections
2. **Leverage Immutability**:
   - Use tuples for constant data
   - Strings are always immutable
3. **Dictionary Keys**: Must be hashable (immutable)
4. **Type Hints**: Helps document expected types
5. **Conversion Functions**: Use `int()`, `str()` etc. explicitly
