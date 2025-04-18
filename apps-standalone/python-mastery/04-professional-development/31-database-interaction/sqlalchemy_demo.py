"""
SQLAlchemy Database Interaction Demo
"""

from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    func,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)


# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    product = Column(String, nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="orders")


# Create tables
Base.metadata.create_all(engine)


if __name__ == "__main__":
    # Create session
    session = Session()

    # Clear existing data
    session.query(Order).delete()
    session.query(User).delete()
    session.commit()

    # Create users
    john = User(name="John Doe", email="john@example.com", age=30)
    jane = User(name="Jane Smith", email="jane@example.com", age=25)

    # Add users to session
    session.add_all([john, jane])
    session.commit()

    # Create orders
    order1 = Order(user=john, product="Laptop", amount=999.99)
    order2 = Order(user=john, product="Mouse", amount=49.99)
    order3 = Order(user=jane, product="Keyboard", amount=79.99)

    # Add orders to session
    session.add_all([order1, order2, order3])
    session.commit()

    # Query all users - output as dicts
    print("\nAll users:")
    for user in session.query(User).all():
        user_dict = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age,
        }
        if user.created_at is not None:  # Proper None check instead of column check
            user_dict["created_at"] = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
        print(user_dict)

    # Get user with orders - output as dict
    print("\nJohn's orders:")
    john = session.query(User).filter_by(name="John Doe").first()
    if john is not None:
        for order in john.orders:
            order_dict = {
                "id": order.id,
                "product": order.product,
                "amount": order.amount,
            }
            if order.order_date is not None:  # Proper None check
                order_dict["order_date"] = order.order_date.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            print(order_dict)
    else:
        print("User 'John Doe' not found")

    # Sales report - output as dict
    print("\nSales report:")
    sales = (
        session.query(
            User.id,
            User.name,
            User.email,
            func.count(Order.id).label("order_count"),
            func.sum(Order.amount).label("total_spent"),
            func.max(Order.order_date).label("last_order_date"),
        )
        .outerjoin(Order)
        .group_by(User.id)
        .order_by(func.sum(Order.amount).desc())
        .all()
    )

    for sale in sales:
        print(f"{sale.name}: {sale.order_count} orders, ${sale.total_spent:.2f} total")

    session.close()
