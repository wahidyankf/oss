---
title: '01 - Python Core Language Essentials'
date: 2025-04-17T07:20:00+07:00
draft: false
weight: 2
---

**Complexity: Easy (E)**

## 1.0 Introduction: Why This Matters for Data Engineering

As a data engineer, your primary job is to build robust systems that extract, transform, and load data reliably. Python has become the lingua franca of data engineering for good reasons:

- **Readability**: Python's clean syntax makes your code easy to understand and maintain
- **Versatility**: Python works with virtually all data sources and formats
- **Ecosystem**: Python's rich libraries cover every aspect of the data engineering lifecycle
- **Community**: Large community means solutions to common problems are readily available

The fundamentals you'll learn in this chapter form the foundation for all your future data engineering work. Consider how these core concepts translate directly to data tasks:

```mermaid
flowchart TD
    A[Data Engineering Workflow] --> B[Data Extraction]
    A --> C[Data Transformation]
    A --> D[Data Loading]

    B --> B1[Python Concepts Used]
    B1 --> B11[Functions - Extract APIs]
    B1 --> B12[Error Handling - Retry Logic]
    B1 --> B13[Data Structures - Store Results]

    C --> C1[Python Concepts Used]
    C1 --> C11[Control Flow - Filter Invalid Data]
    C1 --> C12[String Methods - Parse Text]
    C1 --> C13[Data Structures - Group Data]

    D --> D1[Python Concepts Used]
    D1 --> D11[Functions - DB Operations]
    D1 --> D12[Standard Library - Format Data]
    D1 --> D13[Data Types - Type Conversion]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B,C,D fill:#bbf,stroke:#336,stroke-width:1px
    style B1,C1,D1 fill:#ffd,stroke:#333,stroke-width:1px
    style B11,B12,B13,C11,C12,C13,D11,D12,D13 fill:#efe,stroke:#363,stroke-width:1px
```

This diagram illustrates how the Python fundamentals you'll learn directly enable essential data engineering tasks. Each concept has a practical application in building data pipelines.

Let's begin building your Python toolkit for data engineering!

## 1.1 Python Syntax and Data Types

### Variables and Assignment

Variables are containers for storing data values. In data engineering, you'll use variables to hold configuration settings, data records, and processing results.

```python
# Assign a value to a variable
user_id = 10  # An integer
revenue = 19.99  # A floating-point number
log_message = "Data pipeline completed"  # A string
is_successful = True  # A boolean

# Print variables to see their values
print("user_id:", user_id)  # user_id: 10
print("revenue:", revenue)  # revenue: 19.99
print("log_message:", log_message)  # log_message: Data pipeline completed
print("is_successful:", is_successful)  # is_successful: True

# Variables can be reassigned different values
user_id = "USR_010"  # Now user_id is a string
print("Updated user_id:", user_id)  # Updated user_id: USR_010
```

### Basic Data Types

Python has several built-in data types that you'll use constantly in data engineering:

```python
# Integers - whole numbers
record_count = 42
batch_size = 1000
print("Total records:", record_count * batch_size)  # Total records: 42000

# Floating-point numbers - numbers with decimal points
average_load_time = 1.25  # seconds
error_rate = 0.03  # 3%
print(f"Average load time: {average_load_time} seconds")  # Average load time: 1.25 seconds
print(f"Error rate: {error_rate * 100}%")  # Error rate: 3.0%

# Strings - text enclosed in quotes (single or double)
database_name = "customer_analytics"
query_status = 'completed'
print(f"Database '{database_name}' query {query_status}")  # Database 'customer_analytics' query completed

# Multi-line strings with triple quotes
sql_query = """
SELECT customer_id, SUM(order_total) as revenue
FROM orders
WHERE order_date >= '2023-01-01'
GROUP BY customer_id
"""
print("SQL Query:", sql_query)  # Prints the multi-line query

# Booleans - True or False values
is_production = True
needs_refresh = False
print("Is production environment?", is_production)  # Is production environment? True
print("Needs data refresh?", needs_refresh)  # Needs data refresh? False

# None - represents the absence of a value (null)
next_batch = None
print("Next batch:", next_batch)  # Next batch: None
print("Is next_batch None?", next_batch is None)  # Is next_batch None? True
```

### Basic Operators

Python supports various operators for computations and comparisons:

```python
# Arithmetic operators
records_per_day = 10000
days_processed = 3

total_records = records_per_day * days_processed
print("Total records processed:", total_records)  # Total records processed: 30000

# Division - regular vs. integer division
print("Regular division: 10 / 3 =", 10 / 3)  # Regular division: 10 / 3 = 3.3333333333333335
print("Integer division: 10 // 3 =", 10 // 3)  # Integer division: 10 // 3 = 3
print("Remainder (modulo): 10 % 3 =", 10 % 3)  # Remainder (modulo): 10 % 3 = 1

# Division is useful for data partitioning
records = 1000
partitions = 4
print(f"Each partition will process {records // partitions} records")  # Each partition will process 250 records
print(f"Remaining records: {records % partitions}")  # Remaining records: 0

# Comparison operators
throughput = 5000  # records per minute
sla_throughput = 4500  # SLA requirement
meets_sla = throughput >= sla_throughput
print("Meeting throughput SLA?", meets_sla)  # Meeting throughput SLA? True

# Logical operators
is_production = True
is_peak_hours = False

# AND operator - both must be True
should_optimize = is_production and is_peak_hours
print("Should optimize query?", should_optimize)  # Should optimize query? False

# OR operator - at least one must be True
should_log = is_production or is_peak_hours
print("Should log operation?", should_log)  # Should log operation? True

# NOT operator - reverses the boolean
is_maintenance_window = not is_peak_hours
print("Is maintenance window?", is_maintenance_window)  # Is maintenance window? True
```

### Common Error: Type Confusion

One of the most common errors in Python, especially in data processing, is confusion between data types:

```python
# Data often comes in as strings, even when representing numbers
record_count_str = "1000"
batch_size = 10

# Common error: treating a string as a number
try:
    # This multiplication doesn't perform as expected with a string
    total = record_count_str * batch_size
    print("This won't calculate properly:", total)  # This won't calculate properly: 10001000100010001000100010001000100010001000
except Exception as e:
    print("Error:", e)

# Correct approach: convert string to numeric type first
record_count = int(record_count_str)
total = record_count * batch_size
print("Correct calculation:", total)  # Correct calculation: 10000

# Another common error: forgetting to convert strings in calculations
metric1 = "10.5"
metric2 = "20.3"

# Incorrect: string concatenation instead of numerical addition
incorrect_sum = metric1 + metric2
print("Incorrect string concatenation:", incorrect_sum)  # Incorrect string concatenation: 10.520.3

# Correct: convert to float first
correct_sum = float(metric1) + float(metric2)
print("Correct numerical addition:", correct_sum)  # Correct numerical addition: 30.8
```

## 1.2 Control Flow

Control flow statements allow you to make decisions and repeat actions in your code, which is essential for data processing.

### Conditional Statements (if/elif/else)

```python
# Basic data validation
record_count = 45

if record_count > 1000:
    print("Large dataset detected, using batch processing")
elif record_count > 0:
    print("Normal dataset, using standard processing")  # This will print
else:
    print("No data found, skipping processing")

# Output: Normal dataset, using standard processing

# Validating a database connection
connection_string = "postgresql://user:password@localhost:5432/analytics"
is_active = True

if connection_string and is_active:  # Both must be True (non-empty string and True boolean)
    print("Database connection valid and active")  # This will print
else:
    print("Database connection invalid or inactive")

# Output: Database connection valid and active

# Complex condition for data quality check
error_rate = 0.03
warning_threshold = 0.05
error_threshold = 0.10

if error_rate >= error_threshold:
    status = "Error: Data quality below threshold"
elif error_rate >= warning_threshold:
    status = "Warning: Data quality concerns detected"
else:
    status = "Success: Data quality acceptable"

print(f"Data quality status: {status}")  # Data quality status: Success: Data quality acceptable
```

### For Loops

For loops allow you to iterate through collections, which is essential for processing datasets:

```python
# Processing a batch of records
batch_ids = [1001, 1002, 1003, 1004, 1005]
print("Processing batch records:")
for record_id in batch_ids:
    print(f"Processing record {record_id}")

# Output:
# Processing batch records:
# Processing record 1001
# Processing record 1002
# Processing record 1003
# Processing record 1004
# Processing record 1005

# Calculating total data size from a list of files
file_sizes = [2048, 4096, 1024, 8192, 512]  # sizes in KB
total_size = 0

for size in file_sizes:
    total_size += size

print(f"Total data size: {total_size} KB")  # Total data size: 15872 KB
print(f"Total data size: {total_size / 1024:.2f} MB")  # Total data size: 15.50 MB

# Extracting specific fields from records
customer_records = [
    {"id": 101, "name": "Acme Corp", "active": True, "balance": 45000},
    {"id": 102, "name": "Globex Inc", "active": False, "balance": 12000},
    {"id": 103, "name": "Initech", "active": True, "balance": 89000}
]

# Extract just the names of active customers
active_customer_names = []
for customer in customer_records:
    if customer["active"]:
        active_customer_names.append(customer["name"])

print("Active customers:", active_customer_names)  # Active customers: ['Acme Corp', 'Initech']

# Using range() to generate sequences of numbers
print("First 5 square numbers:")
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(f"{i} squared = {i**2}")

# Output:
# First 5 square numbers:
# 1 squared = 1
# 2 squared = 4
# 3 squared = 9
# 4 squared = 16
# 5 squared = 25

# Using enumerate() to get index and value - useful for batch processing
log_entries = ["Started ETL process", "Extracted 1000 records", "Transformed data", "Loaded into warehouse"]
print("Formatted log:")
for index, entry in enumerate(log_entries):
    print(f"[{index}] {entry}")

# Output:
# Formatted log:
# [0] Started ETL process
# [1] Extracted 1000 records
# [2] Transformed data
# [3] Loaded into warehouse
```

