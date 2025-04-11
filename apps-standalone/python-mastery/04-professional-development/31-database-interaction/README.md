# Database Interaction with SQLite

This demo shows raw SQLite database interaction using Python's built-in `sqlite3` module.

## Key Features

- Creating a database and tables
- Basic CRUD operations (Create, Read, Update, Delete)
- Using context managers for connections
- Parameterized queries to prevent SQL injection
- Transactions for data integrity

## Key Differences

| Feature               | Vanilla SQLite             | SQLAlchemy                     |
| --------------------- | -------------------------- | ------------------------------ |
| **Query Style**       | Raw SQL strings            | ORM methods                    |
| **Relationships**     | Manual joins               | Automatic via `relationship()` |
| **Output Format**     | Single joined dictionaries | Separate related objects       |
| **Datetime Handling** | SQLite strings             | Python datetime objects        |
| **Error Handling**    | Manual checks              | ORM-aware exceptions           |

## Why Keep Differences?

1. **Demonstrates Different Patterns**

   - Vanilla shows direct SQL execution
   - SQLAlchemy shows ORM best practices

2. **Performance Considerations**

   - Vanilla joins may be faster for simple queries
   - SQLAlchemy better for complex object graphs

3. **Readability Tradeoffs**
   - Vanilla shows all data at once
   - SQLAlchemy maintains object boundaries

## How to Run

```bash
python main.py
```

## Database Schema

The example uses a simple `users` table:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Running the Demos

```bash
python vanilla_demo.py
python sqlalchemy_demo.py
```

Outputs will be functionally equivalent but formatted differently to showcase each approach's strengths.

## Implementation Details

### Vanilla SQLite

- Uses Python's built-in `sqlite3` module
- Manual SQL string construction
- Explicit transaction management
- Manual relationship handling via JOINs

### SQLAlchemy

- Uses declarative base for models
- Automatic relationship management
- Session-based transaction handling
- Query builder interface

## Output Comparison

### SQLAlchemy Output

```python
All users:
{'id': 5, 'name': 'John Doe', 'email': 'john@example.com', 'age': 30, 'created_at': '2025-04-11 08:50:53'}
{'id': 6, 'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25, 'created_at': '2025-04-11 08:50:53'}

John's orders:
{'id': 7, 'product': 'Laptop', 'amount': 999.99, 'order_date': '2025-04-11 08:50:53'}
{'id': 8, 'product': 'Mouse', 'amount': 49.99, 'order_date': '2025-04-11 08:50:53'}
```

### Vanilla SQLite Output

```python
All users:
{'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'age': 30, 'created_at': '2025-04-11 08:51:29'}
{'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25, 'created_at': '2025-04-11 08:51:29'}

John's orders:
{'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'age': 30, 'created_at': '2025-04-11 08:51:29', 'order_id': 1, 'amount': 999.99, 'product': 'Laptop', 'order_date': '2025-04-11 08:51:29'}
```

Key Differences:

- **SQLAlchemy**: Separates user and order data (ORM pattern)
- **Vanilla**: Shows joined data in single dictionaries (SQL pattern)
- Both use identical datetime string formatting
- Sales reports are identical in format

## Sample Output Comparison

### Vanilla Demo Output

```python
{
  'id': 1,
  'name': 'John Doe',
  'email': 'john@example.com',
  'orders': [
    {'product': 'Laptop', 'amount': 999.99}
  ]
}
```

### SQLAlchemy Demo Output

```python
<User(id=1, name='John Doe')>
<Order(product='Laptop', user_id=1)>
```

## Performance Considerations

| Operation     | Vanilla SQLite      | SQLAlchemy             |
| ------------- | ------------------- | ---------------------- |
| Simple CRUD   | Faster (raw SQL)    | Slightly slower        |
| Complex Joins | Manual optimization | Automatic optimization |
| Object Graph  | Manual handling     | Built-in support       |

## When to Use Each

- **Choose Vanilla SQLite** when:

  - You need maximum performance
  - Working with simple schemas
  - Want direct SQL control

- **Choose SQLAlchemy** when:
  - Working with complex object relationships
  - Need database abstraction
  - Want automatic session management
