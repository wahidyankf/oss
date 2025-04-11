"""
Basic Descriptor Protocol Demo

Key Concept:
Descriptors control attribute access on classes via __get__ and __set__ methods
"""


class LoggedAccess:
    """
    Descriptor that logs all attribute access
    """

    def __init__(self, name):
        self.name = name
        self.value = None

    def __get__(self, obj, objtype=None):
        print(f"Getting {self.name}")
        return self.value

    def __set__(self, obj, value):
        print(f"Setting {self.name} to {value}")
        self.value = value


class MyClass:
    attr = LoggedAccess("attr")


if __name__ == "__main__":
    print("=== BASIC DESCRIPTOR DEMO ===\n")
    obj = MyClass()
    obj.attr = 10  # Calls __set__
    print(f"Value: {obj.attr}")  # Calls __get__
    print("\nKey Takeaway:")
    print("- Descriptors intercept attribute access via __get__/__set__")