### While Loops

While loops run as long as a condition is true, useful for scenarios where you don't know the exact number of iterations:

```python
# Simulating a batch processing job
batch_size = 100
records_to_process = 340
processed_count = 0

print("Processing records in batches:")
batch_num = 0
while processed_count < records_to_process:
    # Calculate how many to process in this batch
    current_batch = min(batch_size, records_to_process - processed_count)
    processed_count += current_batch
    batch_num += 1
    print(f"Batch {batch_num}: Processed {current_batch} records. Total: {processed_count}/{records_to_process}")

# Output:
# Processing records in batches:
# Batch 1: Processed 100 records. Total: 100/340
# Batch 2: Processed 100 records. Total: 200/340
# Batch 3: Processed 100 records. Total: 300/340
# Batch 4: Processed 40 records. Total: 340/340

# Retry logic for an API connection
max_retries = 3
retry_count = 0
connected = False

print("\nAttempting API connection:")
while not connected and retry_count < max_retries:
    retry_count += 1
    print(f"Connection attempt {retry_count}...")

    # Simulate connection attempt (would normally be an API call)
    if retry_count == 3:  # Succeed on third attempt
        connected = True

    if not connected:
        print("  Connection failed, retrying...")

if connected:
    print("Successfully connected to API")
else:
    print("Failed to connect after maximum retries")

# Output:
# Attempting API connection:
# Connection attempt 1...
#   Connection failed, retrying...
# Connection attempt 2...
#   Connection failed, retrying...
# Connection attempt 3...
# Successfully connected to API
```

### Common Loop Errors

```python
# Common mistake: Modifying a list while iterating
records = [1, 2, 3, 4, 5]

print("Incorrect approach to filtering (bug):")
try:
    for record in records[:]:  # Using a slice to create a copy for demonstration
        if record % 2 == 0:  # Remove even numbers
            records.remove(record)  # WRONG: Modifies the list while iterating
        print(f"Current record: {record}, List: {records}")
except Exception as e:
    print(f"This can cause unexpected behavior: {e}")

# Output would be inconsistent and confusing - we're showing it with a copy
# to demonstrate the concept safely

# Correct approach
records = [1, 2, 3, 4, 5]
filtered_records = []

print("\nCorrect approach:")
for record in records:
    if record % 2 != 0:  # Keep odd numbers
        filtered_records.append(record)
    print(f"Current record: {record}, Filtered list so far: {filtered_records}")

print("Final filtered list:", filtered_records)  # Final filtered list: [1, 3, 5]

# Output:
# Correct approach:
# Current record: 1, Filtered list so far: [1]
# Current record: 2, Filtered list so far: [1]
# Current record: 3, Filtered list so far: [1, 3]
# Current record: 4, Filtered list so far: [1, 3]
# Current record: 5, Filtered list so far: [1, 3, 5]
# Final filtered list: [1, 3, 5]
```

### Performance Tip: Loop Efficiency

```python
# Performance tip: For very large datasets, be mindful of how you build results
import time

# Simulating large dataset processing
print("Processing efficiency demonstration:")

# Inefficient approach: Growing a list with many append operations
start_time = time.time()
inefficient_result = []
for i in range(100000):  # Smaller number for demonstration purpose
    inefficient_result.append(i)  # Append is efficient for individual items, but can be improved
inefficient_time = time.time() - start_time
print(f"Time for inefficient approach: {inefficient_time:.4f} seconds")

# More efficient: Pre-allocate if you know the size
start_time = time.time()
efficient_result = [0] * 100000  # Pre-allocate
for i in range(100000):
    efficient_result[i] = i  # Direct assignment to pre-allocated slot
efficient_time = time.time() - start_time
print(f"Time for efficient approach: {efficient_time:.4f} seconds")
print(f"Speedup factor: {inefficient_time/efficient_time:.2f}x")

# Output (will vary by machine):
# Processing efficiency demonstration:
# Time for inefficient approach: 0.0102 seconds
# Time for efficient approach: 0.0058 seconds
# Speedup factor: 1.76x
```

## 1.3 Functions

Functions are reusable blocks of code that perform specific tasks. In data engineering, they help organize data transformations, validations, and other operations.

### Defining and Calling Functions

```python
# Basic data validation function
def is_valid_record(record):
    """Check if a data record is valid.

    Args:
        record: Dictionary containing record data

    Returns:
        Boolean indicating if record is valid
    """
    if not record:  # Check if record exists
        return False

    # Check if required fields exist
    if "id" not in record or "timestamp" not in record:
        return False

    # Check if ID is positive
    if record["id"] <= 0:
        return False

    return True

# Test the validation function
test_record1 = {"id": 1001, "timestamp": "2023-01-15", "value": 42}
test_record2 = {"id": 0, "value": 42}  # Missing timestamp and invalid ID

print("Record 1 valid:", is_valid_record(test_record1))  # Record 1 valid: True
print("Record 2 valid:", is_valid_record(test_record2))  # Record 2 valid: False

# Function with multiple parameters and default values
def calculate_metrics(values, exclude_outliers=False, min_threshold=None, max_threshold=None):
    """
    Calculate basic statistics for a list of values.

    Args:
        values: List of numeric values
        exclude_outliers: Whether to exclude outlier values
        min_threshold: Minimum value to include
        max_threshold: Maximum value to include

    Returns:
        Dictionary of calculated metrics
    """
    if not values:
        return {"count": 0, "sum": 0, "avg": 0, "min": None, "max": None}

    # Filter values if needed
    filtered_values = []
    for value in values:
        # Apply filters
        if min_threshold is not None and value < min_threshold:
            continue
        if max_threshold is not None and value > max_threshold:
            continue
        filtered_values.append(value)

    # If we have no values after filtering
    if not filtered_values:
        return {"count": 0, "sum": 0, "avg": 0, "min": None, "max": None}

    # Calculate metrics
    total = sum(filtered_values)
    count = len(filtered_values)
    return {
        "count": count,
        "sum": total,
        "avg": total / count,
        "min": min(filtered_values),
        "max": max(filtered_values)
    }

# Test with different parameter combinations
data_points = [10, 15, 87, 45, 92, 3, 8, 56]

# Default parameters
basic_metrics = calculate_metrics(data_points)
print("\nBasic metrics:", basic_metrics)
# Basic metrics: {'count': 8, 'sum': 316, 'avg': 39.5, 'min': 3, 'max': 92}

# With filtering
filtered_metrics = calculate_metrics(data_points, min_threshold=10, max_threshold=90)
print("Filtered metrics:", filtered_metrics)
# Filtered metrics: {'count': 5, 'sum': 203, 'avg': 40.6, 'min': 10, 'max': 87}
```

### Function Return Values

```python
# Function that returns a simple value
def get_database_status(db_name):
    """
    Get the status of a database.

    Args:
        db_name: Database name to check

    Returns:
        String status code
    """
    # In real code, this would check an actual database
    statuses = {
        "customers": "online",
        "products": "maintenance",
        "orders": "online"
    }

    return statuses.get(db_name, "unknown")

db_status = get_database_status("customers")
print(f"Database status: {db_status}")  # Database status: online
unknown_status = get_database_status("inventory")
print(f"Unknown database status: {unknown_status}")  # Unknown database status: unknown

# Function that returns multiple values (as a tuple)
def parse_connection_string(conn_string):
    """
    Parse a database connection string into components.

    Args:
        conn_string: Connection string in format "db_type://user:pass@host:port/db_name"

    Returns:
        Tuple of (db_type, user, host, port, db_name)
    """
    # This is a simplified parser for demonstration
    if not conn_string or "//" not in conn_string:
        return (None, None, None, None, None)

    # Split protocol and rest
    parts = conn_string.split("://")
    db_type = parts[0]

    # Split credentials and location
    rest = parts[1]
    if "@" in rest:
        creds, location = rest.split("@", 1)
        if ":" in creds:
            user, _ = creds.split(":", 1)  # Don't expose the password
        else:
            user = creds
    else:
        user = None
        location = rest

    # Split host, port, db_name
    host_part, db_name = location.split("/", 1) if "/" in location else (location, "")
    if ":" in host_part:
        host, port = host_part.split(":")
        port = int(port)
    else:
        host = host_part
        port = None

    return (db_type, user, host, port, db_name)

# Test the parser
conn = "postgresql://data_user:secret@analytics.example.com:5432/metrics_db"
db_type, user, host, port, db_name = parse_connection_string(conn)
print(f"\nConnection details:")
print(f"Type: {db_type}, User: {user}, Host: {host}, Port: {port}, DB: {db_name}")
# Connection details:
# Type: postgresql, User: data_user, Host: analytics.example.com, Port: 5432, DB: metrics_db
```

