"""
Data vs Non-Data Descriptors Demo

Key Concept:
Data descriptors (with __set__) take precedence over instance dictionaries
Non-data descriptors (only __get__) can be overridden by instance attributes
"""


class DataDescriptor:
    """Data descriptor with both __get__ and __set__"""

    def __get__(self, obj, objtype=None):
        print("DataDescriptor.__get__")
        return "data value"

    def __set__(self, obj, value):
        print("DataDescriptor.__set__")


class NonDataDescriptor:
    """Non-data descriptor with only __get__"""

    def __get__(self, obj, objtype=None):
        print("NonDataDescriptor.__get__")
        return "non-data value"


class MyClass:
    data_attr = DataDescriptor()
    non_data_attr = NonDataDescriptor()


if __name__ == "__main__":
    print("=== DATA VS NON-DATA DESCRIPTORS ===\n")

    obj = MyClass()

    print("1. Data descriptor always wins:")
    print(f"Initial: {obj.data_attr}")
    obj.data_attr = "instance value"  # Still uses descriptor
    print(f"After assignment: {obj.data_attr}\n")

    print("2. Non-data descriptor can be overridden:")
    print(f"Initial: {obj.non_data_attr}")
    # Note: The following intentionally triggers a type checker warning
    # to demonstrate that non-data descriptors can be overridden by
    # instance attributes. This is expected behavior for the demo.
    obj.non_data_attr = "instance value"  # Stores in instance dict
    print(f"After assignment: {obj.non_data_attr}\n")

    print("Key Takeaway:")
    print("- Data descriptors (with __set__) override instance dict")
