"""
Python Descriptors Demo

Demonstrates the descriptor protocol (__get__, __set__, __delete__) which
underlies Python's attribute access mechanism. Used by @property, @classmethod,
and @staticmethod.

Key Concepts:
1. Descriptors control attribute access on classes
2. Data descriptors (with __set__) take precedence over instance dictionaries
3. Non-data descriptors (only __get__) can be overridden by instance attributes
4. The descriptor protocol is how properties work internally
"""


# ========== BASIC DESCRIPTOR ==========
class VerboseAttribute:
    """
    Simple descriptor that logs all access operations.
    Demonstrates basic __get__ and __set__ implementation.

    Note: This is a data descriptor (has __set__) so it will always
    take precedence over instance dictionary attributes.
    """

    def __init__(self, name):
        """Initialize with the public attribute name for logging"""
        self.name = name
        self.value = None

    def __get__(self, obj, objtype=None):
        """
        Called when attribute is accessed.
        obj: Instance the descriptor is accessed through
        objtype: The class of the instance
        """
        print(f"Accessing {self.name}")
        return self.value

    def __set__(self, obj, value):
        """
        Called when attribute is set.
        obj: Instance the descriptor is assigned to
        value: Value being assigned
        """
        print(f"Updating {self.name} to {value}")
        self.value = value


# ========== VALIDATION DESCRIPTOR ==========
class PositiveNumber:
    """
    Descriptor that enforces positive numbers by validating on __set__.
    Stores values in the instance's __dict__ rather than descriptor itself.

    Note: This pattern is useful for data validation while keeping
    the actual storage in the instance dictionary.
    """

    def __init__(self, name):
        """Initialize with the attribute name for storage"""
        self.name = name

    def __get__(self, obj, objtype=None):
        """
        Get value from instance's __dict__ with default of 0.
        Note: Using obj.__dict__ directly for storage avoids infinite recursion.
        """
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        """Validate value is positive before storing in instance __dict__"""
        if value < 0:
            raise ValueError("Value must be positive")
        obj.__dict__[self.name] = value


# ========== PROPERTY IMPLEMENTATION ==========
class PropertyLike:
    """
    Demonstrates how @property works internally by implementing
    a simplified property-like descriptor with getter/setter support.

    Note: The setter() method returns self to allow method chaining,
    which is why @property.setter works in Python.
    """

    def __init__(self, fget=None, fset=None):
        """Store getter and setter functions"""
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, objtype=None):
        """
        Call the getter function when attribute is accessed.
        Returns self if accessed through class rather than instance.
        """
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        """Call the setter function when attribute is assigned"""
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def setter(self, fset):
        """
        Decorator to set the setter function.
        Returns self to allow method chaining (@temperature.setter).
        """
        self.fset = fset
        return self


# ========== DEMO CLASSES ==========
class DataModel:
    """
    Example class demonstrating descriptor usage with:
    1. VerboseAttribute for logging access
    2. PositiveNumber for validation
    """

    attr = VerboseAttribute("attr")  # Will log all access
    positive = PositiveNumber("positive")  # Validates values

    def __init__(self, value):
        """Initialize with a value for the tracked attributes"""
        self.attr = value  # Will trigger VerboseAttribute.__set__
        self.positive = 1  # Will store in instance __dict__ via PositiveNumber


class Temperature:
    """
    Demonstrates property-like behavior using our PropertyLike descriptor.
    Shows both getter and setter functionality.

    Note: The method name collision warning is intentional here to
    demonstrate how @property.setter works in Python.
    """

    def __init__(self, celsius=0):
        """Initialize with celsius temperature"""
        self._celsius = celsius  # Internal storage

    @PropertyLike
    def celsius(self):
        """Getter for celsius temperature"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius temperature"""
        self._celsius = value

    @PropertyLike
    def fahrenheit(self):
        """Read-only computed property for fahrenheit"""
        return (self._celsius * 9 / 5) + 32


# ========== MAIN DEMO ==========
if __name__ == "__main__":
    print("=== PYTHON DESCRIPTORS DEMO ===\n")

    # Show basic descriptor functionality
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
        data.positive = -1  # This will raise ValueError
    except ValueError as e:
        print(f"Invalid update: {e}\n")

    # Show property implementation
    print("--- PropertyLike Demo ---")
    temp = Temperature(25)
    print(f"25°C = {temp.fahrenheit}°F")
    temp.celsius = 100  # Uses our PropertyLike descriptor
    print(f"100°C = {temp.fahrenheit}°F")

    print("\n=== DEMO COMPLETE ===")
    print("Key Takeaways:")
    print("- Descriptors control attribute access via __get__/__set__")
    print("- Used to implement @property, @classmethod, @staticmethod")
    print("- Enable validation, logging, and other attribute side effects")
    print("- Data descriptors (with __set__) override instance dict access")
