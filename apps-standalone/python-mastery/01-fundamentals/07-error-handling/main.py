"""
Error Handling Demo
Demonstrates Python's exception handling mechanisms
"""


# Custom exceptions
class InvalidInputError(Exception):
    """Raised when input validation fails"""

    pass


class ResourceUnavailableError(Exception):
    """Raised when a required resource is unavailable"""

    pass


def demonstrate_basic_handling():
    """Basic try-except-else-finally structure"""
    try:
        # Code that might raise an exception
        numerator = 10
        denominator = int(input("Enter denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    else:
        print(f"Result: {result}")
    finally:
        print("This always executes (cleanup here)")


def demonstrate_custom_exceptions(data):
    """Shows raising and handling custom exceptions"""
    try:
        if not isinstance(data, dict):
            raise InvalidInputError("Expected dictionary input")

        if "required_key" not in data:
            raise ResourceUnavailableError("Missing required key")

        print("Data processing successful")
    except (InvalidInputError, ResourceUnavailableError) as e:
        print(f"Custom error occurred: {e}")


def demonstrate_exception_chaining():
    """Shows exception chaining and context"""
    try:
        # Simulate a low-level operation failure
        try:
            open("nonexistent_file.txt")
        except IOError as e:
            raise ResourceUnavailableError("File operation failed") from e
    except ResourceUnavailableError as e:
        print(f"Caught chained exception: {e}")
        print(f"Original cause: {e.__cause__}")


if __name__ == "__main__":
    print("=== BASIC ERROR HANDLING ===")
    demonstrate_basic_handling()

    print("\n=== CUSTOM EXCEPTIONS ===")
    demonstrate_custom_exceptions("invalid data")

    print("\n=== EXCEPTION CHAINING ===")
    demonstrate_exception_chaining()
