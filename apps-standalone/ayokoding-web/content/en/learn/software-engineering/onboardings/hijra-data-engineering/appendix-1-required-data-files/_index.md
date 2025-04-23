---
title: 'Appendix 1: Required Data Files'
date: 2025-04-17T07:20:00+07:00
draft: false
weight: 73
---

This appendix provides all required data files referenced in the **Data Engineering Onboarding Curriculum** for Hijra Group’s onboarding program. These files are used across various chapters, particularly in micro-projects and exercises, to support hands-on learning with Python, NumPy, Pandas, and other tools. Each file is presented with its content, purpose, and the chapters where it is used, ensuring learners can replicate the datasets for consistent results. All file paths are relative to the `de-onboarding/data/` directory, as specified in the curriculum.

The datasets are designed to be straightforward for seeding, aligning with the curriculum’s pedagogical approach. They simulate financial transaction data relevant to Hijra Group’s Sharia-compliant fintech analytics, such as sales records. Where applicable, notes on file creation, potential pitfalls, and validation are included to prevent issues like `FileNotFoundError` or parsing errors.

## File Structure

All data files should be stored in the `de-onboarding/data/` directory. Create this directory before running any scripts:

```bash
mkdir -p de-onboarding/data
```

**Follow-Along Tips**:

- Ensure the `de-onboarding/` folder exists in your working directory.
- Save each file exactly as shown, including line breaks and formatting, to avoid parsing errors.
- Use a text editor (e.g., VS Code) to create files, ensuring UTF-8 encoding unless specified otherwise.
- Verify file paths with `ls data/` (Unix/macOS) or `dir data\` (Windows) before running scripts.
- If `FileNotFoundError` occurs, confirm the file exists in `de-onboarding/data/` and check the script’s path (e.g., `print(csv_path)`).
- Configure your editor for **4-space indentation** per PEP 8, preferring spaces over tabs to avoid `IndentationError`. In VS Code, set “Editor: Tab Size” to 4, “Editor: Insert Spaces” to true, and “Editor: Detect Indentation” to false. Run `python -tt script.py` to detect tab/space mixing.

## Data Files

Below are the required data files, their contents, purposes, and associated chapters. Each file is presented in a format suitable for copying into the specified path.

### 1. `data/sales.csv`

**Purpose**: This CSV file contains sales transaction data for processing and analysis, simulating Hijra Group’s Sharia-compliant product sales. It is used for parsing, validation, numerical computations, grouping, and visualization in micro-projects and exercises.

**Used in Chapters**:

- Chapter 1: Python Core Language Essentials (Micro-Project: Sales Data Analyzer)
- Chapter 2: Python Data Handling and Error Management (Micro-Project: Sales Data Processor)
- Chapter 3: Essential Data Libraries (Micro-Project: Refactored Sales Data Processor, Exercises 2–5)
- Chapter 6: Checkpoint 1: Python Foundations Review
- Chapter 7: Static Typing with Python
- Chapter 8: Python Annotations and Decorators
- Chapter 9: Introduction to Testing in Python
- Chapter 10: Data Engineering Code Quality
- Chapter 11: Checkpoint 2: Python Code Quality Review
- Chapter 12: SQL Fundamentals with SQLite
- Chapter 13: Python and SQLite Integration
- Chapter 14: Advanced Database Operations with SQLite
- Chapter 15: Type-Safe Database Programming
- Chapter 19: Advanced SQL Querying with SQLite
- Chapter 20: SQLite Indexing and Optimization
- Chapter 25: BigQuery Fundamentals
- Chapter 26: Python and BigQuery Integration
- Chapter 27: BigQuery Advanced Querying
- Chapter 28: BigQuery Data Warehousing
- Chapter 29: BigQuery Optimization Techniques
- Chapter 30: Checkpoint 4: Cloud Analytics Review
- Chapter 32: Data Marts with BigQuery
- Chapter 33: BigQuery and Google Sheets Integration
- Chapter 38: Advanced NumPy
- Chapter 39: Advanced Pandas
- Chapter 40: Concurrency in Python
- Chapter 41: Type-Safe Data Processing
- Chapter 42: Testing Data Pipelines
- Chapter 43: Advanced Testing Techniques
- Chapter 44: Checkpoint 6: Advanced Data Processing Review
- Chapter 46: Jupyter Notebooks for Data Development
- Chapter 50: BigQuery Advanced Optimization
- Chapter 51: Data Visualization and BI Tools
- Chapter 52: Introduction to Django
- Chapter 54: dbt for Data Transformation
- Chapter 55: Simple Scheduling with Python
- Chapter 56: Airflow Fundamentals
- Chapter 57: Airflow in Docker
- Chapter 58: Building Complex Airflow Workflows
- Chapter 59: Checkpoint 7: Pipeline Orchestration Review
- Chapter 60: Docker for Data Applications
- Chapter 64: Airflow in Kubernetes
- Chapter 65: Security Best Practices for Data Pipelines
- Chapter 66: Pipeline Monitoring and Observability
- Chapter 67: Checkpoint 8: Production Deployment Review

**Content**:

```csv
product,price,quantity
Halal Laptop,999.99,2
Halal Mouse,24.99,10
Halal Keyboard,49.99,5
,29.99,3
Monitor,invalid,2
Headphones,5.00,150
```

**Creation Instructions**:

1. Create `de-onboarding/data/sales.csv`.
2. Copy the content above into the file.
3. Save with UTF-8 encoding.
4. Verify with `cat data/sales.csv` (Unix/macOS) or `type data\sales.csv` (Windows).

**Notes**:

- The file includes intentional errors (e.g., missing product, invalid price, excessive quantity) to test validation logic.
- Columns: `product` (string), `price` (float or invalid string), `quantity` (integer or invalid string).
- **Pitfalls**:
  - **Parsing Errors**: Ensure commas are not escaped or quoted, as Chapter 1 parses manually without the `csv` module. From Chapter 2 onward, `csv.DictReader` or `pd.read_csv` handles commas correctly.
  - **Encoding Issues**: Use UTF-8 to avoid `UnicodeDecodeError`. If errors occur, specify `encoding="utf-8"` in `pd.read_csv` (Chapter 3) or `open()` (Chapter 2).
  - **FileNotFoundError**: Verify the file is in `data/`. Print the path in scripts (e.g., `print(csv_path)`).
- **Validation**: Check the file has 6 rows (1 header, 5 data rows) with `wc -l data/sales.csv` (Unix/macOS) or `findstr /r /n "^" data\sales.csv | find /c ":"` (Windows).

### 2. `data/config.yaml`

**Purpose**: This YAML file provides configuration settings for validating sales data, such as minimum price, maximum quantity, and product prefix. It is used to enforce Sharia-compliant rules and ensure data integrity in processing scripts.

**Used in Chapters**:

- Chapter 2: Python Data Handling and Error Management (Micro-Project: Sales Data Processor)
- Chapter 3: Essential Data Libraries (Micro-Project: Refactored Sales Data Processor)
- Chapter 13: Python and SQLite Integration
- Chapter 17: Python and PostgreSQL Integration
- Chapter 31: Data Lakes with Google Cloud Storage
- Chapter 34: Advanced Python for Data Engineering
- Chapter 35: Google Cloud Storage Advanced Features
- Chapter 36: Advanced Python for Data Engineering
- Chapter 37: Checkpoint 5: Analytical Storage Review
- Chapter 54: dbt for Data Transformation
- Chapter 55: Simple Scheduling with Python
- Chapter 56: Airflow Fundamentals
- Chapter 57: Airflow in Docker
- Chapter 58: Building Complex Airflow Workflows
- Chapter 60: Docker for Data Applications
- Chapter 64: Airflow in Kubernetes

**Content**:

```yaml
min_price: 10.0
max_quantity: 100
required_fields:
  - product
  - price
  - quantity
