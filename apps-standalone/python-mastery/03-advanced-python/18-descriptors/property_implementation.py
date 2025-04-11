"""
Property Implementation Demo

Key Concept:
The descriptor protocol is how @property works internally
"""


class PropertyLike:
    """
    Simplified version of Python's @property decorator
    using descriptors
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
        """Allows method chaining like @property.setter"""
        self.fset = fset
        return self


class Temperature:
    """
    Class demonstrating property-like behavior
    using our PropertyLike descriptor
    """

    def __init__(self, celsius=0):
        self._celsius = celsius

    @PropertyLike
    def celsius(self):
        """Getter for celsius temperature"""
        return self._celsius

    # Note: This intentionally reuses the method name 'celsius' to demonstrate
    # how @property.setter works in Python. The name collision warning is expected.
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius temperature"""
        self._celsius = value

    @PropertyLike
    def fahrenheit(self):
        """Read-only computed property"""
        return (self._celsius * 9 / 5) + 32


if __name__ == "__main__":
    print("=== PROPERTY IMPLEMENTATION DEMO ===\n")

    temp = Temperature(25)
    print(f"25°C = {temp.fahrenheit}°F")
    temp.celsius = 100
    print(f"100°C = {temp.fahrenheit}°F")

    try:
        temp.fahrenheit = 212  # Should raise AttributeError
    except AttributeError as e:
        print(f"\nExpected error when setting read-only property: {e}")

    print("\nKey Takeaway:")
    print("- @property uses descriptor protocol internally")
    print("- PropertyLike demonstrates the core mechanism")
