"""
Sample module demonstrating module concepts.
"""

module_variable = "This is a module-level variable"


def module_function():
    """Sample function in the module"""
    return "Hello from module_function"


class ModuleClass:
    """Sample class in the module"""

    def __init__(self):
        self.value = 42

    def get_value(self):
        return self.value