product_prefix: 'Halal'
max_decimals: 2
```

**Creation Instructions**:

1. Create `de-onboarding/data/config.yaml`.
2. Copy the content above into the file.
3. Save with UTF-8 encoding.
4. Verify with `cat data/config.yaml` (Unix/macOS) or `type data\config.yaml` (Windows).

**Notes**:

- The file defines validation rules: minimum price (`10.0`), maximum quantity (`100`), required CSV columns, product prefix (`Halal`), and maximum decimal places for prices (`2`).
- Parsed using `PyYAML` in Chapter 2 onward (e.g., `yaml.safe_load`).
- **Pitfalls**:
  - **YAML Syntax Errors**: Ensure proper indentation (2 spaces, standard for YAML) and no tabs. Validate with an online YAML linter or `python -c "import yaml; yaml.safe_load(open('data/config.yaml'))"`.
  - **ModuleNotFoundError**: Install `pyyaml` with `pip install pyyaml` before running scripts.
  - **FileNotFoundError**: Verify the file is in `data/`. Print the path in scripts (e.g., `print(config_path)`).
- **Validation**: Check the file has 8 lines and contains all required keys (`min_price`, `max_quantity`, `required_fields`, `product_prefix`, `max_decimals`). Run a script to load and print the config:

```python
import yaml
with open("data/config.yaml", "r") as file:
    config = yaml.safe_load(file)
