# Automated Testing with pytest

This demo showcases Python testing best practices using pytest.

## Key Features Demonstrated

- **Basic assertions**: Simple test cases for calculator functions
- **Exception testing**: Verifying error conditions
- **Fixtures**: Reusable test components
- **Parametrized tests**: Running tests with multiple inputs
- **Mocking**: Isolating components for testing
- **Coverage**: Measuring test coverage
- **Benchmarking**: Performance testing with pytest-benchmark

## Test Files

1. `test_calculator.py` - Functional tests (unit, integration)
2. `test_benchmarks.py` - Performance benchmarks

## How to Run Tests

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run all functional tests:

   ```bash
   pytest -v test_calculator.py
   ```

3. Run performance benchmarks:

   ```bash
   pytest -v test_benchmarks.py
   ```

   (Add `--benchmark-histogram` for visual output)

4. Run with coverage reporting:

   ```bash
   pytest --cov=calculator --cov-report=html
   ```

   (Open htmlcov/index.html in browser)

5. Run specific test categories:

   ```bash
   # Just unit tests
   pytest -v -k "test_add or test_subtract"

   # Just integration tests
   pytest -v -k "TestCalculatorIntegration"

   # Just mocking tests
   pytest -v -k "mocking"
   ```

## Test Organization

Tests are organized into sections:

1. `test_calculator.py` contains:

   - Basic function tests
   - Exception tests
   - Fixture examples
   - Parametrized tests
   - Mocking examples
   - Coverage demonstration

2. `calculator.py` contains the implementation being tested

## Benchmark Testing

Key benchmark features demonstrated:

- Basic operation timing
- Complex calculation performance
- Parametrized benchmarks with different input sizes

View benchmark results with:

```bash
pytest test_benchmarks.py --benchmark-autosave
pytest-benchmark compare
```

## Key Testing Concepts

- **Fixtures**: Reduce code duplication with reusable test components
- **Parametrization**: Test multiple inputs with a single test function
- **Mocking**: Isolate components by replacing dependencies
- **Coverage**: Identify untested code paths

## Best Practices Illustrated

- Clear separation of test types
- Small, focused test cases
- Documentation of test purpose
- Verification of both happy paths and error cases
- Performance measurement
- Coverage analysis
