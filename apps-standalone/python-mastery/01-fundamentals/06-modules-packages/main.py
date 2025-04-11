"""
Python Modules & Packages Comprehensive Demo

This heavily commented example demonstrates:
1. All Python module/package import techniques
2. Practical examples with clear output
3. Standard library module usage
4. Package structure best practices

Key Concepts Covered:
- Module imports and namespaces
- Package structure and organization
- Import styles and aliasing
- Standard library modules
- Relative vs absolute imports
- __init__.py usage
"""

# ========== BASIC MODULE IMPORTS ==========
"""
Basic Module Import:
- Imports entire module into its own namespace
- Access contents using module_name.attribute
- Most explicit but most verbose
"""
print("\n=== BASIC MODULE IMPORT ===")
import demo_module  # Imports demo_module.py

print(demo_module.module_function())  # Access module contents
print(demo_module.module_variable)  # Using dot notation

# ========== SPECIFIC IMPORT ==========
"""
Specific Import:
- Imports only specified names into current namespace
- More concise but can cause name collisions
- Avoid 'from module import *' (pollutes namespace)
"""
print("\n=== SPECIFIC IMPORT ===")
from demo_module import ModuleClass  # Import just ModuleClass

obj = ModuleClass()  # Use directly without module prefix
print(f"Value from ModuleClass: {obj.get_value()}")

# ========== IMPORT WITH ALIAS ==========
"""
Import with Alias:
- Useful for long module names
- Can prevent naming conflicts
- Common in data science (import numpy as np)
"""
print("\n=== IMPORT WITH ALIAS ===")
import demo_module as dm  # Create short alias

print(f"Aliased import: {dm.module_function()}")

# ========== PACKAGE IMPORTS ==========
"""
Package Imports:
- Packages are directories containing modules
- Must contain __init__.py (can be empty)
- Use dot notation to access submodules
"""
print("\n=== PACKAGE IMPORTS ===")
from demo_package import package_function  # Import from package

print(package_function())

# ========== SUBPACKAGE IMPORTS ==========
"""
Subpackage Imports:
- Packages can be nested arbitrarily deep
- Each level should have __init__.py
- Can use relative imports within package
"""
print("\n=== SUBPACKAGE IMPORT ===")
from demo_package.subpackage import subpackage_function

print(subpackage_function())

# ========== STANDARD LIBRARY IMPORTS ==========
"""
Standard Library:
- Python comes with many built-in modules
- math: Mathematical functions
- datetime: Date/time handling
- os: Operating system interfaces
- Many more (see Python docs)
"""
print("\n=== STANDARD LIBRARY ===")
from math import pi, sqrt
from datetime import datetime

print(f"Square root of 16: {sqrt(16)}")
print(f"Current time: {datetime.now()}")

# ========== PACKAGE CONTENTS ==========
"""
Package Contents:
- Can import entire package
- __init__.py can define package-level variables/functions
- Can expose subpackage contents at package level
"""
print("\n=== PACKAGE CONTENTS ===")
import demo_package  # Import entire package

print(f"Package variable: {demo_package.package_variable}")
print(f"From subpackage: {demo_package.subpackage_function()}")