print(config)
```

### 3. `data/sample.csv`

**Purpose**: This CSV file is a simplified dataset for exercises, containing a subset of sales data to test specific functionalities like filtering, grouping, and visualization. It ensures learners can focus on coding logic without complex data issues.

**Used in Chapters**:

- Chapter 3: Essential Data Libraries (Exercises 2–5)

**Content**:

```csv
product,price,quantity
Halal Laptop,999.99,2
Halal Mouse,24.99,10
```

**Creation Instructions**:

1. Create `de-onboarding/data/sample.csv`.
2. Copy the content above into the file.
3. Save with UTF-8 encoding.
4. Verify with `cat data/sample.csv` (Unix/macOS) or `type data\sample.csv` (Windows).

**Notes**:

- Contains 3 rows (1 header, 2 data rows) with valid data for simplicity.
- Columns match `sales.csv`: `product` (string), `price` (float), `quantity` (integer).
- **Pitfalls**:
  - **Parsing Errors**: Ensure commas are not escaped. Use `pd.read_csv` in Chapter 3 exercises.
  - **FileNotFoundError**: Verify the file is in `data/`. Print the path in scripts.
- **Validation**: Check the file has 3 rows with `wc -l data/sample.csv` (Unix/macOS) or `findstr /r /n "^" data\sample.csv | find /c ":"` (Windows).

### 4. `data/empty.csv`

**Purpose**: This CSV file is an empty dataset (header only) used to test edge cases, such as handling empty inputs in processing scripts. It ensures robustness in micro-projects and exercises.

**Used in Chapters**:

- Chapter 1: Python Core Language Essentials (Micro-Project: Sales Data Analyzer, Test Scenarios)
- Chapter 3: Essential Data Libraries (Micro-Project: Refactored Sales Data Processor, Test Scenarios)

**Content**:

```csv
product,price,quantity
```

**Creation Instructions**:

1. Create `de-onboarding/data/empty.csv`.
2. Copy the content above into the file (single line with header).
3. Save with UTF-8 encoding.
4. Verify with `cat data/empty.csv` (Unix/macOS) or `type data\empty.csv` (Windows).

**Notes**:

- Contains only the header row to simulate an empty dataset.
- **Pitfalls**:
  - **Parsing Errors**: Scripts should handle zero data rows. In Chapter 1, manual parsing should return an empty list; in Chapter 3, `pd.read_csv` returns an empty DataFrame.
  - **FileNotFoundError**: Verify the file is in `data/`.
- **Validation**: Check the file has 1 row with `wc -l data/empty.csv` (Unix/macOS) or `findstr /r /n "^" data\empty.csv | find /c ":"` (Windows).

### 5. `data/invalid.csv`

**Purpose**: This CSV file contains invalid headers to test error handling in scripts, ensuring robustness when column names do not match expected values (e.g., `product`, `price`, `quantity`).

**Used in Chapters**:

- Chapter 3: Essential Data Libraries (Micro-Project: Refactored Sales Data Processor, Test Scenarios)

**Content**:

```csv
name,price,quantity
Halal Laptop,999.99,2
```

**Creation Instructions**:

1. Create `de-onboarding/data/invalid.csv`.
2. Copy the content above into the file.
3. Save with UTF-8 encoding.
4. Verify with `cat data/invalid.csv` (Unix/macOS) or `type data\invalid.csv` (Windows).

**Notes**:

- Uses `name` instead of `product` to trigger `KeyError` or validation failures.
- **Pitfalls**:
  - **KeyError**: Scripts should check for required columns (e.g., `if "product" not in df.columns`). Print `df.columns` to debug.
  - **FileNotFoundError**: Verify the file is in `data/`.
- **Validation**: Check the file has 2 rows with `wc -l data/invalid.csv` (Unix/macOS) or `findstr /r /n "^" data\invalid.csv | find /c ":"` (Windows).

### 6. `data/malformed.csv`

**Purpose**: This CSV file contains malformed data (e.g., non-numeric quantity) to test validation and filtering logic, ensuring scripts can handle invalid data types.

**Used in Chapters**:

- Chapter 3: Essential Data Libraries (Micro-Project: Refactored Sales Data Processor, Test Scenarios)

**Content**:

```csv
product,price,quantity
Halal Laptop,999.99,invalid
Halal Mouse,24.99,10
```

**Creation Instructions**:

1. Create `de-onboarding/data/malformed.csv`.
2. Copy the content above into the file.
3. Save with UTF-8 encoding.
4. Verify with `cat data/malformed.csv` (Unix/macOS) or `type data\malformed.csv` (Windows).

**Notes**:

- Includes an invalid `quantity` (`invalid`) to test type validation (e.g., `isdigit()` in Chapter 3).
- **Pitfalls**:
  - **TypeError**: Scripts should filter non-integer quantities (e.g., `df["quantity"].apply(lambda x: str(x).isdigit())`). Print `df.dtypes` to debug.
  - **FileNotFoundError**: Verify the file is in `data/`.
- **Validation**: Check the file has 3 rows with `wc -l data/malformed.csv` (Unix/macOS) or `findstr /r /n "^" data\malformed.csv | find /c ":"` (Windows).

### 7. `data/negative.csv`

**Purpose**: This CSV file includes negative prices to test validation logic, ensuring scripts reject invalid financial data (e.g., negative transaction amounts).

**Used in Chapters**:

- Chapter 3: Essential Data Libraries (Micro-Project: Refactored Sales Data Processor, Test Scenarios)

**Content**:

```csv
product,price,quantity
Halal Laptop,-999.99,2
Halal Mouse,24.99,10
```

**Creation Instructions**:

1. Create `de-onboarding/data/negative.csv`.
2. Copy the content above into the file.
3. Save with UTF-8 encoding.
4. Verify with `cat data/negative.csv` (Unix/macOS) or `type data\negative.csv` (Windows).

**Notes**:

- Includes a negative `price` (`-999.99`) to test filtering (e.g., `df["price"] > 0`).
- **Pitfalls**:
  - **Validation Errors**: Scripts should reject negative prices. Print `df["price"]` to debug.
  - **FileNotFoundError**: Verify the file is in `data/`.
- **Validation**: Check the file has 3 rows with `wc -l data/negative.csv` (Unix/macOS) or `findstr /r /n "^" data\negative.csv | find /c ":"` (Windows).

### 8. `data/transactions.csv`

**Purpose**: This CSV file contains transaction data for advanced processing, such as API integration, database operations, and cloud analytics. It extends the sales data concept to broader financial transactions.

**Used in Chapters**:

- Chapter 4: Web Integration and APIs
- Chapter 5: Object-Oriented Programming for Data Engineering
- Chapter 21: Advanced PostgreSQL Querying
- Chapter 22: PostgreSQL Indexing and Optimization
- Chapter 23: Type-Safe Database Integration
- Chapter 24: Checkpoint 3B: Database Fundamentals II Review
- Chapter 31: Data Lakes with Google Cloud Storage
- Chapter 34: Advanced Python for Data Engineering
- Chapter 35: Google Cloud Storage Advanced Features
- Chapter 36: Advanced Python for Data Engineering
- Chapter 37: Checkpoint 5: Analytical Storage Review
- Chapter 53: Introduction to FastAPI
- Chapter 68: Capstone Project Planning
- Chapter 69: Capstone Project Implementation Part 1
- Chapter 70: Capstone Project Implementation Part 2
- Chapter 71: Capstone Project Implementation Part 3

**Content**:

```csv
transaction_id,product,price,quantity,date
T001,Halal Laptop,999.99,2,2023-10-01
T002,Halal Mouse,24.99,10,2023-10-02
T003,Halal Keyboard,49.99,5,2023-10-03
T004,,29.99,3,2023-10-04
T005,Monitor,199.99,2,2023-10-05
```

**Creation Instructions**:

1. Create `de-onboarding/data/transactions.csv`.
2. Copy the content above into the file.
3. Save with UTF-8 encoding.
4. Verify with `cat data/transactions.csv` (Unix/macOS) or `type data\transactions.csv` (Windows).

**Notes**:

- Includes additional columns: `transaction_id` (string) and `date` (string, YYYY-MM-DD format).
- Contains 5 data rows with intentional errors (e.g., missing product) for validation testing.
- **Pitfalls**:
  - **Parsing Errors**: Ensure `pd.read_csv` is used in Chapter 4 onward, as it handles additional columns. Print `df.columns` to verify.
  - **Date Parsing**: If dates are processed (e.g., Chapter 21), use `pd.to_datetime` to convert. Print `df["date"]` to debug.
  - **FileNotFoundError**: Verify the file is in `data/`.
- **Validation**: Check the file has 6 rows (1 header, 5 data rows) with `wc -l data/transactions.csv` (Unix/macOS) or `findstr /r /n "^" data\transactions.csv | find /c ":"` (Windows).

### 9. `data/sales.db`

**Purpose**: This SQLite database file stores sales data for database-related chapters, allowing learners to practice SQL queries, Python integration, and optimization.

**Used in Chapters**:

- Chapter 12: SQL Fundamentals with SQLite
- Chapter 13: Python and SQLite Integration
- Chapter 14: Advanced Database Operations with SQLite
- Chapter 15: Type-Safe Database Programming
- Chapter 18: Checkpoint 3A: Database Fundamentals I Review
- Chapter 19: Advanced SQL Querying with SQLite
- Chapter 20: SQLite Indexing and Optimization
- Chapter 24: Checkpoint 3B: Database Fundamentals II Review

**Content**:

- **Table**: `sales`
- **Columns**: `product` (TEXT), `price` (REAL), `quantity` (INTEGER)
- **Data**:
  ```sql
  INSERT INTO sales (product, price, quantity) VALUES
  ('Halal Laptop', 999.99, 2),
  ('Halal Mouse', 24.99, 10),
  ('Halal Keyboard', 49.99, 5);
  ```

**Creation Instructions**:

1. Install SQLite: Ensure `sqlite3` is available (`sqlite3 --version`).
2. Create `de-onboarding/data/sales.db` by running the following Python script:

```python
# File: de-onboarding/create_sales_db.py
import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("data/sales.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    price REAL,
    quantity INTEGER
)
""")

# Insert sample data
cursor.executemany(
    "INSERT INTO sales (product, price, quantity) VALUES (?, ?, ?)",
    [
        ("Halal Laptop", 999.99, 2),
        ("Halal Mouse", 24.99, 10),
        ("Halal Keyboard", 49.99, 5),
    ]
)

# Commit and close
conn.commit()
conn.close()
print("Created data/sales.db")
```

3. Save as `de-onboarding/create_sales_db.py`.
4. Configure editor for 4-space indentation per PEP 8.
5. Run: `python create_sales_db.py`.
6. Verify with `sqlite3 data/sales.db "SELECT * FROM sales;"`.

**Notes**:

- Contains 3 valid rows for simplicity in database exercises.
- **Pitfalls**:
  - **DatabaseNotFound**: Ensure `data/sales.db` is created before running scripts. Run the creation script first.
  - **SQLite Errors**: Verify table schema with `sqlite3 data/sales.db ".schema sales"`.
  - **Permission Issues**: Check write permissions in `data/` with `ls -l data/` (Unix/macOS) or `dir data\` (Windows).
- **Validation**: Query the database to confirm 3 rows:
  ```bash
  sqlite3 data/sales.db "SELECT COUNT(*) FROM sales;"
  # Expected: 3
  ```

### 10. `data/tasks.db`

**Purpose**: This SQLite database file stores task-related data for advanced database operations and web integration, simulating a task management system integrated with sales data.

**Used in Chapters**:

- Chapter 47: Data Access Patterns for Applications

**Content**:

- **Table**: `tasks`
- **Columns**: `task_id` (TEXT), `description` (TEXT), `status` (TEXT)
- **Data**:
  ```sql
  INSERT INTO tasks (task_id, description, status) VALUES
  ('T001', 'Process Halal Laptop sales', 'Completed'),
  ('T002', 'Validate Halal Mouse inventory', 'Pending'),
  ('T003', 'Update Halal Keyboard pricing', 'In Progress');
  ```

**Creation Instructions**:

1. Install SQLite: Ensure `sqlite3` is available (`sqlite3 --version`).
2. Create `de-onboarding/data/tasks.db` by running the following Python script:

```python
# File: de-onboarding/create_tasks_db.py
import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("data/tasks.db")
cursor = conn.cursor()

# Create tasks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    task_id TEXT,
    description TEXT,
    status TEXT
)
""")

