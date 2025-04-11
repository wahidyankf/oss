"""
Simple calculator implementation for testing demo
"""


def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