### Function Scope

```python
# Understanding scope in data processing functions
total_record_count = 0  # Global variable

def process_batch(records):
    """Process a batch of records and update global count."""
    # This won't modify the global variable unless declared global
    # total_record_count += len(records)  # Would cause UnboundLocalError

    # Correct way to update global variable
    global total_record_count
    total_record_count += len(records)

    # Local variable for batch-specific counting
    error_count = 0
    for record in records:
        if not is_valid_record(record):
            error_count += 1

    return error_count

# Test with sample batches
batch1 = [{"id": 1, "timestamp": "2023-01-01"}, {"id": 2, "timestamp": "2023-01-02"}]
batch2 = [{"id": 3, "timestamp": "2023-01-03"}, {"id": 0}]  # Second record is invalid

print("\nProcessing batches:")
print(f"Batch 1 errors: {process_batch(batch1)}")  # Batch 1 errors: 0
print(f"Current total count: {total_record_count}")  # Current total count: 2

print(f"Batch 2 errors: {process_batch(batch2)}")  # Batch 2 errors: 1
print(f"Final total count: {total_record_count}")  # Final total count: 4

# Common error: Trying to access local variable from outside
def extract_fields(records, field_name):
    """Extract values of a specific field from records."""
    values = []
    for record in records:
        if field_name in record:
            values.append(record[field_name])
    return values

extracted_values = extract_fields(batch1, "timestamp")
print("\nExtracted timestamps:", extracted_values)  # Extracted timestamps: ['2023-01-01', '2023-01-02']

# This would cause an error - values only exists inside the function
# print(values)  # NameError: name 'values' is not defined
```

### Database-Specific Function Example

```python
def build_sql_query(table_name, columns=None, where_conditions=None, group_by=None, limit=None):
    """
    Build a SQL SELECT query with various conditions.

    Args:
        table_name: Table to query
        columns: List of columns to select, or None for all
        where_conditions: List of WHERE conditions
        group_by: List of columns to group by
        limit: Maximum number of rows to return

    Returns:
        SQL query string
    """
    # Build SELECT clause
    if columns:
        select_clause = f"SELECT {', '.join(columns)}"
    else:
        select_clause = "SELECT *"

    # Add FROM clause
    query = f"{select_clause} FROM {table_name}"

    # Add WHERE clause if needed
    if where_conditions:
        where_clause = " AND ".join(where_conditions)
        query += f" WHERE {where_clause}"

    # Add GROUP BY if needed
    if group_by:
        group_clause = ", ".join(group_by)
        query += f" GROUP BY {group_clause}"

    # Add LIMIT if needed
    if limit is not None:
        query += f" LIMIT {limit}"

    return query

# Test the query builder for different query types
print("\nSQL Query Examples:")

# Simple query
simple_query = build_sql_query("customers")
print(f"Simple query: {simple_query}")  # Simple query: SELECT * FROM customers

# Complex query
complex_query = build_sql_query(
    table_name="orders",
    columns=["customer_id", "SUM(order_total) as total_revenue"],
    where_conditions=["order_date >= '2023-01-01'", "status = 'completed'"],
    group_by=["customer_id"],
    limit=100
)
print(f"Complex query: {complex_query}")
# Complex query: SELECT customer_id, SUM(order_total) as total_revenue FROM orders WHERE order_date >= '2023-01-01' AND status = 'completed' GROUP BY customer_id LIMIT 100
```

## 1.4 Data Structures

Python has several built-in data structures to help organize data. Understanding their characteristics is crucial for effective data engineering.

### Lists

Lists are ordered, mutable collections that can hold items of different types. In data engineering, they're commonly used for storing records, batch processing, and intermediate results.

```python
# Creating a list of log entries
logs = ["ETL started", "Extraction complete", "Transformation complete", "Load complete"]
print("Log entries:", logs)  # Log entries: ['ETL started', 'Extraction complete', 'Transformation complete', 'Load complete']

# Accessing elements (indexing starts at 0)
first_log = logs[0]  # "ETL started"
last_log = logs[-1]  # "Load complete" (negative indexing starts from the end)
print("First log entry:", first_log)  # First log entry: ETL started
print("Last log entry:", last_log)   # Last log entry: Load complete

# Slicing a list [start:stop:step]
middle_logs = logs[1:3]  # ["Extraction complete", "Transformation complete"] (stop index is exclusive)
print("Middle log entries:", middle_logs)  # Middle log entries: ['Extraction complete', 'Transformation complete']

# Modifying lists
logs[1] = "Data extraction complete with 1000 records"  # Replace an element
print("After updating extraction log:", logs)
# After updating extraction log: ['ETL started', 'Data extraction complete with 1000 records', 'Transformation complete', 'Load complete']

logs.append("ETL process completed successfully")  # Add to the end
print("After appending completion message:", logs)
# After appending completion message: ['ETL started', 'Data extraction complete with 1000 records', 'Transformation complete', 'Load complete', 'ETL process completed successfully']

logs.insert(1, "Beginning extraction phase")  # Insert at specific position
print("After inserting phase message:", logs)
# After inserting phase message: ['ETL started', 'Beginning extraction phase', 'Data extraction complete with 1000 records', 'Transformation complete', 'Load complete', 'ETL process completed successfully']

removed_log = logs.pop()  # Remove and return the last element
print("Removed log:", removed_log)  # Removed log: ETL process completed successfully
print("Logs after pop():", logs)
# Logs after pop(): ['ETL started', 'Beginning extraction phase', 'Data extraction complete with 1000 records', 'Transformation complete', 'Load complete']

# Common list methods
data_samples = [45, 23, 78, 12, 56]
print("\nData samples:", data_samples)  # Data samples: [45, 23, 78, 12, 56]
print("Number of samples:", len(data_samples))  # Number of samples: 5
print("Minimum value:", min(data_samples))  # Minimum value: 12
print("Maximum value:", max(data_samples))  # Maximum value: 78
print("Sum of values:", sum(data_samples))  # Sum of values: 214
print("Average value:", sum(data_samples) / len(data_samples))  # Average value: 42.8

# Sorting lists
data_samples.sort()  # Sort in-place
print("Sorted samples:", data_samples)  # Sorted samples: [12, 23, 45, 56, 78]

data_samples.sort(reverse=True)  # Sort in descending order
print("Reverse sorted:", data_samples)  # Reverse sorted: [78, 56, 45, 23, 12]
```

### Dictionaries

Dictionaries are collections of key-value pairs, perfect for representing record structures and lookups in data engineering.

```python
# Creating a dictionary representing a database record
customer = {
    "customer_id": 1001,
    "name": "Acme Corporation",
    "industry": "Manufacturing",
    "active": True,
    "joined_date": "2022-08-15",
    "contact_info": {
        "email": "info@acme.example.com",
        "phone": "555-123-4567",
        "address": "123 Main St"
    }
}
print("Customer record:", customer)
# Customer record: {'customer_id': 1001, 'name': 'Acme Corporation', 'industry': 'Manufacturing', 'active': True, 'joined_date': '2022-08-15', 'contact_info': {'email': 'info@acme.example.com', 'phone': '555-123-4567', 'address': '123 Main St'}}

# Accessing values - essential for data processing
customer_name = customer["name"]
print("Customer name:", customer_name)  # Customer name: Acme Corporation

# Access nested dictionary
contact_email = customer["contact_info"]["email"]
print("Contact email:", contact_email)  # Contact email: info@acme.example.com

# Alternative access with .get() - safer when key might not exist
# Common in data processing where fields might be missing
status = customer.get("status", "unknown")  # Returns "unknown" as default
print("Status (which doesn't exist):", status)  # Status (which doesn't exist): unknown

# Modifying dictionaries
customer["active"] = False  # Change a value
print("After updating active status:", customer["active"])  # After updating active status: False

customer["last_order_date"] = "2023-02-28"  # Add a new key-value pair
print("After adding last order date:", customer["last_order_date"])  # After adding last order date: 2023-02-28

# Useful dictionary methods
print("\nDictionary keys:", customer.keys())  # Dictionary keys: dict_keys(['customer_id', 'name', 'industry', 'active', 'joined_date', 'contact_info', 'last_order_date'])
print("Dictionary values:", list(customer.values())[:3], "...")  # First 3 values for brevity

# Common data engineering pattern: counting occurrences
event_counts = {}
events = ["login", "search", "purchase", "login", "logout", "search", "login"]

for event in events:
    if event in event_counts:
        event_counts[event] += 1
    else:
        event_counts[event] = 1

print("\nEvent frequency counts:", event_counts)
# Event frequency counts: {'login': 3, 'search': 2, 'purchase': 1, 'logout': 1}

# Alternative using get() with default
event_counts_alt = {}
for event in events:
    event_counts_alt[event] = event_counts_alt.get(event, 0) + 1

print("Event counts (using get method):", event_counts_alt)
# Event counts (using get method): {'login': 3, 'search': 2, 'purchase': 1, 'logout': 1}
```

