"""
Context Managers Comprehensive Demonstration

This script illustrates two fundamental ways to implement Python context managers:
1. Class-based approach using __enter__ and __exit__ methods
2. Generator-based approach using @contextmanager decorator

Key Concepts Illustrated:
- Resource acquisition/release patterns
- Exception safety guarantees
- The with statement protocol
- Practical use cases
"""

from contextlib import contextmanager

# ========== CLASS-BASED CONTEXT MANAGER ==========
"""
DatabaseConnection demonstrates a class-based context manager for managing
database connections with proper setup/teardown.

This pattern is ideal when:
- You need complex setup/teardown logic
- You want to maintain state between enter/exit
- The resource requires object-oriented management
"""


class DatabaseConnection:
    """
    Simulates a database connection context manager.

    Attributes:
        db_name: Name of the database to connect to
        connection: The active connection object (simulated)
    """

    def __init__(self, db_name):
        """Initialize with database name but don't connect yet."""
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """
        Enter the runtime context - performs setup.

        Returns:
            The connection object to be used in the with block
        """
        print(f"[CONNECTING] Opening connection to {self.db_name}...")
        # Simulate establishing a connection
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context - performs cleanup.

        Args:
            exc_type: Exception type if exception occurred, else None
            exc_val: Exception value if exception occurred, else None
            exc_tb: Traceback if exception occurred, else None

        Returns:
            True to suppress exceptions, False to propagate them
        """
        print(f"[DISCONNECTING] Closing {self.db_name} connection")
        # Simulate closing the connection
        self.connection = None

        # Handle exceptions if they occurred in the with block
        if exc_type:
            print(f"[ERROR] Operation failed: {exc_val}")

        # Return False to propagate any exceptions
        return False


# ========== GENERATOR-BASED CONTEXT MANAGER ==========
"""
file_lock demonstrates a generator-based context manager using the
@contextmanager decorator from contextlib.

This pattern is ideal when:
- You want more concise implementation
- Your setup/teardown is relatively simple
- You're comfortable with generator functions
"""


@contextmanager
def file_lock(lock_name):
    """
    Manages file lock acquisition and release.

    Args:
        lock_name: Name/ID of the lock to acquire

    Yields:
        The lock object to be used in the with block
    """
    print(f"[LOCK] Acquiring {lock_name}...")
    # Simulate lock acquisition
    lock = f"Lock-{lock_name}"

    try:
        yield lock  # This is where the with block executes
    finally:
        # This always runs, even if an exception occurs
        print(f"[UNLOCK] Releasing {lock_name}")
        # Simulate lock release


# ========== DEMONSTRATION ==========
if __name__ == "__main__":
    """
    Main execution block demonstrating both context manager types.
    """
    print("=== CLASS-BASED CONTEXT MANAGER DEMO ===")
    with DatabaseConnection("production_db") as conn:
        print(f"[USING] Connection: {conn}")
        # Simulate database operations
        print("[WORK] Executing queries...")
        # Uncomment to test exception handling:
        # raise ValueError("Query failed!")

    print("\n=== GENERATOR-BASED CONTEXT MANAGER DEMO ===")
    with file_lock("critical_section") as lock:
        print(f"[USING] Lock: {lock}")
        # Simulate locked operations
        print("[WORK] Performing protected operations...")
        # Uncomment to test exception handling:
        # raise RuntimeError("Operation failed!")

    print("\n=== DEMO COMPLETED SUCCESSFULLY ===")
