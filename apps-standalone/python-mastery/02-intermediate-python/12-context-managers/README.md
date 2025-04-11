# Python Context Managers - Resource Management

## Overview

This module demonstrates Python's context managers, which provide a clean way to handle resource setup and teardown using the `with` statement.

## Key Concepts

- The `with` statement and protocol
- Implementing context managers with classes
- Using `contextlib.contextmanager` decorator
- Practical resource management patterns

## How to Run

```bash
python main.py
```

# Python Context Managers Masterclass

## Overview

This module (`main.py`) demonstrates the two fundamental ways to implement context managers in Python:

1. **Class-based approach** using `__enter__` and `__exit__` methods
2. **Generator-based approach** using `@contextmanager` decorator from `contextlib`

Context managers are essential for reliable resource management, ensuring proper setup and teardown operations.

## Implementation Methods

### 1. Class-Based Context Manager (`DatabaseConnection`)

**Structure:**

- `__init__`: Initializes context manager state
- `__enter__`: Performs setup and returns resource
- `__exit__`: Handles cleanup and exceptions

**Key Features:**

- Full control over enter/exit logic
- Maintains state between operations
- Explicit exception handling

**Best For:**

- Complex resource management
- Stateful contexts
- Object-oriented resource patterns

### 2. Generator-Based Context Manager (`file_lock`)

**Structure:**

- `@contextmanager` decorator
- Single `yield` statement
- `try/finally` for cleanup guarantee

**Key Features:**

- Concise implementation
- Automatic exception safety
- Clean separation of setup/teardown

**Best For:**

- Simple resource patterns
- Quick context implementations
- Functional-style code

## Key Concepts

- **Resource Management**: Automatic acquisition/release
- **Exception Safety**: Guaranteed cleanup
- **Protocol Integration**: Seamless `with` statement support
- **Pattern Flexibility**: Choose implementation style

## How to Run

1. Execute the demo script:
   ```bash
   python main.py
   ```
2. Observe the output showing:

   - Context setup/teardown
   - Resource usage patterns
   - Clean execution flow

3. Experiment by uncommenting:
   - Exception examples to test error handling
   - Additional context operations

## Learning Outcomes

Through this module you will:

- Implement both context manager patterns
- Understand Python's context protocol
- Apply resource management best practices
- Handle exceptions in resource contexts
- Choose appropriate patterns for different scenarios

## Advanced Topics

1. **Nested Contexts**: Multiple `with` statements
2. **Dynamic Resources**: Context-dependent setup
3. **Reusable Contexts**: Factory patterns
4. **Async Contexts**: `__aenter__`/`__aexit__`

For deeper understanding, examine:

- The `__enter__`/`__exit__` protocol
- `contextlib` implementation details
- Exception propagation behavior
