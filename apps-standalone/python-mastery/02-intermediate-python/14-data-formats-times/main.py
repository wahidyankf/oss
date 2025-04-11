"""
Python Data Formats and Times Comprehensive Demo

Covers:
1. datetime module (dates, times, timezones, durations)
2. json module (reading/writing JSON data)
3. csv module (reading/writing CSV files)
"""

import datetime
import json
import csv
from pathlib import Path


# ========== DATETIME DEMO ==========
def demonstrate_datetime():
    """
    Demonstrates datetime module features:
    - Date and time objects
    - Timezone handling
    - Timedelta calculations
    - Formatting and parsing
    """
    print("\n=== DATETIME DEMO ===")

    # Current date and time
    now = datetime.datetime.now()
    print(f"Current datetime: {now}")

    # Specific date
    some_date = datetime.date(2023, 12, 25)
    print(f"Christmas 2023: {some_date}")

    # Time arithmetic
    time_diff = datetime.timedelta(days=7, hours=3)
    future_date = now + time_diff
    print(f"One week and 3 hours from now: {future_date}")

    # Timezone handling (requires pytz package)
    try:
        import pytz

        utc = pytz.UTC
        local_tz = pytz.timezone("Asia/Jakarta")
        localized = local_tz.localize(now)
        print(f"Localized time: {localized}")
    except ImportError:
        print("Note: Install pytz for timezone support")

    # Formatting
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted datetime: {formatted}")

    # Parsing
    parsed = datetime.datetime.strptime("2023-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
    print(f"Parsed datetime: {parsed}")


# ========== JSON DEMO ==========
def demonstrate_json():
    """
    Demonstrates json module features:
    - Serialization/deserialization
    - Working with files
    - Pretty printing
    """
    print("\n=== JSON DEMO ===")

    # Sample data structure
    data = {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Data Analysis"],
        "contact": {"email": "alice@example.com", "phone": "123-456-7890"},
    }

    # Serialization
    json_str = json.dumps(data, indent=2)
    print(f"JSON string:\n{json_str}")

    # Deserialization
    loaded_data = json.loads(json_str)
    print(f"Loaded data name: {loaded_data['name']}")

    # File operations
    json_file = Path("data.json")
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

    with open(json_file) as f:
        file_data = json.load(f)

    print(f"Data loaded from file: {file_data['contact']['email']}")

    # Clean up
    json_file.unlink()


# ========== CSV DEMO ==========
def demonstrate_csv():
    """
    Demonstrates csv module features:
    - Reading/writing CSV files
    - DictReader/DictWriter
    - Custom dialects
    """
    print("\n=== CSV DEMO ===")

    # Sample data
    employees = [
        {"name": "Alice", "department": "Engineering", "salary": 85000},
        {"name": "Bob", "department": "Marketing", "salary": 75000},
        {"name": "Charlie", "department": "Engineering", "salary": 90000},
    ]

    # Writing CSV
    csv_file = Path("employees.csv")
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "department", "salary"])
        writer.writeheader()
        writer.writerows(employees)

    # Reading CSV
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        print("Employee Data:")
        for row in reader:
            print(f"{row['name']}: {row['department']} (${row['salary']})")

    # Clean up
    csv_file.unlink()


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    print("=== PYTHON DATA FORMATS AND TIMES DEMO ===")
    demonstrate_datetime()
    demonstrate_json()
    demonstrate_csv()
    print("\n=== DEMO COMPLETE ===")
    print("Tip: Explore the generated files and modify the examples!")
