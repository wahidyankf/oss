# Python Error Handling Demo

This directory demonstrates Python's exception handling mechanisms.

## Key Concepts Demonstrated

1. **Basic Exception Handling** (`try-except-else-finally`)
2. **Multiple Exception Types** (catching different exceptions)
3. **Custom Exceptions** (defining application-specific errors)
4. **Exception Chaining** (preserving original exceptions)
5. **Exception Context** (adding supplemental information)
6. **Built-in Exceptions** (common exception types)

## How to Run

```bash
python main.py
```

## Key Takeaways

- Always catch specific exceptions rather than bare `except`
- Use `else` for code that should only run when no exception occurs
- `finally` blocks are ideal for cleanup operations
- Custom exceptions make error handling more maintainable
- Exception chaining preserves the full error context
