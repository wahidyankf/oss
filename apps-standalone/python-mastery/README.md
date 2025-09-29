# python-mastery

Comprehensive Python learning curriculum covering fundamentals to advanced topics, with practical examples and exercises for each concept.

## Overview

Python Mastery is a structured learning path designed to take you from Python basics to advanced concepts and professional development practices. The curriculum is organized into 32 topics across 4 main sections, each building upon previous knowledge.

## Curriculum Structure

```
python-mastery/
├── 01-fundamentals/           # Core Python concepts
├── 02-intermediate-python/    # Advanced language features
├── 03-advanced-python/        # Expert-level topics
└── 04-professional-development/ # Real-world practices
```

### 1. Fundamentals (8 topics)

- **Syntax, Semantics & Environment**: Python basics and setup
- **Core Data Types**: Numbers, strings, lists, tuples, sets, dicts
- **Operators**: Arithmetic, comparison, logical, bitwise
- **Control Flow**: if/elif/else, loops, comprehensions
- **Functions**: Definition, arguments, scope, lambdas
- **Modules & Packages**: Imports, creating packages
- **Error Handling**: Exceptions, try/except, custom errors
- **File I/O**: Reading, writing, file operations

### 2. Intermediate Python (7 topics)

- **OOP Modeling & Abstraction**: Classes, inheritance, polymorphism
- **Iterators & Generators**: Custom iterators, yield, generator expressions
- **Decorators**: Function and class decorators
- **Context Managers**: with statements, creating context managers
- **Regular Expressions**: Pattern matching, groups, substitutions
- **Data Formats & Times**: JSON, CSV, datetime handling
- **Functional Programming**: map, filter, reduce, functools

### 3. Advanced Python (3 topics)

- **Concurrency & Parallelism**: Threading, multiprocessing, asyncio
- **Metaclasses**: Class creation, descriptors, metaclass use cases
- **Descriptors**: Property implementation, data vs non-data descriptors

### 4. Professional Development (14 topics)

- Testing strategies
- Documentation
- Performance optimization
- Database interaction
- Web development
- API design
- Security best practices
- And more...

## Getting Started

### Prerequisites

- Python 3.13.2 (managed via pyenv)
- pip package manager
- Virtual environment support

### Setup

```bash
# Navigate to project
cd apps-standalone/python-mastery

# Set Python version
pyenv local 3.13.2

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Unix/macOS
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running Examples

Each topic has its own directory with README and example code:

```bash
# Navigate to a topic
cd 01-fundamentals/01-syntax-semantics-environment

# Run the example
python main.py

# Read the topic documentation
cat README.md
```

### Testing

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest test_main.py

# Run with coverage
python -m pytest --cov=.

# Run with verbose output
python -m pytest -v
```

## Learning Path

### Recommended Approach

1. **Start with Fundamentals**: Work through topics 1-8 in order
2. **Practice Each Topic**: Run examples, modify code, experiment
3. **Build Projects**: Apply concepts in small projects
4. **Move to Intermediate**: Once comfortable with basics
5. **Choose Specialization**: Focus on areas relevant to your goals

### Time Estimates

- **Fundamentals**: 2-4 weeks (beginner), 1 week (experienced)
- **Intermediate**: 3-4 weeks
- **Advanced**: 2-3 weeks
- **Professional**: Ongoing, based on needs

## Code Examples

### Basic Function (Fundamentals)

```python
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"
```

### Generator (Intermediate)

```python
def fibonacci(n: int):
    """Generate Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### Descriptor (Advanced)

```python
class Positive:
    """Descriptor ensuring positive values."""
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        obj.__dict__[self.name] = value
```

## Best Practices

### Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all functions/classes
- Keep functions small and focused

### Learning Tips

- Run every example
- Modify code to test understanding
- Break when confused - review fundamentals
- Join Python communities for support

## Resources

### Documentation

- [Python Official Docs](https://docs.python.org/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)

### Tools

- **Black**: Code formatter (configured)
- **pytest**: Testing framework
- **mypy**: Static type checker
- **pylint**: Code analyzer

## Contributing

To add new topics or improve examples:

1. Follow existing structure
2. Include README for each topic
3. Add practical examples
4. Include tests
5. Submit pull request

## Development Commands

```bash
# Format code
black .

# Run linting
pylint src/

# Type checking
mypy src/

# Run specific topic
cd 02-intermediate-python/10-iterators-generators
python main.py
```

## Troubleshooting

### Virtual Environment Issues

```bash
# Recreate environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Import Errors

- Ensure virtual environment is activated
- Check Python version: `python --version`
- Verify package installation: `pip list`

## Related Documentation

- [Standalone Projects Guide](/docs/reference/standalone-projects.md)
- [Development Workflow](/docs/how-to/development-workflow.md)
- [Code Style Guide](/docs/reference/code-style.md)

## License

MIT License - Educational use encouraged!
