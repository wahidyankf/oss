"""
Practical Uses of Descriptors

Key Concept:
Descriptors enable powerful patterns like validation, logging,
and framework features
"""


# ===== USE CASE 1: ATTRIBUTE VALIDATION =====
class BoundedNumber:
    """Descriptor that enforces min/max values"""

    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __set__(self, obj, value):
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"Value must be between {self.min_val} and {self.max_val}")
        obj.__dict__[self.__name__] = value

    def __set_name__(self, owner, name):
        self.__name__ = name


# ===== USE CASE 2: AUTOMATIC REGISTRATION =====
class PluginRegistry:
    """Descriptor that registers plugin classes"""

    registry = {}

    def __init__(self, name):
        self.name = name

    def __set__(self, obj, value):
        self.registry[self.name] = obj


# ===== USE CASE 3: LAZY EVALUATION =====
class LazyProperty:
    """Descriptor that computes value once and caches it"""

    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        obj.__dict__[self.__name__] = value
        return value


# ===== DEMO CLASSES =====
class GameCharacter:
    """Uses BoundedNumber for attribute validation"""

    health = BoundedNumber(0, 100)
    mana = BoundedNumber(0, 200)

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana


class Plugin:
    """Uses PluginRegistry for automatic registration"""

    register = PluginRegistry("plugins")


class DataProcessor:
    """Uses LazyProperty for expensive computations"""

    def __init__(self, data):
        self.data = data

    @LazyProperty
    def processed_data(self):
        print("Performing expensive computation...")
        return [x * 2 for x in self.data]


if __name__ == "__main__":
    print("=== PRACTICAL DESCRIPTOR USES ===\n")

    # Validation demo
    print("1. Attribute Validation:")
    char = GameCharacter(50, 100)
    print(f"Initial: health={char.health}, mana={char.mana}")
    try:
        char.health = 150  # Should raise ValueError
    except ValueError as e:
        print(f"Validation error: {e}\n")

    # Registration demo
    print("2. Automatic Registration:")
    plugin = Plugin()
    plugin.register = plugin  # Self-register
    print(f"Registered plugins: {PluginRegistry.registry}\n")

    # Lazy evaluation demo
    print("3. Lazy Evaluation:")
    processor = DataProcessor([1, 2, 3])
    print("First access (computes):", processor.processed_data)
    print("Second access (cached):", processor.processed_data)

    print("\nKey Takeaway:")
    print(
        "- Descriptors enable clean solutions for validation, registration,"
        " lazy loading and more"
    )
