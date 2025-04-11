# Database Interaction with SQLite

This demo shows raw SQLite database interaction using Python's built-in `sqlite3` module.

## Key Features

- Creating a database and tables
- Basic CRUD operations (Create, Read, Update, Delete)
- Using context managers for connections
- Parameterized queries to prevent SQL injection
- Transactions for data integrity

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
