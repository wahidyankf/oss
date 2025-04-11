# Python Descriptors Demos

This directory contains four focused demonstrations of Python descriptors:

## 1. Basic Descriptor Protocol (`basic_descriptor.py`)

- Demonstrates the fundamental `__get__` and `__set__` methods
- Shows how descriptors intercept attribute access
- Key takeaway: Descriptors control attribute access on classes

## 2. Data vs Non-Data Descriptors (`data_vs_non_data.py`)

- Compares descriptors with and without `__set__` method
- Shows how instance dictionaries interact with descriptors
- Key takeaway: Data descriptors override instance dict access

## 3. Property Implementation (`property_implementation.py`)

- Reveals how `@property` works internally using descriptors
- Demonstrates getter/setter functionality
- Key takeaway: `@property` uses descriptor protocol internally

## 4. Practical Uses (`practical_uses.py`)

- Shows real-world descriptor applications:
  - Attribute validation with bounds checking
  - Automatic class registration
  - Lazy evaluation of expensive computations
- Key takeaway: Descriptors enable clean solutions for common patterns

## How to Run

Run each demo individually:

```bash
python basic_descriptor.py
python data_vs_non_data.py
python property_implementation.py
python practical_uses.py
```

## Learning Path

1. Start with `basic_descriptor.py` to understand the core protocol
2. Move to `data_vs_non_data.py` to see descriptor precedence rules
3. Examine `property_implementation.py` to understand property mechanics
4. Finish with `practical_uses.py` to see real-world applications

## Key Concepts Illustrated

- Descriptor protocol (`__get__`, `__set__`, `__delete__`)
- Difference between data and non-data descriptors
- How properties and methods work under the hood
- Practical patterns like validation and lazy loading