# Insert sample data
cursor.executemany(
    "INSERT INTO tasks (task_id, description, status) VALUES (?, ?, ?)",
    [
        ("T001", "Process Halal Laptop sales", "Completed"),
        ("T002", "Validate Halal Mouse inventory", "Pending"),
        ("T003", "Update Halal Keyboard pricing", "In Progress"),
    ]
)

# Commit and close
conn.commit()
conn.close()
print("Created data/tasks.db")
```

3. Save as `de-onboarding/create_tasks_db.py`.
4. Configure editor for 4-space indentation per PEP 8.
5. Run: `python create_tasks_db.py`.
6. Verify with `sqlite3 data/tasks.db "SELECT * FROM tasks;"`.

**Notes**:

- Contains 3 rows to test data access patterns (e.g., DAO, Repository).
- **Pitfalls**:
  - **DatabaseNotFound**: Run the creation script first.
  - **Schema Errors**: Verify table schema with `sqlite3 data/tasks.db ".schema tasks"`.
  - **Permission Issues**: Check write permissions in `data/`.
- **Validation**: Query the database to confirm 3 rows:
  ```bash
  sqlite3 data/tasks.db "SELECT COUNT(*) FROM tasks;"
  # Expected: 3
  ```

## Additional Notes

- **File Organization**: Keep all files in `de-onboarding/data/` to match script expectations. If reorganizing, update script paths accordingly and print paths for debugging.
- **Version Control**: Consider storing `data/` in a Git repository for version control, but exclude large database files (e.g., `sales.db`, `tasks.db`) using `.gitignore`. Recreate database files using the provided scripts.
- **Dependencies**: Install required libraries before running scripts:
  ```bash
  pip install numpy pandas matplotlib pyyaml sqlite3
  ```
  Create a virtual environment to isolate dependencies:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Unix/macOS
  venv\Scripts\activate     # Windows
  ```