### Tuples

Tuples are ordered, immutable collections, useful for fixed data structures in data pipelines.

```python
# Using tuples for database connection parameters (fixed structure)
db_config = ("localhost", 5432, "analytics_db", "data_user", "secure_password")
print("Database configuration tuple:", db_config)  # Database configuration tuple: ('localhost', 5432, 'analytics_db', 'data_user', 'secure_password')

# Unpacking tuples - common in data engineering for returning multiple values
host, port, db_name, username, password = db_config
print(f"Connecting to {db_name} on {host}:{port}")  # Connecting to analytics_db on localhost:5432

# Tuples are immutable - cannot be changed after creation
try:
    db_config[0] = "new_host"  # This will cause an error
except TypeError as e:
    print("Error when trying to modify tuple:", e)  # Error when trying to modify tuple: 'tuple' object does not support item assignment

# Tuples in a list of records (common data structure)
data_points = [
    ("2023-01-01", 23.5, "sensor1"),
    ("2023-01-01", 22.8, "sensor2"),
    ("2023-01-02", 24.1, "sensor1"),
    ("2023-01-02", 23.2, "sensor2")
]

print("\nSensor readings:")
for date, temp, sensor in data_points:  # Unpacking in the loop
    print(f"{sensor} on {date}: {temp}°C")

# Output:
# Sensor readings:
# sensor1 on 2023-01-01: 23.5°C
# sensor2 on 2023-01-01: 22.8°C
# sensor1 on 2023-01-02: 24.1°C
# sensor2 on 2023-01-02: 23.2°C
```

### Sets

Sets are unordered collections of unique elements, useful for deduplication and membership testing - common operations in data engineering.

```python
# Using sets for deduplication (a common data cleaning operation)
log_sources = {"app-server-1", "database", "app-server-1", "load-balancer", "database", "cache"}
print("Unique log sources:", log_sources)  # Unique log sources: {'app-server-1', 'database', 'load-balancer', 'cache'}

# Check if an element exists - very efficient lookup
has_database_logs = "database" in log_sources
print("Have database logs?", has_database_logs)  # Have database logs? True

# Set operations for data analysis
system_a_users = {"user1", "user2", "user3", "user4", "user5"}
system_b_users = {"user3", "user4", "user5", "user6", "user7"}

# Users in both systems (common in data integration)
common_users = system_a_users & system_b_users  # Intersection
print("\nUsers in both systems:", common_users)  # Users in both systems: {'user3', 'user4', 'user5'}

# Users in either system (union)
all_users = system_a_users | system_b_users
print("Total unique users:", all_users)  # Total unique users: {'user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7'}

# Users only in system A (difference)
system_a_only = system_a_users - system_b_users
print("Users only in system A:", system_a_only)  # Users only in system A: {'user1', 'user2'}

# Users in exactly one system (symmetric difference)
exclusive_users = system_a_users ^ system_b_users
print("Users in exactly one system:", exclusive_users)  # Users in exactly one system: {'user1', 'user2', 'user6', 'user7'}

# Common data engineering example: Finding overlapping records
record_ids_batch1 = {101, 102, 103, 104, 105}
record_ids_batch2 = {104, 105, 106, 107}

# Check for duplicate processing
duplicates = record_ids_batch1 & record_ids_batch2
if duplicates:
    print(f"\nWarning: Found {len(duplicates)} duplicate records: {duplicates}")
    # Warning: Found 2 duplicate records: {104, 105}
```

### Database Record Example

Here's a more data engineering focused example using various data structures to represent database records and operations:

```python
# Database table schema representation using dictionaries
customer_table = {
    "name": "customers",
    "columns": [
        {"name": "id", "type": "INTEGER", "primary_key": True},
        {"name": "name", "type": "VARCHAR(100)", "nullable": False},
        {"name": "email", "type": "VARCHAR(100)", "unique": True},
        {"name": "signup_date", "type": "DATE", "nullable": True},
        {"name": "active", "type": "BOOLEAN", "default": True}
    ],
    "indexes": [
        {"name": "idx_customer_email", "columns": ["email"], "unique": True},
        {"name": "idx_customer_signup", "columns": ["signup_date"]}
    ]
}

# Sample data as a list of dictionaries (records)
customers = [
    {"id": 1001, "name": "Acme Corp", "email": "info@acme.example.com", "signup_date": "2022-01-15", "active": True},
    {"id": 1002, "name": "Globex Inc", "email": "contact@globex.example.com", "signup_date": "2022-03-20", "active": True},
    {"id": 1003, "name": "Initech", "email": "info@initech.example.com", "signup_date": "2022-02-28", "active": False}
]

# Print table schema
print("Table schema for:", customer_table["name"])
for column in customer_table["columns"]:
    constraints = []
    if column.get("primary_key"):
        constraints.append("PRIMARY KEY")
    if column.get("nullable") is False:
        constraints.append("NOT NULL")
    if column.get("unique"):
        constraints.append("UNIQUE")
    if "default" in column:
        constraints.append(f"DEFAULT {column['default']}")

    constraints_str = ", ".join(constraints)
    print(f"  {column['name']} {column['type']} {constraints_str}")

# Function to query our "database"
def query_customers(customers, where_condition=None):
    """Simple query function for our in-memory "database"."""
    results = []

    for customer in customers:
        # Apply where condition if provided
        if where_condition:
            condition_met = where_condition(customer)
            if not condition_met:
                continue

        results.append(customer)

    return results

# Query all active customers (using a lambda function as our where condition)
active_customers = query_customers(customers, lambda c: c["active"])
print("\nActive customers:")
for customer in active_customers:
    print(f"  {customer['id']}: {customer['name']} ({customer['email']})")

# Query by signup date range
def signup_in_q1_2022(customer):
    """Check if customer signed up in Q1 2022."""
    signup = customer["signup_date"]
    return signup >= "2022-01-01" and signup <= "2022-03-31"

q1_signups = query_customers(customers, signup_in_q1_2022)
print("\nCustomers who signed up in Q1 2022:")
for customer in q1_signups:
    print(f"  {customer['name']} - {customer['signup_date']}")

# Output (partial):
# Table schema for: customers
#   id INTEGER PRIMARY KEY
#   name VARCHAR(100) PRIMARY KEY, NOT NULL
#   email VARCHAR(100) UNIQUE, NOT NULL
#   signup_date DATE
#   active BOOLEAN DEFAULT True
#
# Active customers:
#   1001: Acme Corp (info@acme.example.com)
#   1002: Globex Inc (contact@globex.example.com)
#
# Customers who signed up in Q1 2022:
#   Acme Corp - 2022-01-15
#   Globex Inc - 2022-03-20
#   Initech - 2022-02-28
```

## 1.5 String Manipulation

Strings are sequences of characters, and Python provides many ways to work with them. String manipulation is essential in data engineering for parsing, formatting, and generating reports.

### String Basics

```python
# String creation with different quotes - useful for SQL queries and file paths
sql_query = 'SELECT * FROM customers WHERE signup_date > "2023-01-01"'
file_path = "C:\\data\\exports\\customers.csv"  # Note the escaped backslashes
multi_line_query = """
SELECT
    customer_id,
    COUNT(*) as order_count,
    SUM(order_total) as total_revenue
FROM
    orders
WHERE
    order_date >= '2023-01-01'
GROUP BY
    customer_id
"""

print("SQL query:", sql_query)
print("File path:", file_path)
print("Multi-line query:", multi_line_query)

# String concatenation - common in dynamic SQL generation
table_name = "customers"
where_clause = "active = true"
limit_value = 100

# Building a query dynamically
dynamic_query = "SELECT * FROM " + table_name + " WHERE " + where_clause + " LIMIT " + str(limit_value)
print("\nDynamically built query:", dynamic_query)
# Dynamically built query: SELECT * FROM customers WHERE active = true LIMIT 100

# String repetition - useful for report formatting
separator_line = "-" * 40
print(separator_line)  # Prints a line of 40 hyphens

# String indexing and slicing
timestamp = "2023-03-15T14:30:45.123Z"
date_part = timestamp[:10]  # "2023-03-15"
time_part = timestamp[11:19]  # "14:30:45"

print("Full timestamp:", timestamp)
print("Date part:", date_part)
print("Time part:", time_part)
```

### String Methods

