# Python Regular Expressions Masterclass

## Overview

This heavily commented Python script (`main.py`) demonstrates Python's built-in `re` module for pattern matching and text manipulation. It combines fundamental techniques with advanced features through practical examples.

## Key Concepts

### 1. Pattern Matching Fundamentals

- **`re.search()`**: First match anywhere in string (returns Match object)
- **`re.findall()`**: All non-overlapping matches (returns list)
- **`re.match()`**: Match only at string beginning (returns Match object)
- Basic syntax: `\d` (digits), `\w` (word chars), `{n}` (quantifiers)

### 2. Group Extraction

- **Numbered groups**: `()` captures for `match.group(n)` access
- **Named groups**: `(?P<name>...)` for semantic references via `match.group('name')`
- Nested groups and backreferences in patterns

### 3. Text Substitutions

- **`re.sub()`**: Pattern replacement with backreferences (`\1`, `\g<name>`)
- Complex transformations using callbacks
- Multi-pass processing patterns

### 4. Advanced Features

- Lookaheads/lookbehinds (zero-width assertions)
- Greedy (`*`, `+`) vs lazy (`*?`, `+?`) quantifiers
- Compilation flags (`re.IGNORECASE`, `re.MULTILINE`)

## re Module Functions

| Function       | Description                   | Returns           |
| -------------- | ----------------------------- | ----------------- |
| `re.search()`  | First match anywhere          | Match object/None |
| `re.findall()` | All non-overlapping matches   | List of strings   |
| `re.match()`   | Match only at string start    | Match object/None |
| `re.sub()`     | Replace all occurrences       | Modified string   |
| `re.compile()` | Pre-compile pattern for reuse | Pattern object    |

## Regex Syntax Cheatsheet

| Pattern         | Matches                        | Example                 |
| --------------- | ------------------------------ | ----------------------- |
| `\d`            | Digit character                | `\d{3}` matches "123"   |
| `\w`            | Word character (a-z, 0-9, \_)  | `\w+` matches "word"    |
| `.`             | Any character (except newline) | `a.c` matches "abc"     |
| `^`             | Start of string                | `^Hello` matches start  |
| `$`             | End of string                  | `end$` matches end      |
| `*`             | 0 or more repetitions          | `a*` matches "", "a"    |
| `+`             | 1 or more repetitions          | `\d+` matches "123"     |
| `{n}`           | Exactly n repetitions          | `a{3}` matches "aaa"    |
| `( )`           | Capturing group                | `(\d+)` captures digits |
| `(?P<name>...)` | Named capturing group          | `(?P<year>\d{4})`       |
| `\1`            | Backreference to group 1       | `(\w) \1` matches "a a" |

## How to Run

1. Execute the demo script:
   ```bash
   python main.py
   ```
2. Observe the output demonstrating:
   - Date extraction patterns
   - Log parsing with groups
   - Email anonymization
   - Price matching
3. Experiment by modifying:
   - Input text in each function
   - Regex patterns
   - Substitution patterns

## Learning Outcomes

By studying this module, you will:

- Master Python's regex syntax and functions
- Extract structured data from unstructured text
- Implement robust text transformations
- Optimize pattern matching performance
- Handle edge cases in real-world text processing

## Advanced Topics

1. **Pattern Optimization**

   - Pre-compiling with `re.compile()` for reuse
   - Atomic grouping to prevent backtracking
   - Possessive quantifiers for performance

2. **Real-world Applications**

   - Log file analysis and parsing
   - Data validation and sanitization
   - Web scraping content extraction
   - Text normalization pipelines

3. **Performance Considerations**
   - Benchmarking different pattern approaches
   - Balancing readability with efficiency
   - Avoiding catastrophic backtracking

## Code Structure

The script demonstrates:

- `demonstrate_basic_matching()`: Core matching functions
- `demonstrate_groups()`: Data extraction techniques
- `demonstrate_substitutions()`: Text transformations
- `demonstrate_advanced_features()`: Specialized patterns

Each function contains:

- Clear examples with annotated patterns
- Practical use cases
- Experimentation suggestions
