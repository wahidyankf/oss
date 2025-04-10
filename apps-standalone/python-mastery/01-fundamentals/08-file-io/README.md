# Python File I/O Demo

This directory demonstrates Python's file input/output capabilities with robust error handling.

## Key Concepts Demonstrated

1. **File Opening Modes** (`'r'`, `'w'`, `'a'`, `'b'`)
2. **Context Managers** (`with` statement)
3. **Exception Handling** for common file operations:
   - `FileNotFoundError`
   - `PermissionError`
   - `IOError`/`OSError`
4. **Custom Exceptions** for application-specific errors
5. **Cleanup Operations** in `finally` blocks
6. **Reading Methods** (`read()`, `readline()`, `readlines()`)
7. **Writing Methods** (`write()`, `writelines()`)
8. **Path Handling** (`os.path` vs `pathlib`)
9. **Binary File Operations**

## How to Run

```bash
python main.py
```

## Key Takeaways

- Always handle potential file operation errors
- Use specific exception types for different failure modes
- Ensure resources are cleaned up in `finally` blocks
- Create custom exceptions for application-specific errors
- Always use `with` statements for automatic resource cleanup
- `pathlib` provides more intuitive path manipulation
- Different modes serve different purposes (write vs append)
- Be mindful of file encodings when working with text files
