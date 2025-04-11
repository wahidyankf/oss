"""
Multiple Inheritance Demonstration

This heavily commented example demonstrates:
1. Multiple inheritance behavior
2. Method Resolution Order (MRO)
3. Method name collision handling

Key Concepts Illustrated:
- Diamond inheritance pattern
- Superclass method precedence
- Python's MRO algorithm
"""


class Camera:
    """
    Camera functionality class.

    Represents one parent in multiple inheritance.
    Contains:
    - take_photo(): Camera-specific method
    - power_on(): Method that will collide with Phone
    """

    def take_photo(self):
        """
        Simulate taking a photo.

        Returns:
            str: Camera shutter sound
        """
        return "Click!"

    def power_on(self):
        """
        Camera-specific power on method.

        Returns:
            str: Camera power status
        """
        return "Camera powered on"


class Phone:
    """
    Phone functionality class.

    Represents second parent in multiple inheritance.
    Contains:
    - make_call(): Phone-specific method
    - power_on(): Method that collides with Camera
    """

    def make_call(self):
        """
        Simulate making a phone call.

        Returns:
            str: Ringing sound
        """
        return "Ring ring..."

    def power_on(self):
        """
        Phone-specific power on method.

        Returns:
            str: Phone power status
        """
        return "Phone powered on"


class SmartPhone(Camera, Phone):
    """
    SmartPhone class demonstrating multiple inheritance.

    Inherits from both Camera and Phone, showing:
    - Method resolution when methods collide (power_on)
    - The MRO that determines lookup order

    Note: Camera appears first in inheritance list,
    so its power_on() will be used.
    """

    pass


if __name__ == "__main__":
    """
    Demonstration of multiple inheritance concepts.

    Shows:
    - Combined functionality from both parents
    - Method collision resolution
    - The actual MRO Python uses
    """
    # Create smartphone instance
    phone = SmartPhone()

    # Demonstrate combined functionality
    print("Multiple Inheritance Demo:")
    print(f"Features: {phone.take_photo()} and {phone.make_call()}")

    # Show method collision resolution
    print(f"\nMethod Collision:")
    print(f"Power on behavior: {phone.power_on()}")
    print(f"This uses: {SmartPhone.power_on.__qualname__}")

    # Display Python's Method Resolution Order
    print(f"\nMethod Resolution Order (MRO):")
    print(SmartPhone.__mro__)
