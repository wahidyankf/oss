"""
Python Descriptors Demo

Covers:
1. Basic descriptor protocol
2. Data vs non-data descriptors
3. Property implementation
4. Practical use cases
"""


# ========== BASIC DESCRIPTOR ==========
class VerboseAttribute:
    """
    Simple descriptor that logs access
    """

    def __init__(self, name):
        self.name = name
        self.value = None

    def __get__(self, obj, objtype=None):
        print(f"Accessing {self.name}")
        return self.value

    def __set__(self, obj, value):
        print(f"Updating {self.name} to {value}")
        self.value = value


# ========== VALIDATION DESCRIPTOR ==========
class PositiveNumber:
    """
    Descriptor that enforces positive numbers
    """

    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Value must be positive")
        obj.__dict__[self.name] = value


# ========== PROPERTY IMPLEMENTATION ==========
class PropertyLike:
    """
    Shows how @property works internally
    """

    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def setter(self, fset):
        self.fset = fset
        return self


# ========== DEMO CLASSES ==========
class DataModel:
    """Class using descriptors"""

    attr = VerboseAttribute("attr")
    positive = PositiveNumber("positive")

    def __init__(self, value):
        self.attr = value
        self.positive = 1


class Temperature:
    """Class using PropertyLike descriptor"""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @PropertyLike
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @PropertyLike
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


# ========== MAIN DEMO ==========
if __name__ == "__main__":
    print("=== PYTHON DESCRIPTORS DEMO ===\n")

    # Show basic descriptor
    print("--- VerboseAttribute Demo ---")
    data = DataModel(10)
    print(f"Initial value: {data.attr}")
    data.attr = 20
    print(f"Updated value: {data.attr}\n")

    # Show validation descriptor
    print("--- PositiveNumber Demo ---")
    print(f"Initial positive: {data.positive}")
    data.positive = 42
    print(f"Valid update: {data.positive}")
    try:
        data.positive = -1
    except ValueError as e:
        print(f"Invalid update: {e}\n")

    # Show property implementation
    print("--- PropertyLike Demo ---")
    temp = Temperature(25)
    print(f"25°C = {temp.fahrenheit}°F")
    temp.celsius = 100
    print(f"100°C = {temp.fahrenheit}°F")

    print("\n=== DEMO COMPLETE ===")
    print("Key Takeaways:")
    print("- Descriptors control attribute access")
    print("- Used to implement properties, methods")
    print("- Enable validation and side effects")
    print("- __get__/__set__/__delete__ methods")