```python
# Common string methods for data cleaning and transformation
log_entry = "  [ERROR] Database connection failed: timeout after 30s  "
print("Original log entry:", repr(log_entry))  # Shows whitespace with repr()
# Original log entry: '  [ERROR] Database connection failed: timeout after 30s  '

# Removing whitespace - essential for data cleaning
cleaned_entry = log_entry.strip()
print("After strip():", repr(cleaned_entry))  # After strip(): '[ERROR] Database connection failed: timeout after 30s'

# Case conversion - helpful for standardization
standardized_entry = cleaned_entry.upper()
print("Uppercase:", standardized_entry)  # Uppercase: [ERROR] DATABASE CONNECTION FAILED: TIMEOUT AFTER 30S

# Finding and replacing - common in data transformation
error_type = "ERROR"
position = cleaned_entry.find(error_type)
print(f"Position of '{error_type}':", position)  # Position of 'ERROR': 1

# Replace keywords or fix common typos
fixed_entry = cleaned_entry.replace("ERROR", "CRITICAL")
print("After replacement:", fixed_entry)  # After replacement: [CRITICAL] Database connection failed: timeout after 30s

# Splitting strings - common for parsing log entries and CSV data
parts = cleaned_entry.split(":")
print("\nSplit by ':':", parts)
# Split by ':': ['[ERROR] Database connection failed', ' timeout after 30s']

# Common pattern: Extracting log level from a standard log format
if cleaned_entry.startswith("["):
    log_level = cleaned_entry[1:cleaned_entry.find("]")]
    message = cleaned_entry[cleaned_entry.find("]")+2:]  # +2 to skip "] "
    print(f"Log level: {log_level}, Message: {message}")
    # Log level: ERROR, Message: Database connection failed: timeout after 30s

# Joining strings - useful for building CSV lines or combining path elements
fields = ["2023-03-15", "SYSTEM", "Database", "Connection established"]
log_line = " | ".join(fields)
print("\nJoined log line:", log_line)
# Joined log line: 2023-03-15 | SYSTEM | Database | Connection established

# Common data cleaning: Handling inconsistent field separators
raw_data = "customer_id=1001;name=Acme Corp;  status=active"
# First, standardize separators
standardized = raw_data.replace(";", ",").replace("=", ":")
print("Standardized format:", standardized)
# Standardized format: customer_id:1001,name:Acme Corp,  status:active

# Then parse into key-value pairs
field_pairs = standardized.split(",")
record = {}
for pair in field_pairs:
    if ":" in pair:
        key, value = pair.split(":", 1)
        record[key.strip()] = value.strip()

print("Parsed record:", record)
# Parsed record: {'customer_id': '1001', 'name': 'Acme Corp', 'status': 'active'}
```

### f-strings (formatted string literals)

f-strings provide an easy way to embed expressions inside string literals, extremely useful for report generation and log formatting.

```python
# Basic f-string usage with database fields
record_id = 1001
status = "active"
last_updated = "2023-03-15"

log_message = f"Record {record_id} is {status}, last updated on {last_updated}"
print(log_message)  # Record 1001 is active, last updated on 2023-03-15

# F-strings with expressions - useful for reporting
row_count = 45678
batch_size = 1000
estimated_batches = (row_count + batch_size - 1) // batch_size  # Ceiling division

progress_report = f"""
Data Processing Summary:
=======================
Total records:     {row_count:,}
Batch size:        {batch_size:,}
Estimated batches: {estimated_batches:,}
Completion:        {(row_count / 50000) * 100:.1f}%
"""
print(progress_report)
# Data Processing Summary:
# =======================
# Total records:     45,678
# Batch size:        1,000
# Estimated batches: 46
# Completion:        91.4%

# F-strings with dictionaries - perfect for record formatting
user = {
    "id": "user123",
    "name": "Alice Johnson",
    "role": "Data Analyst",
    "access_level": 3,
    "last_login": "2023-03-14T09:23:51Z"
}

user_info = f"""
USER PROFILE: {user['name']}
------------------------
ID:          {user['id']}
Role:        {user['role']}
Access:      {'Admin' if user['access_level'] >= 5 else 'Standard'}
Last Login:  {user['last_login']}
"""
print(user_info)
# USER PROFILE: Alice Johnson
# ------------------------
# ID:          user123
# Role:        Data Analyst
# Access:      Standard
# Last Login:  2023-03-14T09:23:51Z

# Formatting numbers in different ways
value = 123456.78
print(f"Default:       {value}")           # Default:       123456.78
print(f"With commas:   {value:,}")         # With commas:   123,456.78
print(f"Two decimals:  {value:.2f}")       # Two decimals:  123456.78
print(f"Percentage:    {value/1000000:.2%}")  # Percentage:    12.35%
```

## 1.6 Standard Library Modules

Python's standard library provides many useful modules for common tasks. Here are some essential ones for data engineering:

### Basic Import Syntax

```python
# Importing an entire module
import math

# Now we can use functions from the math module with dot notation
result = math.sqrt(16)
print(f"The square root of 16 is: {result}")  # The square root of 16 is: 4.0

# We can also use constants from the module
print(f"The value of pi is approximately: {math.pi}")  # The value of pi is approximately: 3.141592653589793
```

### Importing Specific Items

```python
# Importing specific functions or constants from a module
from math import sqrt, pi

# Now we can use these directly without the module name
result = sqrt(16)
print(f"The square root of 16 is: {result}")  # The square root of 16 is: 4.0
print(f"The value of pi is approximately: {pi}")  # The value of pi is approximately: 3.141592653589793
```

### Renaming Imports

```python
# Renaming modules or functions during import
import math as m
from datetime import datetime as dt

# Now we use the shorter names
print(f"The square root of 25 is: {m.sqrt(25)}")  # The square root of 25 is: 5.0
print(f"The current time is: {dt.now().strftime('%H:%M:%S')}")  # The current time is: 14:35:22  (time will vary)
```

### Common Modules for Data Engineering

```python
# The datetime module for working with dates and times
from datetime import datetime, timedelta

current_time = datetime.now()
print(f"Current time: {current_time}")  # Current time: 2023-08-15 14:36:45.123456 (will vary)

yesterday = current_time - timedelta(days=1)
print(f"Yesterday: {yesterday}")  # Yesterday: 2023-08-14 14:36:45.123456 (will vary)

# Format dates for output
formatted_date = current_time.strftime("%Y-%m-%d")
print(f"Formatted date: {formatted_date}")  # Formatted date: 2023-08-15 (will vary)

# Parse date strings
date_str = "2023-01-15"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")  # Parsed date: 2023-01-15 00:00:00

# The os module for interacting with the operating system
import os

# Get the current working directory
cwd = os.getcwd()
print(f"\nCurrent working directory: {cwd}")  # Current working directory: /your/current/directory

# List files in the current directory (showing first 3)
files = os.listdir('.')
print(f"Files in current directory: {files[:3] if len(files) > 3 else files}")

# Join paths in a platform-independent way
data_dir = os.path.join("data", "processed", "2023")
print(f"Platform-independent path: {data_dir}")  # Platform-independent path: data/processed/2023

# The math module for mathematical operations
import math

# Calculate how many batches we'll need (ceiling division)
total_records = 1000
batch_size = 32
num_batches = math.ceil(total_records / batch_size)
print(f"\nProcessing {total_records} records in batches of {batch_size}:")
print(f"Total batches needed: {num_batches}")  # Total batches needed: 32

# Statistical functions
values = [28.5, 32.1, 29.7, 30.5, 27.8]
average = sum(values) / len(values)
variance = sum((x - average) ** 2 for x in values) / len(values)
std_dev = math.sqrt(variance)

print(f"\nStatistics for data sample:")
print(f"Average: {average:.2f}")  # Average: 29.72
print(f"Standard deviation: {std_dev:.2f}")  # Standard deviation: 1.60
```

### Import Best Practices

1. **Place imports at the top of the file**: Makes dependencies clear
2. **Group imports**: Standard library first, then third-party modules, then local modules
3. **Avoid `from module import *`**: Makes it unclear where functions come from
4. **Use specific imports**: Only import what you need for cleaner namespace

### Database-Specific Example

```python
# Building a database URL using components
import os
from urllib.parse import quote_plus  # For handling special characters in URLs

def build_database_url(db_type, host, port, database, user=None, password=None):
    """
    Build a database URL string.

    Args:
        db_type: Database type (e.g., postgresql, mysql)
        host: Database host
        port: Database port
        database: Database name
        user: Username (optional)
        password: Password (optional)

    Returns:
        URL string for database connection
    """
    # Build authentication part if credentials are provided
    auth = ""
    if user:
        if password:
            # Quote password to handle special characters
            auth = f"{user}:{quote_plus(password)}@"
        else:
            auth = f"{user}@"

    # Assemble the URL
    url = f"{db_type}://{auth}{host}:{port}/{database}"
    return url

# Example usage
host = "db.example.com"
database = "customer_data"
user = "db_user"
password = "Secret@123"  # In real code, get from environment or secure storage

# Build and print the URL (masking password)
url = build_database_url("postgresql", host, 5432, database, user, password)
safe_url = url.replace(quote_plus(password), "******")
print(f"\nDatabase URL: {safe_url}")
# Database URL: postgresql://db_user:******@db.example.com:5432/customer_data

# In production, you'd typically get credentials from environment variables
def get_db_url_from_env():
    """Get database URL from environment variables."""
    db_type = os.environ.get("DB_TYPE", "postgresql")
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    database = os.environ.get("DB_NAME", "app")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")

    return build_database_url(db_type, host, port, database, user, password)

# We won't actually run this in our example as it depends on environment variables
print("In production, use environment variables for database credentials.")
```