- **Testing Edge Cases**: Use `empty.csv`, `invalid.csv`, `malformed.csv`, and `negative.csv` to test script robustness. Debug with print statements (e.g., `print(df.head())` for DataFrames, `print(sale)` for dictionaries).
- **Scalability**: These datasets are small for learning purposes. In production, Hijra Group’s datasets may include millions of rows, requiring chunked processing (Chapter 40) or distributed systems (Chapters 60–66).
- **Future Files**: Later chapters (e.g., Chapter 4’s `transactions.csv` from API fetches, Chapter 12’s `sales.db` for SQLite) may generate additional files dynamically. This appendix includes only static files explicitly defined in Chapters 1–3.

## Summary

This appendix consolidates all required data files for the **Data Engineering Onboarding Curriculum**, ensuring learners have the necessary datasets to complete micro-projects and exercises. By creating these files in `de-onboarding/data/`, you can replicate the curriculum’s examples and test cases. Always verify file contents, paths, and permissions before running scripts, and use the provided creation scripts for database files. These files lay the foundation for learning Python, NumPy, Pandas, and database operations, preparing you for advanced data engineering tasks in later chapters.

**Follow-Along Checklist**:

- [ ] Create `de-onboarding/data/` directory.
- [ ] Save `sales.csv`, `config.yaml`, `sample.csv`, `empty.csv`, `invalid.csv`, `malformed.csv`, `negative.csv`, and `transactions.csv` with the provided contents.
- [ ] Run `create_sales_db.py` and `create_tasks_db.py` to generate `sales.db` and `tasks.db`.
- [ ] Install dependencies: `pip install numpy pandas matplotlib pyyaml sqlite3`.
- [ ] Configure editor for 4-space indentation per PEP 8, preferring spaces over tabs.
- [ ] Verify files with `ls data/` or `dir data\` and check row counts where applicable.
- [ ] Debug issues with print statements and path verification.

This appendix ensures a consistent starting point for all learners, aligning with Hijra Group’s goal of building robust, testable data pipelines.
