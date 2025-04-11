"""
Python Error Handling Comprehensive Demo

This heavily commented example demonstrates:
1. Basic exception handling
2. Custom exceptions
3. Exception chaining
4. Best practices
5. Real-world patterns

Key Concepts Covered:
- try/except/else/finally blocks
- Built-in exceptions
- Custom exception classes
- Exception chaining (raise from)
- Context managers
- Logging exceptions
"""

# ========== CUSTOM EXCEPTIONS ==========
"""
Custom Exceptions:
- Inherit from Exception (or more specific built-in)
- Should be named with 'Error' suffix
- Can add custom attributes/methods
"""


class InvalidInputError(Exception):
    """
    Raised when input validation fails.

    Attributes:
        message: Explanation of the error
        input_value: The invalid input that caused the error
    """

    def __init__(self, message, input_value=None):
        self.input_value = input_value
        super().__init__(message)


class ResourceUnavailableError(Exception):
    """
    Raised when a required resource is unavailable.

    Attributes:
        resource: Name of the unavailable resource
        reason: Explanation of why unavailable
    """

    def __init__(self, resource, reason):
        self.resource = resource
        self.reason = reason
        super().__init__(f"{resource} unavailable: {reason}")


# ========== BASIC ERROR HANDLING ==========
"""
Basic Exception Handling:
- try: Code that might raise exceptions
- except: Handle specific exceptions
- else: Runs if no exceptions
- finally: Always runs (cleanup code)
"""


def demonstrate_basic_handling():
    """Demonstrates basic try-except-else-finally structure."""
    try:
        # Code that might raise an exception
        numerator = 10
        denominator = int(input("Enter denominator (0 for ZeroDivisionError): "))
        result = numerator / denominator
    except ValueError as ve:
        print(f"ValueError: {ve} - Please enter a valid number")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde} - Cannot divide by zero")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Cleanup: This always executes (close resources here)")


# ========== CUSTOM EXCEPTION USAGE ==========
"""
Custom Exception Usage:
- Raise when business logic conditions aren't met
- More specific than built-in exceptions
- Can include additional context
"""


def demonstrate_custom_exceptions(data):
    """Demonstrates raising and handling custom exceptions."""
    try:
        if not isinstance(data, dict):
            raise InvalidInputError("Expected dictionary input", input_value=data)

        if "required_key" not in data:
            raise ResourceUnavailableError(
                resource="required_key", reason="Missing from input data"
            )

        print("Data processing successful")
    except (InvalidInputError, ResourceUnavailableError) as e:
        print(f"Custom error occurred: {type(e).__name__}: {e}")
        if isinstance(e, InvalidInputError):
            print(f"Invalid input value: {e.input_value}")


# ========== EXCEPTION CHAINING ==========
"""
Exception Chaining:
- raise...from shows causal relationship
- Preserves original traceback
- Helps debugging complex failures
"""


def demonstrate_exception_chaining():
    """Demonstrates exception chaining and context."""
    try:
        # Simulate a low-level operation failure
        try:
            with open("nonexistent_file.txt") as f:
                content = f.read()
        except IOError as e:
            raise ResourceUnavailableError(
                resource="nonexistent_file.txt", reason="File not found"
            ) from e
    except ResourceUnavailableError as e:
        print(f"Caught chained exception: {type(e).__name__}: {e}")
        print(f"Original cause: {type(e.__cause__).__name__}: {e.__cause__}")


# ========== MAIN DEMO ==========
if __name__ == "__main__":
    print("\n=== BASIC ERROR HANDLING ===")
    demonstrate_basic_handling()

    print("\n=== CUSTOM EXCEPTIONS ===")
    demonstrate_custom_exceptions("invalid data")

    print("\n=== EXCEPTION CHAINING ===")
    demonstrate_exception_chaining()