## 1.7 Common Troubleshooting Guide

When working with Python, especially in data engineering contexts, you'll encounter common errors. Here's a quick reference for troubleshooting:

### Syntax Errors

| Problem                                          | Possible Cause                         | Solution                                                    |
| ------------------------------------------------ | -------------------------------------- | ----------------------------------------------------------- |
| `SyntaxError: invalid syntax`                    | Missing parentheses, quotes, or colons | Check line for missing syntax elements                      |
| `IndentationError`                               | Inconsistent indentation               | Use consistent indentation (4 spaces per level recommended) |
| `SyntaxError: EOL while scanning string literal` | Unclosed string (missing quote)        | Ensure all strings have closing quotes                      |

### Type Errors

| Problem                                                  | Possible Cause                                        | Solution                                                        |
| -------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------- |
| `TypeError: can only concatenate str (not "int") to str` | Mixing strings and numbers                            | Convert numbers to strings before concatenation (`str(number)`) |
| `TypeError: 'NoneType' object is not subscriptable`      | Trying to index None as if it were a list or dict     | Check if variable is None before indexing                       |
| `TypeError: 'dict' object is not callable`               | Using parentheses with dictionary instead of brackets | Use square brackets for dict access: `dict_var[key]`            |

### Logic Errors

| Problem                  | Possible Cause                         | Solution                                                         |
| ------------------------ | -------------------------------------- | ---------------------------------------------------------------- |
| Unexpected output values | Logic error in calculations            | Add print statements to debug calculations step by step          |
| Infinite loop            | Loop condition never becomes False     | Ensure loop has a proper exit condition                          |
| List not being modified  | Creating new list instead of modifying | Use in-place methods (append, extend) or assign back to variable |

### Performance Issues

| Problem                            | Possible Cause                        | Solution                                                |
| ---------------------------------- | ------------------------------------- | ------------------------------------------------------- |
| Script runs slowly with large data | Inefficient loops or algorithms       | Use list comprehensions, more efficient data structures |
| Memory usage grows over time       | Accumulating data without cleaning up | Process data in chunks, avoid storing entire dataset    |
| Slow string building in loops      | Using += for string concatenation     | Use list of strings and join() at the end               |

## 1.8 Performance Considerations for Data Engineering

When processing large volumes of data, performance becomes critical. Here are key considerations:

### Efficient List Operations

```python
# Benchmark different list creation approaches
import time

# Measure performance of different approaches
def benchmark_list_creation(size):
    """Compare different ways to create a list of squares."""
    print(f"Benchmarking list creation methods for {size} elements:")

    # Approach 1: Growing a list with append in loop
    start = time.time()
    result1 = []
    for i in range(size):
        result1.append(i ** 2)
    time1 = time.time() - start
    print(f"  Append in loop:     {time1:.6f} seconds")

    # Approach 2: Pre-allocate and assign
    start = time.time()
    result2 = [0] * size
    for i in range(size):
        result2[i] = i ** 2
    time2 = time.time() - start
    print(f"  Pre-allocate:       {time2:.6f} seconds")

    # Approach 3: List comprehension
    start = time.time()
    result3 = [i ** 2 for i in range(size)]
    time3 = time.time() - start
    print(f"  List comprehension: {time3:.6f} seconds")

    return time1, time2, time3

# Run benchmark with moderate size for demonstration
times = benchmark_list_creation(100000)

# Calculate relative performance
fastest = min(times)
print("\nRelative performance (lower is better):")
print(f"  Append in loop:     {times[0]/fastest:.2f}x")
print(f"  Pre-allocate:       {times[1]/fastest:.2f}x")
print(f"  List comprehension: {times[2]/fastest:.2f}x")

# Output (will vary by system):
# Benchmarking list creation methods for 100000 elements:
#   Append in loop:     0.012345 seconds
#   Pre-allocate:       0.009876 seconds
#   List comprehension: 0.005432 seconds
#
# Relative performance (lower is better):
#   Append in loop:     2.27x
#   Pre-allocate:       1.82x
#   List comprehension: 1.00x
```

### Dictionary Lookups vs. List Searches

```python
import time
import random

# Create test data
size = 10000
test_data = list(range(size))
random.shuffle(test_data)  # Randomize order

# Create a dictionary for lookups
lookup_dict = {value: index for index, value in enumerate(test_data)}

# Define a function to find a value in a list
def find_in_list(data_list, value):
    for item in data_list:
        if item == value:
            return True
    return False

# Benchmark lookups
def benchmark_lookups(num_lookups):
    """Compare dictionary lookups vs list searches."""
    print(f"Benchmarking {num_lookups} lookups in list vs dictionary:")

    # Generate lookup values (mix of hits and misses)
    lookup_values = [random.randint(0, size * 2) for _ in range(num_lookups)]

    # List search
    start = time.time()
    list_results = [find_in_list(test_data, value) for value in lookup_values]
    list_time = time.time() - start
    print(f"  List search time:   {list_time:.6f} seconds")

    # Dictionary lookup
    start = time.time()
    dict_results = [value in lookup_dict for value in lookup_values]
    dict_time = time.time() - start
    print(f"  Dict lookup time:   {dict_time:.6f} seconds")
    print(f"  Dictionary is {list_time/dict_time:.1f}x faster")

    return list_time, dict_time

# Run benchmark
benchmark_lookups(1000)

# Output (will vary by system):
# Benchmarking 1000 lookups in list vs dictionary:
#   List search time:   0.112345 seconds
#   Dict lookup time:   0.000321 seconds
#   Dictionary is 349.7x faster

print("\nKey Data Engineering Takeaway:")
print("Use dictionaries for lookups when you have a large collection and need to frequently check if values exist.")
```

### Memory Management

```python
# Python's memory usage can be a concern when processing large datasets
import sys

# Demonstrate memory usage of different data structures
integers = list(range(10000))
floats = [float(i) for i in range(10000)]
strings = [str(i) for i in range(10000)]

print("Memory usage comparison:")
print(f"  List of 10000 integers: {sys.getsizeof(integers)} bytes")
print(f"  List of 10000 floats:   {sys.getsizeof(floats)} bytes")
print(f"  List of 10000 strings:  {sys.getsizeof(strings)} bytes")

# Note that getsizeof doesn't account for the size of elements themselves
# Let's check a few individual elements
print("\nIndividual element sizes:")
print(f"  Integer (42):        {sys.getsizeof(42)} bytes")
print(f"  Float (42.0):        {sys.getsizeof(42.0)} bytes")
print(f"  String ('42'):       {sys.getsizeof('42')} bytes")
print(f"  String ('hello'):    {sys.getsizeof('hello')} bytes")

print("\nMemory Management Tips:")
print("1. Process large datasets in chunks rather than loading everything into memory")
print("2. Use generators instead of lists when possible to avoid storing all data at once")
print("3. Consider specialized libraries like NumPy for numerical data")
print("4. Release references to large objects when no longer needed")
```

## 1.9 Micro-Project: Sales Data Analyzer

In this micro-project, we'll analyze sales data by creating a Python script that calculates key metrics from a dataset.

### Project Requirements

1. Read a dataset containing sales records
2. Calculate key metrics:
   - Total sales
   - Average order value
   - Top selling product
3. Handle basic data cleaning and validation
4. Generate formatted output showing the results

### Acceptance Criteria

- Script runs without errors when provided with sample data
- Correctly calculates all required statistics
- Properly handles edge cases (missing data, invalid entries)
- Uses appropriate Python data structures (lists, dictionaries)
- Includes comments explaining the code's functionality
- Produces readable, formatted output

### Common Pitfalls and Solutions

1. **String vs. numeric data confusion**:

   - Remember that data in files or user input is often stored as strings
   - Convert strings to numeric types before performing calculations
   - Use explicit conversion: `int()`, `float()`

2. **Not checking for invalid data**:

   - Always verify data is valid before using it in calculations
   - Check for empty strings, zero quantities, or values that can't be converted to numbers

3. **Using incorrect aggregation logic**:
   - Pay attention to how totals and averages should be calculated
   - For average order value, divide total revenue by number of orders, not number of items

### Implementation

First, let's create a sample dataset:

```python
# Sample sales data (normally this would come from a CSV file)
# Format: [order_id, product_name, quantity, price_per_unit, date]
sales_data = [
    ["1001", "Laptop", "2", "999.99", "2023-01-15"],
    ["1002", "Mouse", "10", "24.99", "2023-01-16"],
    ["1003", "Keyboard", "5", "49.99", "2023-01-16"],
    ["1004", "Monitor", "3", "149.99", "2023-01-17"],
    ["1005", "Laptop", "1", "999.99", "2023-01-18"],
    ["1006", "Headphones", "4", "59.99", "2023-01-18"],
    ["1007", "Mouse", "5", "24.99", "2023-01-19"],
    ["1008", "", "2", "29.99", "2023-01-19"],  # Missing product name
    ["1009", "Keyboard", "0", "49.99", "2023-01-20"],  # Zero quantity
    ["1010", "Monitor", "2", "invalid_price", "2023-01-20"],  # Invalid price
    ["1011", "Laptop", "1", "899.99", "2023-01-21"]
]

print("Sample of sales data (first 3 records):")
for i in range(3):
    print(f"  Record {i+1}: {sales_data[i]}")
# Sample of sales data (first 3 records):
#   Record 1: ['1001', 'Laptop', '2', '999.99', '2023-01-15']
#   Record 2: ['1002', 'Mouse', '10', '24.99', '2023-01-16']
#   Record 3: ['1003', 'Keyboard', '5', '49.99', '2023-01-16']
```

