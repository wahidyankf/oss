"""
Vanilla SQLite Database Interaction Demo
"""

import sqlite3
from datetime import datetime
from contextlib import closing

# Database file path
DB_FILE = "example.db"


# Initialize database
def init_db():
    with closing(sqlite3.connect(DB_FILE)) as conn:
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


# CRUD Operations
def create_user(name, email, age=None):
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age)
        )
        conn.commit()
        return conn.execute("SELECT last_insert_rowid()").fetchone()[0]


def create_order(user_id, product, amount):
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


def get_users():
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute("SELECT * FROM users").fetchall()


def get_user_with_orders(user_id):
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


# Example Usage
if __name__ == "__main__":
    # Initialize database
    with closing(sqlite3.connect(DB_FILE)) as conn:
        conn.execute("DROP TABLE IF EXISTS orders")
        conn.execute("DROP TABLE IF EXISTS users")
        conn.commit()
    init_db()

    # Create users
    john_id = create_user("John Doe", "john@example.com", 30)
    jane_id = create_user("Jane Smith", "jane@example.com", 25)

    # Create orders
    create_order(john_id, "Laptop", 999.99)
    create_order(john_id, "Mouse", 49.99)
    create_order(jane_id, "Keyboard", 79.99)

    # Query all users
    print("\nAll users:")
    for user in get_users():
        print(dict(user))

    # Get user with orders
    print("\nJohn's orders:")
    john = get_user_with_orders(john_id)
    if john is not None:
        for order in john["orders"]:
            print(order)
    else:
        print("User not found")

    # Sales report
    print("\nSales report:")
    for row in get_sales_report():
        print(
            f"{row['name']}: {row['order_count']} orders, ${row['total_spent']:.2f} total"
        )
