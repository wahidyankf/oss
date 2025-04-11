# Python Fundamentals: Syntax, Semantics & Environment

## Overview

This project demonstrates core Python language features including dynamic typing, indentation-based blocks, naming conventions, and basic syntax elements. Understanding these fundamentals is crucial for writing correct and idiomatic Python code.

## Key Concepts Demonstrated

### 1. Dynamic Typing

- **Purpose**: Show Python's runtime type system
- **Example**:
  ```python
  a = 5          # Integer
  a = "hello"    # String (type changed)
  a = [1, 2, 3]  # List (type changed again)
  ```
- **Implications**:
  - Flexible but requires careful type management
  - Type hints recommended for larger projects

### 2. Indentation-Based Blocks

- **Purpose**: Demonstrate Python's unique scoping
- **Example**:
  ```python
  def greet(name):
      if name:          # Indented block starts
          print(name)   # Further indentation
      else:
          print("stranger")
  ```
- **Key Points**:
  - 4 spaces per level (PEP 8 standard)
  - Indentation is syntactically significant

### 3. Naming Conventions (PEP 8)

- **Standards**:
  ```python
  snake_case = "variables and functions"  # Lowercase with underscores
  UPPER_SNAKE_CASE = "CONSTANTS"          # All caps with underscores
  PascalCase = "Classes"                  # Capitalized words
  ```

### 4. Basic Syntax Elements

- **Features**:
  - Comments: `# Single-line` and `"""Multi-line"""`
  - f-Strings: `f"Value: {variable}"` (Python 3.6+)
  - List Comprehensions: `[x*2 for x in range(5)]`
  - Operator Precedence: `5 + 3 * 2` = 11

## How to Run

1. Ensure Python 3.6+ is installed
2. Execute:
   ```bash
   python main.py
   ```
3. Output demonstrates:
   - Dynamic type changes
   - Proper indentation usage
   - PEP 8 naming examples
   - Core syntax features

## Implementation Details

The demo script (`main.py`) contains:

1. Complete examples of each concept
2. Well-commented code explanations
3. Practical demonstrations
4. Type hints where appropriate

For deeper understanding, examine:

- The dynamic type changes
- Indentation levels in control structures
- PEP 8 naming patterns
- Modern Python syntax features

## Best Practices

1. **Consistent Indentation**: Use 4 spaces (never tabs)
2. **Follow PEP 8**: Makes code more maintainable
3. **Type Hints**: Add `# type: ignore` only when necessary
4. **Docstrings**: Document functions/modules properly
5. **Modern Features**: Prefer f-strings over older formatting
