"""
Comprehensive pytest examples covering:
- Basic assertions
- Exception testing
- Fixtures
- Parametrized tests
- Mocking
- Coverage reporting
"""

import pytest
from calculator import add, subtract, multiply, divide


# ===== BASIC TESTS =====
def test_add():
    """Test basic addition"""
    assert add(2, 3) == 5


def test_subtract():
    """Test basic subtraction"""
    assert subtract(5, 3) == 2


# ===== EXCEPTION TESTING =====
def test_divide_by_zero():
    """Test division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# ===== FIXTURES =====
@pytest.fixture
def calculator_fixture():
    """Provides test numbers for calculator tests"""
    return (10, 2)


def test_with_fixture(calculator_fixture):
    """Test using fixture"""
    a, b = calculator_fixture
    assert add(a, b) == 12


# ===== PARAMETRIZED TESTS =====
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (5, -3, 2),
        (0, 0, 0),
    ],
)
def test_add_parametrized(a, b, expected):
    """Test add with multiple inputs"""
    assert add(a, b) == expected


# ===== MOCKING =====
def test_mocking_example(mocker):
    """Demonstrate mocking with pytest-mock"""
    mock_add = mocker.patch("calculator.add", return_value=10)
    assert mock_add(2, 3) == 10
    mock_add.assert_called_once_with(2, 3)


# ===== COVERAGE DEMO =====
# Run with: pytest --cov=calculator
# This test ensures we cover the divide function
def test_divide():
    """Test normal division"""
    assert divide(10, 2) == 5


# ===== INTEGRATION TESTS =====
class TestCalculatorIntegration:
    """Tests combining multiple calculator operations"""

    def test_multiple_operations(self):
        """Test chained calculator operations"""
        result = add(10, multiply(2, subtract(5, 3)))
        assert result == 14

    def test_complex_calculation(self):
        """Test more complex calculation sequence"""
        result = divide(multiply(add(2, 3), subtract(10, 5)), add(1, 1))
        assert result == 12.5

    @pytest.mark.parametrize(
        "operations,expected",
        [
            ([(add, (1, 2)), (multiply, (3, 4))], (3, 12)),
            ([(subtract, (5, 1)), (divide, (10, 2))], (4, 5)),
        ],
    )
    def test_operation_sequences(self, operations, expected):
        """Test sequences of operations with parametrization"""
        results = []
        for func, args in operations:
            results.append(func(*args))
        assert tuple(results) == expected
