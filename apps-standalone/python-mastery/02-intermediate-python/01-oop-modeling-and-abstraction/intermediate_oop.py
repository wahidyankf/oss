"""
Intermediate Object-Oriented Programming Demo

This heavily commented example demonstrates:
1. Abstract Base Classes (ABC) - enforcing interface contracts
2. Polymorphism - different animal implementations
3. Class vs Static Methods - temperature conversion utilities

Key Concepts Illustrated:
- Abstraction through ABC
- Polymorphic behavior
- Utility method organization
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class defining animal interface.

    Purpose:
    - Forces subclasses to implement make_sound()
    - Provides common sleep() implementation
    - Demonstrates interface enforcement
    """

    @abstractmethod
    def make_sound(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            str: Sound the animal makes
        """
        pass

    def sleep(self):
        """
        Concrete method shared by all animals.

        Returns:
            str: Sleeping representation
        """
        return "Zzz..."


class TemperatureConverter:
    """
    Utility class demonstrating method types.

    Key Differences:
    - Class methods: receive cls, can modify class state
    - Static methods: pure functions, no cls/self
    """

    @classmethod
    def celsius_to_fahrenheit(cls, c):
        """
        Convert Celsius to Fahrenheit (class method).

        Args:
            c (float): Temperature in Celsius

        Returns:
            float: Temperature in Fahrenheit
        """
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        """
        Convert Fahrenheit to Celsius (static method).

        Args:
            f (float): Temperature in Fahrenheit

        Returns:
            float: Temperature in Celsius
        """
        return (f - 32) * 5 / 9


class Dog(Animal):
    """
    Concrete Animal implementation for dogs.

    Demonstrates:
    - Interface implementation
    - Method overriding
    """

    def make_sound(self):
        """Dog-specific sound implementation"""
        return "Woof!"


class Cat(Animal):
    """
    Concrete Animal implementation for cats.

    Shows polymorphic behavior - same interface,
    different implementation
    """

    def make_sound(self):
        """Cat-specific sound implementation"""
        return "Meow!"


if __name__ == "__main__":
    """
    Demonstration of intermediate OOP concepts.

    Shows:
    - Polymorphism through Animal ABC
    - Temperature conversion utilities
    """
    # Create animal instances
    animals = [Dog(), Cat()]

    # Demonstrate polymorphism
    print("Polymorphism Demo:")
    for animal in animals:
        print(f"{animal.__class__.__name__} says: {animal.make_sound()}")
        print(f"{animal.__class__.__name__} sleeps: {animal.sleep()}")

    # Demonstrate temperature conversion
    print("\nTemperature Conversion:")
    print(f"37°C is {TemperatureConverter.celsius_to_fahrenheit(37)}°F")
    print(f"98.6°F is {TemperatureConverter.fahrenheit_to_celsius(98.6)}°C")