Now, let's write the analysis function:

```python
def analyze_sales_data(sales_data):
    """
    Analyze the provided sales data and return key metrics.

    Args:
        sales_data: A list of sales records

    Returns:
        A dictionary containing calculated metrics
    """
    # Initialize variables to track metrics
    total_sales = 0
    valid_orders = 0
    product_sales = {}  # Dictionary to track sales by product

    # Process each sales record
    for record in sales_data:
        order_id, product_name, quantity_str, price_str, date = record

        # Basic data validation
        if not product_name:  # Check for missing product name
            print(f"Warning: Missing product name in order {order_id}. Skipping.")
            continue

        # Check and convert quantity
        try:
            quantity = int(quantity_str)
        except ValueError:
            print(f"Warning: Invalid quantity in order {order_id}. Skipping.")
            continue

        # Skip records with zero or negative quantity
        if quantity <= 0:
            print(f"Warning: Zero or negative quantity in order {order_id}. Skipping.")
            continue

        # Check and convert price
        try:
            price = float(price_str)
        except ValueError:
            print(f"Warning: Invalid price format in order {order_id}. Skipping.")
            continue

        # Calculate the order value
        order_value = quantity * price

        # Update total sales
        total_sales += order_value
        valid_orders += 1

        # Update product sales dictionary
        if product_name in product_sales:
            product_sales[product_name] += order_value
        else:
            product_sales[product_name] = order_value

    # Calculate the average order value
    if valid_orders > 0:
        average_order_value = total_sales / valid_orders
    else:
        average_order_value = 0

    # Find the top selling product
    top_product = ""
    top_product_sales = 0

    for product, sales in product_sales.items():
        if sales > top_product_sales:
            top_product = product
            top_product_sales = sales

    # Return the calculated metrics
    return {
        "total_sales": total_sales,
        "average_order_value": average_order_value,
        "valid_orders": valid_orders,
        "top_product": top_product,
        "top_product_sales": top_product_sales,
        "product_sales": product_sales
    }
```

Let's create a helper function to format currency values:

```python
def format_as_currency(amount):
    """Format a number as currency with $ symbol and 2 decimal places."""
    return f"${amount:.2f}"
```

Finally, let's run the analysis and display the results:

```python
# Analyze the sales data
print("\nAnalyzing sales data...")
results = analyze_sales_data(sales_data)

# Display the results
print("\nAnalysis Results:")
print(f"Total Sales: {format_as_currency(results['total_sales'])}")  # e.g., Total Sales: $4,419.70
print(f"Number of Valid Orders: {results['valid_orders']}")          # e.g., Number of Valid Orders: 8
print(f"Average Order Value: {format_as_currency(results['average_order_value'])}")  # e.g., Average Order Value: $552.46

print(f"\nTop Selling Product: {results['top_product']}")  # e.g., Top Selling Product: Laptop
print(f"Top Product Sales: {format_as_currency(results['top_product_sales'])}")  # e.g., Top Product Sales: $2,899.97

print("\nSales by Product:")
for product, sales in sorted(results["product_sales"].items()):
    print(f"  - {product}: {format_as_currency(sales)}")
# Sales by Product:
#   - Headphones: $239.96
#   - Keyboard: $249.95
#   - Laptop: $2,899.97
#   - Monitor: $449.97
#   - Mouse: $374.85

# Generate a formatted report
report = f"""
SALES DATA ANALYSIS REPORT
===========================

Total Sales: {format_as_currency(results["total_sales"])}
Number of Valid Orders: {results["valid_orders"]}
Average Order Value: {format_as_currency(results["average_order_value"])}

Top Selling Product: {results["top_product"]}
Top Product Sales: {format_as_currency(results["top_product_sales"])}

Sales by Product:
"""

# Add each product's sales to the report
for product, sales in sorted(results["product_sales"].items()):
    report += f"  - {product}: {format_as_currency(sales)}\n"

# Print the report
print("\nFinal formatted report:")
print(report)
"""
Final formatted report:

SALES DATA ANALYSIS REPORT
===========================

Total Sales: $4,214.70
Number of Valid Orders: 8
Average Order Value: $526.84

Top Selling Product: Laptop
Top Product Sales: $2,899.97

Sales by Product:
  - Headphones: $239.96
  - Keyboard: $249.95
  - Laptop: $2,899.97
  - Monitor: $449.97
  - Mouse: $374.85
"""
```

### How This Differs from Production-Grade Solutions

In a real-world data engineering scenario, our solution would differ in several ways:

1. **Data Source**:

   - Production: Data would be read from files, databases, or APIs
   - Micro-project: Using in-memory data

2. **Error Handling**:

   - Production: Comprehensive error handling with detailed logging
   - Micro-project: Basic warnings printed to console

3. **Performance Optimization**:

   - Production: Optimized for large datasets using efficient algorithms
   - Micro-project: Simple loops and basic data structures

4. **Output Formats**:

   - Production: Multiple output formats (JSON, CSV, database) and dashboards
   - Micro-project: Simple console output and text report

5. **Monitoring**:
   - Production: Metrics on processing time, error rates, and data quality
   - Micro-project: No monitoring implementation

### How to Run and Test the Solution

To run this solution:

1. Copy the entire code (all sections) to a Python file (e.g., `sales_analyzer.py`)
2. Run the file using Python: `python sales_analyzer.py`
3. The script will process the sample data, display warnings for invalid entries, and generate a formatted report of the sales metrics

To test with different data:

- Modify the `sales_data` list to include different products, quantities, and prices
- Add more test cases with invalid data to verify error handling
- Check if the calculations change appropriately with the modified data

## 1.10 Practice Exercises

Reinforce your Python fundamentals with these exercises:

### Exercise 1: Basic Data Types and Functions

Create a function to calculate the total price of items in a shopping cart:

- Takes parameters for a list of prices and a tax rate
- Returns the total including tax
- Test it with different inputs

### Exercise 2: Data Transformation

Write a function that:

- Takes a list of product dictionaries (each with 'name' and 'price' keys)
- Returns a list of only the products with prices greater than $50
- Use a traditional for loop with appropriate conditionals

### Exercise 3: Data Structures

Create a program that tracks daily sales using:

- A dictionary with dates as keys
- Lists of products sold as values
- Functions to add sales and calculate daily totals

### Exercise 4: Standard Library Challenge

Write a program using the datetime module that:

- Calculates and prints the current day of the week
- Determines the number of days until the end of the current month
- Formats the current date in "Month Day, Year" format

### Challenge Exercise: Enhanced Sales Analyzer

Extend the Sales Data Analyzer micro-project to:

- Create a filtered list of valid sales records using traditional loops
- Group sales by product using a dictionary
- Format the output using string formatting

## 1.11 Exercise Solutions

### Solution to Exercise 1: Basic Data Types and Functions

```python
def calculate_cart_total(prices, tax_rate):
    """
    Calculate the total price of items including tax.

    Args:
        prices: A list of prices
        tax_rate: The tax rate as a decimal (e.g., 0.08 for 8%)

    Returns:
        The total price including tax
    """
    # Calculate subtotal by adding all prices
    subtotal = 0
    for price in prices:
        subtotal = subtotal + price

    # Calculate tax amount
    tax_amount = subtotal * tax_rate

    # Calculate total
    total = subtotal + tax_amount

    return total

# Test with different inputs
cart1 = [10.99, 24.50, 5.95]
tax_rate1 = 0.08  # 8% tax

cart2 = [199.99, 99.50, 50.00, 17.85]
tax_rate2 = 0.06  # 6% tax

# Calculate and display results
total1 = calculate_cart_total(cart1, tax_rate1)
print(f"Cart 1 Items: {cart1}")  # Cart 1 Items: [10.99, 24.5, 5.95]
print(f"Tax Rate: {tax_rate1 * 100}%")  # Tax Rate: 8.0%
print(f"Total with tax: ${total1:.2f}")  # Total with tax: $44.80

total2 = calculate_cart_total(cart2, tax_rate2)
print(f"\nCart 2 Items: {cart2}")  # Cart 2 Items: [199.99, 99.5, 50.0, 17.85]
print(f"Tax Rate: {tax_rate2 * 100}%")  # Tax Rate: 6.0%
print(f"Total with tax: ${total2:.2f}")  # Total with tax: $389.58
```

### Solution to Exercise 2: Data Transformation

