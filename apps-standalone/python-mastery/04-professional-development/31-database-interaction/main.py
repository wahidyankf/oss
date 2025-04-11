"""
SQLite Database Interaction Demo
"""

import sqlite3
from datetime import datetime
from contextlib import closing

# Database file path
DB_FILE = "example.db"

# Initialize database
with closing(sqlite3.connect(DB_FILE)) as conn:
    # Create tables
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            product TEXT NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
    """
    )
    conn.commit()


# ===== Basic CRUD Operations =====
def create_user(name, email, age=None):
    """Insert a new user"""
    with closing(sqlite3.connect(DB_FILE)) as conn:
        try:
            conn.execute(
                "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                (name, email, age),
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Email {email} already exists")
            return False


def get_users():
    """Get all users"""
    with closing(sqlite3.connect(DB_FILE)) as conn:
        cursor = conn.execute("SELECT * FROM users")
        return cursor.fetchall()


def update_user(user_id, **kwargs):
    """Update user fields"""
    if not kwargs:
        return False

    set_clause = ", ".join(f"{k} = ?" for k in kwargs)
    values = tuple(kwargs.values()) + (user_id,)

    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.execute(f"UPDATE users SET {set_clause} WHERE id = ?", values)
        conn.commit()
        return True


def delete_user(user_id):
    """Delete a user"""
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return True


# ===== Complex Queries =====
def get_user_with_orders(user_id):
    """Get user with their orders using a join"""
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(
            """
            SELECT u.*, o.id as order_id, o.amount, o.product, o.order_date
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            WHERE u.id = ?
        """,
            (user_id,),
        )

        result = cursor.fetchall()
        if not result:
            return None

        user_data = dict(result[0])
        if "order_id" in user_data and user_data["order_id"] is not None:
            user_data["orders"] = [dict(row) for row in result]
        else:
            user_data["orders"] = []

        return user_data


def get_sales_report():
    """Get sales report with aggregates"""
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(
            """
            SELECT 
                u.id as user_id,
                u.name,
                u.email,
                COUNT(o.id) as order_count,
                SUM(o.amount) as total_spent,
                MAX(o.order_date) as last_order_date
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            GROUP BY u.id, u.name, u.email
            ORDER BY total_spent DESC
        """
        )
        return [dict(row) for row in cursor.fetchall()]


def create_order(user_id, product, amount):
    """Create a new order"""
    with closing(sqlite3.connect(DB_FILE)) as conn:
        try:
            conn.execute(
                "INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)",
                (user_id, product, amount),
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Error creating order: {e}")
            return False


# Example Usage
if __name__ == "__main__":
    # Clear and recreate tables for demo
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.execute("DROP TABLE IF EXISTS orders")
        conn.execute("DROP TABLE IF EXISTS users")
        conn.commit()

    # Reinitialize
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.executescript(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                product TEXT NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
        """
        )
        conn.commit()

    # Create some users
    create_user("John Doe", "john@example.com", 30)
    create_user("Jane Smith", "jane@example.com", 25)

    # Create some orders
    create_order(1, "Laptop", 999.99)
    create_order(1, "Mouse", 49.99)
    create_order(2, "Keyboard", 79.99)

    # Demo complex queries
    print("\nUser with orders:")
    user_with_orders = get_user_with_orders(1)
    print(user_with_orders)

    print("\nSales report:")
    sales_report = get_sales_report()
    for row in sales_report:
        print(row)
