"""
Python Modules and Packages Demo

Key concepts demonstrated:
1. Module imports
2. Package structure
3. Different import styles
4. Standard library modules
"""

# 1. Importing modules
print("=== MODULE IMPORTS ===")
import demo_module

print(demo_module.module_function())
print(demo_module.module_variable)

# 2. Importing specific items
from demo_module import ModuleClass

obj = ModuleClass()
print(f"Value from ModuleClass: {obj.get_value()}")

# 3. Import with alias
import demo_module as dm

print(f"Aliased import: {dm.module_function()}")

# 4. Importing from packages
from demo_package import package_function

print(f"\n=== PACKAGE IMPORTS ===")
print(package_function())

# 5. Accessing subpackage
from demo_package.subpackage import subpackage_function

print(subpackage_function())

# 6. Standard library examples
print("\n=== STANDARD LIBRARY ===")
from math import pi, sqrt
from datetime import datetime

print(f"Square root of 16: {sqrt(16)}")
print(f"Current time: {datetime.now()}")

# 7. Package contents
print("\n=== PACKAGE CONTENTS ===")
import demo_package

print(f"Package variable: {demo_package.package_variable}")
print(f"From subpackage: {demo_package.subpackage_function()}")
