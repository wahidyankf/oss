"""
Python Metaclasses Demo

Covers:
1. Basic metaclass creation
2. Customizing class creation
3. Practical use cases
4. Type as default metaclass
"""


# ========== BASIC METACLASS ==========
class SimpleMeta(type):
    """
    Simple metaclass that prints when classes are created
    """

    def __new__(cls, name, bases, namespace):
        print(f"Creating class {name} with metaclass {cls.__name__}")
        return super().__new__(cls, name, bases, namespace)


# ========== CLASS REGISTRY METACLASS ==========
class RegistryMeta(type):
    """
    Metaclass that maintains a registry of all classes
    """

    registry = {}

    def __new__(cls, name, bases, namespace):
        new_class = super().__new__(cls, name, bases, namespace)
        cls.registry[name] = new_class
        return new_class


# ========== VALIDATION METACLASS ==========
class ValidateFieldsMeta(type):
    """
    Metaclass that validates class field names
    """

    def __new__(cls, name, bases, namespace):
        # Validate field names
        for attr_name in namespace:
            if attr_name.startswith("_"):
                continue
            if not attr_name.islower():
                raise ValueError(f"Field '{attr_name}' must be lowercase")

        return super().__new__(cls, name, bases, namespace)


# ========== DEMO CLASSES ==========
class BasicClass(metaclass=SimpleMeta):
    """Class created with SimpleMeta metaclass"""

    pass


class PluginBase(metaclass=RegistryMeta):
    """Base class for plugin system"""

    pass


class PluginA(PluginBase):
    """First plugin"""

    pass


class PluginB(PluginBase):
    """Second plugin"""

    pass


class ValidatedModel(metaclass=ValidateFieldsMeta):
    """Class with field validation"""

    valid_field = 42
    # InvalidField = 100  # Would raise ValueError


# ========== MAIN DEMO ==========
if __name__ == "__main__":
    print("=== PYTHON METACLASSES DEMO ===\n")

    # Show basic metaclass
    print("BasicClass was created with SimpleMeta")
    print(f"Type of BasicClass: {type(BasicClass)}")
    print(f"Type of BasicClass instance: {type(BasicClass())}\n")

    # Show registry metaclass
    print(f"Registered classes: {RegistryMeta.registry}")
    print(f"PluginA type: {type(PluginA)}")
    print(f"PluginB type: {type(PluginB)}\n")

    # Show validation metaclass
    print("ValidatedModel created successfully with valid_field")
    try:

        class InvalidModel(metaclass=ValidateFieldsMeta):
            InvalidField = 100

    except ValueError as e:
        print(f"Validation error: {e}")

    print("\n=== DEMO COMPLETE ===")
    print("Key Takeaways:")
    print("- Metaclasses control class creation")
    print("- Useful for frameworks and validation")
    print("- type is the default metaclass")
    print("- Use sparingly as they add complexity")
