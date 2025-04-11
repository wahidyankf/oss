"""
Property-based tests using Hypothesis
"""

from hypothesis import given, strategies as st
from calculator import add, subtract, multiply, divide
import pytest
import math


# Helper to check for NaN safely
def is_nan(x):
    return x != x


# ===== BASIC PROPERTIES =====
@given(st.floats(), st.floats())
def test_add_commutative(a, b):
    """Addition is commutative (a + b == b + a)"""
    result1 = add(a, b)
    result2 = add(b, a)
    if is_nan(result1) or is_nan(result2):
        assert is_nan(result1) and is_nan(result2)
    else:
        assert result1 == result2


@given(st.floats(), st.floats(), st.floats())
def test_add_associative(a, b, c):
    """Addition is associative ((a + b) + c == a + (b + c))"""
    # Skip very large numbers that exceed floating point precision
    if abs(a) > 1e15 or abs(b) > 1e15 or abs(c) > 1e15:
        pytest.skip(
            "Skipping very large numbers to avoid floating point precision issues"
        )

    result1 = add(add(a, b), c)
    result2 = add(a, add(b, c))
    if is_nan(result1) or is_nan(result2):
        assert is_nan(result1) and is_nan(result2)
    else:
        # Use approximate comparison for floating point numbers
        assert result1 == pytest.approx(result2, rel=1e-10, abs=1e-10)


# ===== OPERATION PROPERTIES =====
@given(st.floats(), st.floats())
def test_subtract_inverse(a, b):
    """Subtraction is inverse of addition (a - b == a + (-b))"""
    result1 = subtract(a, b)
    result2 = add(a, -b)
    if is_nan(result1) or is_nan(result2):
        assert is_nan(result1) and is_nan(result2)
    else:
        assert result1 == result2


@given(st.floats(min_value=1e-10), st.floats(min_value=1e-10))
def test_divide_multiply_inverse(a, b):
    """Division is inverse of multiplication (a / b == a * (1/b))"""
    if math.isinf(a) or math.isinf(b):
        pytest.skip("Skip infinite values for this test")
    result1 = divide(a, b)
    result2 = multiply(a, 1 / b)
    assert result1 == pytest.approx(result2)


# ===== EDGE CASE TESTING =====
@given(st.floats())
def test_add_zero_identity(a):
    """Adding zero returns same value (a + 0 == a)"""
    if math.isinf(a):
        pytest.skip("Skip infinite values for this test")
    result = add(a, 0)
    if is_nan(result):
        assert is_nan(a)
    else:
        assert result == a


@given(st.floats())
def test_multiply_zero(a):
    """Multiplying by zero returns zero (a * 0 == 0)"""
    if math.isinf(a):
        pytest.skip("Skip infinite values for this test")
    result = multiply(a, 0)
    if is_nan(result):
        assert is_nan(a)
    else:
        assert result == 0


# ===== ADDITIONAL PROPERTIES =====
@given(st.floats())
def test_subtract_self(a):
    """Subtracting a number from itself returns zero (a - a == 0)"""
    if math.isinf(a):
        pytest.skip("Skip infinite values")
    result = subtract(a, a)
    if is_nan(result):
        assert is_nan(a)
    else:
        assert result == 0


@given(st.floats(allow_nan=False))
def test_multiply_identity(a):
    """Multiplying by one returns same value (a * 1 == a)"""
    if abs(a) > 1e15:
        pytest.skip("Skip very large numbers")
    assert multiply(a, 1) == a


@given(st.floats(min_value=1e-10, allow_nan=False, allow_infinity=False))
def test_divide_self(a):
    """Dividing a number by itself returns one (a / a == 1)"""
    assert divide(a, a) == pytest.approx(1, rel=1e-10)


# Stateful testing example
from hypothesis import note, settings, HealthCheck
from hypothesis.stateful import RuleBasedStateMachine, rule


class CalculatorMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.total = 0.0

    @rule(num=st.floats(allow_nan=False, allow_infinity=False))
    def add_number(self, num):
        """Stateful test: adding numbers sequentially"""
        original = self.total
        self.total = add(self.total, num)
        note(f"Added {num} to {original} = {self.total}")
        if abs(original) < 1e15 and abs(num) < 1e15:
            assert self.total == pytest.approx(original + num)

    @rule(num=st.floats(allow_nan=False, allow_infinity=False))
    def subtract_number(self, num):
        """Stateful test: subtracting numbers sequentially"""
        original = self.total
        self.total = subtract(self.total, num)
        note(f"Subtracted {num} from {original} = {self.total}")
        if abs(original) < 1e15 and abs(num) < 1e15:
            assert self.total == pytest.approx(original - num)


# Register the stateful test
TestCalculator = CalculatorMachine.TestCase
TestCalculator.settings = settings(
    max_examples=100, suppress_health_check=[HealthCheck.too_slow]
)


# ===== ERROR CASE TESTING =====
@given(st.floats(), st.floats(allow_nan=False, allow_infinity=False))
def test_divide_by_zero(a, b):
    """Division by zero raises ValueError"""
    with pytest.raises(ValueError):
        divide(a, 0)
