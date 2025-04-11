"""
Demo Module - Comprehensive Example

This module demonstrates:
1. Module-level variables
2. Module functions
3. Module classes
4. Documentation standards

When imported, this module's code executes normally.
When run directly, it can include test code (see __name__ check).
"""

# ========== MODULE VARIABLE ==========
"""
Module-level variables:
- Accessible via module_name.variable
- Shared across all imports
- Convention is to use ALL_CAPS for constants
"""
module_variable = "This is a module-level variable"


# ========== MODULE FUNCTION ==========
def module_function() -> str:
    """
    Demonstrates a module-level function.

    Returns:
        str: A greeting message from the module
    """
    return "Hello from module_function"


# ========== MODULE CLASS ==========
class ModuleClass:
    """
    Demonstrates a module-level class.

    Attributes:
        value (int): A sample value initialized to 42
    """

    def __init__(self):
        """Initializes with default value 42."""
        self.value = 42

    def get_value(self) -> int:
        """
        Gets the current value.

        Returns:
            int: The stored value
        """
        return self.value


# ========== MODULE TEST CODE ==========
if __name__ == "__main__":
    """
    Test code that runs only when module is executed directly.
    Not run when module is imported.
    """
    print("Running module tests:")
    print(module_function())
    print(ModuleClass().get_value())
