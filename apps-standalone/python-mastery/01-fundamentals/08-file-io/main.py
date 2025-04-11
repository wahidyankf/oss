"""
Comprehensive File I/O Demonstration

This module demonstrates Python file operations with:
1. Proper error handling
2. Context managers (with)
3. Different file modes
4. Path handling best practices
5. Real-world patterns

Key Concepts Covered:
- Reading/writing text and binary files
- Using pathlib for cross-platform paths
- Exception handling for file operations
- File encoding considerations
- Temporary files and cleanup
"""

from pathlib import Path

# ========== CUSTOM EXCEPTIONS ==========
"""
File Operation Exceptions:
- Custom exceptions provide better error context
- Inherit from appropriate built-in exceptions
- Include relevant file system details
"""


class FileOperationError(Exception):
    """
    Custom exception for file operation failures.

    Attributes:
        path: The file path involved
        operation: The failed operation (read/write/etc)
        original_error: The underlying exception
    """

    def __init__(self, path, operation, original_error):
        self.path = path
        self.operation = operation
        self.original_error = original_error
        super().__init__(f"Failed to {operation} file at {path}: {original_error}")


# ========== BASIC FILE OPERATIONS ==========
"""
Basic File Operations:
- Always use context managers (with)
- Handle specific exceptions
- Include cleanup in finally blocks
"""


def demonstrate_basic_operations():
    """Demonstrates fundamental file operations with proper error handling."""
    file_path = Path("example.txt")

    try:
        # 1. Writing to file
        print("=== WRITING TO FILE ===")

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("Line 1: Hello File World!\n")
                f.write("Line 2: Second line content\n")
                print(f"Successfully wrote to {file_path}")
        except (PermissionError, IsADirectoryError) as e:
            raise FileOperationError(str(file_path), "write", e)

        # 2. Reading from file
        print("\n=== READING FROM FILE ===")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"File content:\n{content}")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except UnicodeDecodeError as e:
            raise FileOperationError(str(file_path), "read (decode)", e)

    finally:
        # 3. Cleanup
        if file_path.exists():
            print("\n=== CLEANUP ===")
            file_path.unlink()
            print(f"Removed {file_path}")


# ========== ADVANCED FILE OPERATIONS ==========
"""
Advanced File Operations:
- Working with binary files
- Using pathlib for path operations
- Handling different file encodings
"""


def demonstrate_advanced_operations():
    """Demonstrates more complex file operations."""
    # Using pathlib for robust path handling
    data_dir = Path("data_files")
    binary_file = data_dir / "example.bin"

    try:
        # Create directory if needed
        data_dir.mkdir(exist_ok=True)

        # Binary file operations
        print("\n=== BINARY FILE OPERATIONS ===")

        try:
            with open(binary_file, "wb") as f:
                f.write(b"Binary data \x01\x02\x03")
                print(f"Wrote binary data to {binary_file}")

            with open(binary_file, "rb") as f:
                data = f.read()
                print(f"Read binary data: {data}")
        except OSError as e:
            raise FileOperationError(str(binary_file), "binary operation", e)

    finally:
        # Cleanup
        if binary_file.exists():
            binary_file.unlink()
        if data_dir.exists():
            data_dir.rmdir()


# ========== MAIN DEMO ==========
if __name__ == "__main__":
    print("=== FILE I/O DEMONSTRATION ===\n")

    try:
        demonstrate_basic_operations()
        demonstrate_advanced_operations()
    except FileOperationError as e:
        print(f"\nERROR: {e}")
        print(f"Original error: {type(e.original_error).__name__}: {e.original_error}")
    except Exception as e:
        print(f"\nUNEXPECTED ERROR: {type(e).__name__}: {e}")
    finally:
        print("\nDemo completed.")
