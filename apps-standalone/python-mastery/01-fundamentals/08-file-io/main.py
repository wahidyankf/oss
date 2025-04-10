"""
File I/O Demo
Demonstrates reading/writing files in Python with exception handling
"""

import os
from pathlib import Path


# Custom exception for file operations
class FileOperationError(Exception):
    """Custom exception for file operation errors"""

    pass


def safe_file_operations():
    """Demonstrates file operations with proper error handling"""
    try:
        # 1. Basic file writing
        print("=== BASIC FILE WRITING ===")
        try:
            with open("example.txt", "w") as f:
                f.write("Hello file world!\n")
                f.write("Second line\n")
        except (IOError, PermissionError) as e:
            raise FileOperationError(f"Failed to write file: {e}")

        # 2. Basic file reading
        print("\n=== BASIC FILE READING ===")
        try:
            with open("example.txt", "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("Error: File not found")
        except IOError as e:
            print(f"Error reading file: {e}")

        # 3. Reading line by line
        print("\n=== READING LINE BY LINE ===")
        try:
            with open("example.txt", "r") as f:
                for i, line in enumerate(f):
                    print(f"Line {i+1}: {line.strip()}")
        except FileNotFoundError:
            print("Error: File not found")
        except IOError as e:
            print(f"Error reading file: {e}")

        # 4. Using pathlib for modern path handling
        print("\n=== PATHLIB DEMO ===")
        file_path = Path("example.txt")
        try:
            print(f"File exists: {file_path.exists()}")
            print(f"File size: {file_path.stat().st_size} bytes")
        except OSError as e:
            print(f"Error accessing file metadata: {e}")

        # 5. File append mode
        print("\n=== APPEND MODE ===")
        try:
            with open("example.txt", "a") as f:
                f.write("This line was appended\n")
        except (IOError, PermissionError) as e:
            raise FileOperationError(f"Failed to append to file: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Clean up
        try:
            if os.path.exists("example.txt"):
                os.remove("example.txt")
        except OSError as e:
            print(f"Error during cleanup: {e}")


if __name__ == "__main__":
    safe_file_operations()