```python
def find_expensive_products(products, min_price):
    """
    Find products with prices greater than the minimum price using a traditional loop.

    Args:
        products: A list of product dictionaries with 'name' and 'price' keys
        min_price: The minimum price threshold

    Returns:
        A list of products with prices greater than min_price
    """
    expensive_products = []

    for product in products:
        if product["price"] > min_price:
            expensive_products.append(product)

    return expensive_products

# Test data
product_list = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 24.99},
    {"name": "Keyboard", "price": 49.99},
    {"name": "Monitor", "price": 149.99},
    {"name": "Headphones", "price": 79.99}
]

# Find products over $50
min_price = 50.0

# Using traditional loop
expensive_products = find_expensive_products(product_list, min_price)
print(f"Products over ${min_price}:")
for product in expensive_products:
    print(f"  - {product['name']}: ${product['price']}")
# Products over $50.0:
#   - Laptop: $999.99
#   - Monitor: $149.99
#   - Headphones: $79.99

# Count expensive products
num_expensive = len(expensive_products)
print(f"\nNumber of products over ${min_price}: {num_expensive}")
# Number of products over $50.0: 3
```

### Solution to Exercise 3: Data Structures

```python
def create_sales_tracker():
    """Create and return an empty sales tracking dictionary."""
    return {}

def add_sale(sales_tracker, date, product):
    """
    Add a product sale to the given date.

    Args:
        sales_tracker: The sales tracking dictionary
        date: The date of the sale (string)
        product: The product that was sold
    """
    # If the date already exists in the tracker, append to its list
    if date in sales_tracker:
        sales_tracker[date].append(product)
    # Otherwise, create a new list with this product
    else:
        sales_tracker[date] = [product]

    return sales_tracker

def calculate_daily_totals(sales_tracker):
    """
    Calculate the number of sales for each day.

    Args:
        sales_tracker: The sales tracking dictionary

    Returns:
        A dictionary with dates as keys and total sales as values
    """
    daily_totals = {}

    for date, products in sales_tracker.items():
        daily_totals[date] = len(products)

    return daily_totals

# Test the sales tracker
tracker = create_sales_tracker()
print("Initial sales tracker:", tracker)  # Initial sales tracker: {}

# Add some sales
tracker = add_sale(tracker, "2023-01-15", "Laptop")
tracker = add_sale(tracker, "2023-01-15", "Mouse")
tracker = add_sale(tracker, "2023-01-16", "Keyboard")
tracker = add_sale(tracker, "2023-01-17", "Monitor")
tracker = add_sale(tracker, "2023-01-17", "Headphones")
tracker = add_sale(tracker, "2023-01-17", "Mouse")

print("\nSales tracker after adding sales:")
for date, products in tracker.items():
    print(f"  {date}: {products}")
# Sales tracker after adding sales:
#   2023-01-15: ['Laptop', 'Mouse']
#   2023-01-16: ['Keyboard']
#   2023-01-17: ['Monitor', 'Headphones', 'Mouse']

# Calculate daily totals
totals = calculate_daily_totals(tracker)
print("\nDaily sales totals:")
for date, total in totals.items():
    print(f"  {date}: {total} items")
# Daily sales totals:
#   2023-01-15: 2 items
#   2023-01-16: 1 items
#   2023-01-17: 3 items
```

### Solution to Exercise 4: Standard Library Challenge

```python
import datetime

# Get current date
current_date = datetime.datetime.now()
print(f"Current date and time: {current_date}")  # Current date and time: 2023-04-17 15:45:30.123456 (will vary)

# 1. Calculate and print the current day of the week
day_of_week = current_date.strftime("%A")  # %A gives full weekday name
print(f"1. Current day of the week: {day_of_week}")  # 1. Current day of the week: Monday (will vary)

# 2. Determine number of days until the end of the current month
# First, get the last day of the current month
year = current_date.year
month = current_date.month

# To get the last day of the month, we'll use the first day of next month and subtract one day
if month == 12:  # December
    next_month = datetime.datetime(year + 1, 1, 1)  # January 1 of next year
else:
    next_month = datetime.datetime(year, month + 1, 1)  # First day of next month

last_day_of_month = next_month - datetime.timedelta(days=1)
days_remaining = last_day_of_month.day - current_date.day

print(f"2. Days until the end of {current_date.strftime('%B')}: {days_remaining}")
# 2. Days until the end of April: 13 (will vary)

# 3. Format the current date as "Month Day, Year"
formatted_date = current_date.strftime("%B %d, %Y")
print(f"3. Formatted date: {formatted_date}")  # 3. Formatted date: April 17, 2023 (will vary)
```

### Solution to Challenge Exercise: Enhanced Sales Analyzer

```python
def is_valid_record(record):
    """Check if a sales record is valid."""
    order_id, product_name, quantity_str, price_str, date = record

    # Check for missing product name
    if not product_name:
        return False

    # Check if quantity is a valid number
    try:
        quantity = int(quantity_str)
    except ValueError:
        return False

    # Check for zero or negative quantity
    if quantity <= 0:
        return False

    # Check if price is a valid number
    try:
        price = float(price_str)
    except ValueError:
        return False

    return True

def analyze_sales_enhanced(sales_data):
    """Analyze sales data with filtering and grouping."""
    # Filter valid records using traditional loop
    valid_records = []
    for record in sales_data:
        if is_valid_record(record):
            valid_records.append(record)

    print(f"Total records: {len(sales_data)}")  # Total records: 11
    print(f"Valid records: {len(valid_records)}")  # Valid records: 8

    # Calculate totals and group by product
    product_sales = {}
    total_sales = 0

    for record in valid_records:
        _, product_name, quantity_str, price_str, _ = record
        quantity = int(quantity_str)
        price = float(price_str)

        # Calculate order value
        order_value = quantity * price

        # Add to total sales
        total_sales += order_value

        # Group by product (using dictionary)
        if product_name in product_sales:
            product_sales[product_name] += order_value
        else:
            product_sales[product_name] = order_value

    # Calculate average order value
    average_order = total_sales / len(valid_records) if valid_records else 0

    # Find top product
    top_product = ""
    top_sales = 0

    for product, sales in product_sales.items():
        if sales > top_sales:
            top_product = product
            top_sales = sales

    # Generate a formatted report
    report = f"""
ENHANCED SALES ANALYSIS REPORT
=============================

Summary:
--------
Total Records: {len(sales_data)}
Valid Records: {len(valid_records)}
Total Sales: ${total_sales:.2f}
Average Order: ${average_order:.2f}

Top Product:
-----------
{top_product}: ${top_sales:.2f}

Sales by Product:
---------------
"""

    # Add product sales in descending order
    # First, create a sorted list of (product, sales) tuples
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

    # Add to report
    for product, sales in sorted_products:
        report += f"{product}: ${sales:.2f}\n"

    return report

# Run the enhanced analyzer with our sample data
enhanced_report = analyze_sales_enhanced(sales_data)
print(enhanced_report)
"""
ENHANCED SALES ANALYSIS REPORT
=============================

Summary:
--------
Total Records: 11
Valid Records: 8
Total Sales: $4214.70
Average Order: $526.84

Top Product:
-----------
Laptop: $2899.97

Sales by Product:
---------------
Laptop: $2899.97
Monitor: $449.97
Mouse: $374.85
Keyboard: $249.95
Headphones: $239.96
"""
```

## 1.12 Connection to Chapter 2: Python Data Handling and Error Management

In this chapter, we've established the core Python skills needed for data engineering. In Chapter 2, we'll build on these foundations by focusing on:

### What's Coming in Chapter 2

- **File Handling**: Reading from and writing to files, essential for data ingestion and export
- **Error Handling**: Creating robust code that gracefully recovers from failures
- **Working with Data Formats**: Processing common formats like CSV and JSON
- **List Comprehensions**: Creating concise, readable data transformations
- **Modules and Imports**: Organizing and reusing code effectively

### How Chapter 1 Skills Will Apply

The skills you've learned in this chapter will be directly applied in Chapter 2:

- **Variables and Data Types**: Used for storing and manipulating file contents
- **Control Flow**: Applied to process files line by line and handle different conditions
- **Functions**: Used to create reusable file processing operations
- **Data Structures**: Applied to organize and process data read from files
- **String Manipulation**: Essential for parsing and formatting text files

In Chapter 2, we'll shift from working with in-memory data to reading and writing external files, a critical skill for data engineering pipelines.

## 1.13 Summary

In this chapter, we've built a solid foundation in Python fundamentals, specifically tailored for data engineering:

- **Python Syntax and Data Types**: Variables, basic types, operators, and common errors
- **Control Flow**: Conditional statements and loops to make decisions and repeat actions
- **Functions**: Creating reusable code blocks for data operations
- **Data Structures**: Using lists, dictionaries, tuples, and sets to organize data effectively
- **String Manipulation**: Working with text data using methods and f-strings
- **Standard Library Modules**: Leveraging Python's built-in capabilities
- **Performance Considerations**: Understanding efficiency in data operations

These fundamentals form the building blocks for all data engineering tasks. We've seen how to apply these concepts to practical data scenarios through our micro-project and exercises.

In the next chapter, we'll extend these skills by learning how to work with external data files, implement robust error handling, and process common data formats like CSV and JSON.
