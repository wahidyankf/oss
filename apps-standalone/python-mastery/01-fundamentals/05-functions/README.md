# Python Functions Comprehensive Guide

## Overview

Functions are fundamental building blocks in Python, allowing code reuse, organization, and abstraction. This module explores various facets of Python functions through practical examples, covering both fundamental aspects and advanced features.

## Key Concepts Covered

### 1. Basic Function Definition & Invocation

- The core structure using `def` keyword
- Function naming conventions
- Parameters and arguments
- Docstring conventions (PEP 257)
- Return values (single and multiple)

### 2. Parameter Passing Techniques

- **Positional Arguments**: Passed in order defined
- **Keyword Arguments**: Passed using `name=value` syntax
- **Default Parameter Values**: Making arguments optional
- **Variable-Length Arguments**:
  - `*args`: Extra positional arguments as tuple
  - `**kwargs`: Extra keyword arguments as dictionary

### 3. Scope Rules (LEGB)

- **L**ocal: Inside current function
- **E**nclosing: In nested functions
- **G**lobal: Module level
- **B**uilt-in: Pre-defined names
- `global` and `nonlocal` keywords

### 4. Advanced Features

- **Lambda Functions**: Anonymous single-expression functions
- **Decorators**: Modifying/enhancing functions
- **Type Hints**: Argument and return type annotations
- **Recursion**: Function calling itself

### 5. Function Characteristics

- First-class objects (can be assigned, passed, returned)
- Closures and factory functions
- Generator functions using `yield`

## How to Run

1. Ensure Python 3.5+ is installed (for type hints)
2. Run the demo script:
   ```bash
   python main.py
   ```
3. The script will demonstrate:
   - Function definition and invocation
   - Parameter passing techniques
   - Scope behavior
   - Advanced features

## Learning Objectives

By studying this module, you will:

- Master all function definition styles
- Understand parameter passing techniques
- Learn scope resolution rules
- Apply advanced function features
- Write more modular and reusable code

## Implementation Details

The demo script (`main.py`) contains:

1. Complete examples for each concept
2. Well-commented explanations
3. Practical use cases
4. Type hints for clarity

For deeper understanding, examine:

- Nested function scope
- Decorator implementation
- Lambda usage patterns
- Recursion examples
