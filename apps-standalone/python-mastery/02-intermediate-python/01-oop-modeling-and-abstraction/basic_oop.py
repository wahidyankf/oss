"""
Basic Object-Oriented Programming Demo

This heavily commented example demonstrates fundamental Python OOP concepts:
1. Class definition and instantiation
2. Attribute visibility (public, protected, private)
3. Instance methods
4. Special/magic methods (__dunder__ methods)

Key Concepts Illustrated:
- Encapsulation through access modifiers
- Operator overloading via special methods
- Instance state management
"""


class BankAccount:
    """
    A bank account class demonstrating core OOP principles.

    Attributes:
        account_type (public): Account category (checking/savings/etc)
        _owner (protected): Account holder name (convention: internal use)
        __balance (private): Current balance (name-mangled for privacy)
        __transactions (private): List of transaction records

    Methods:
        deposit: Add funds to account
        withdraw: Remove funds from account
        __str__: String representation
        __eq__: Compare account balances
        __add__: Merge two accounts
        __len__: Count transactions
    """

    def __init__(self, owner, balance=0, account_type="checking"):
        """
        Initialize a new bank account.

        Args:
            owner (str): Account holder name
            balance (float): Starting balance (default 0)
            account_type (str): Account category (default "checking")
        """
        # Public attribute - freely accessible
        self.account_type = account_type

        # Protected attribute (single underscore) - convention for internal use
        self._owner = owner

        # Private attribute (double underscore) - name mangled at runtime
        self.__balance = balance

        # Private transaction history
        self.__transactions = []

    def deposit(self, amount):
        """
        Deposit money into account.

        Args:
            amount (float): Amount to deposit (must be positive)

        Returns:
            str: Transaction confirmation message
        """
        # Validate input
        if amount <= 0:
            return "Deposit amount must be positive"

        self.__balance += amount
        self.__transactions.append(f"Deposit: +{amount}")
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        """
        Withdraw money from account.

        Args:
            amount (float): Amount to withdraw (must be positive)

        Returns:
            str: Transaction confirmation or error message
        """
        # Validate input and funds
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.__balance:
            return "Insufficient funds"

        self.__balance -= amount
        self.__transactions.append(f"Withdrawal: -{amount}")
        return f"Withdrew {amount}. New balance: {self.__balance}"

    # Special Methods (operator overloading) ==============================

    def __str__(self):
        """
        String representation of account (used by print() and str())

        Returns:
            str: Human-readable account summary
        """
        return f"BankAccount(owner='{self._owner}', type='{self.account_type}', balance={self.__balance})"

    def __eq__(self, other):
        """
        Compare accounts by balance (== operator)

        Args:
            other (BankAccount): Account to compare with

        Returns:
            bool: True if balances are equal
        """
        return self.__balance == other.__balance

    def __add__(self, other):
        """
        Merge two accounts (+ operator)

        Args:
            other (BankAccount): Account to merge with

        Returns:
            BankAccount: New account with combined balance
        """
        new_account = BankAccount(
            owner=f"{self._owner}+{other._owner}",
            balance=self.__balance + other.__balance,
            account_type="merged",
        )
        return new_account

    def __len__(self):
        """
        Get transaction count (len() function)

        Returns:
            int: Number of transactions
        """
        return len(self.__transactions)


if __name__ == "__main__":
    """
    Demonstration of BankAccount functionality.

    Shows:
    - Account creation
    - Deposits/withdrawals
    - Special method usage
    - Transaction tracking
    """
    # Create accounts
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 500)

    # Perform transactions
    print(acc1.deposit(200))  # Expected: Deposit confirmation
    print(acc1.withdraw(100))  # Expected: Withdrawal confirmation
    print(acc2.deposit(300))  # Expected: Deposit confirmation

    # Demonstrate special methods
    print(f"\nAccount Info:\n{acc1}")  # Uses __str__
    print(f"Alice's transactions: {len(acc1)}")  # Uses __len__
    print(f"Bob's transactions: {len(acc2)}")

    # Merge accounts (__add__)
    merged = acc1 + acc2
    print(f"\nMerged account: {merged}")

    # Compare balances (__eq__)
    print(f"Accounts equal? {acc1 == acc2}")  # Expected: False
