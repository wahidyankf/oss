# Python Modules and Packages Demo

This directory demonstrates Python's module and package system.

## Structure

```
06-modules-packages/
├── modules_demo.py       # Main demo script
├── demo_module.py        # Standalone module
└── demo_package/         # Example package
    ├── __init__.py       # Package initialization
    ├── module_in_package.py  # Module within package
    └── subpackage/       # Subpackage example
        └── __init__.py   # Subpackage initialization
```

## Key Concepts Demonstrated

1. **Module Imports**

   - Basic imports (`import demo_module`)
   - Specific imports (`from demo_module import ModuleClass`)
   - Aliased imports (`import demo_module as dm`)

2. **Package Structure**

   - Package directories require `__init__.py`
   - Subpackages follow the same structure
   - Package-level variables and imports in `__init__.py`

3. **Standard Library Usage**
   - Examples using `math` and `datetime` modules

## How to Run

1. Execute the main demo:

   ```bash
   python modules_demo.py
   ```

2. Expected output shows:
   - Module imports and usage
   - Package imports and structure
   - Standard library functionality

## Key Takeaways

- Modules are single `.py` files
- Packages are directories containing `__init__.py`
- Import statements affect namespace access
- The Python Standard Library provides many useful modules
