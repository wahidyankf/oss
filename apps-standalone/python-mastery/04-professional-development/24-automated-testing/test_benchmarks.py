"""
Performance benchmarks for calculator operations
"""

import pytest
from calculator import add, subtract, multiply, divide


# ===== BASIC BENCHMARKS =====
def test_add_performance(benchmark):
    """Benchmark basic addition"""
    result = benchmark(add, 1000, 2000)
    assert result == 3000


def test_subtract_performance(benchmark):
    """Benchmark basic subtraction"""
    result = benchmark(subtract, 5000, 3000)
    assert result == 2000


# ===== COMPLEX OPERATION BENCHMARKS =====
def test_complex_calculation_performance(benchmark):
    """Benchmark complex calculation sequence"""

    def calculation():
        return divide(multiply(add(2, 3), subtract(10, 5)), add(1, 1))

    result = benchmark(calculation)
    assert result == 12.5


# ===== PARAMETRIZED BENCHMARKS =====
@pytest.mark.parametrize(
    "a,b",
    [
        (1000, 2000),
        (5000, 3000),
        (12345, 67890),
    ],
)
def test_parametrized_benchmark(benchmark, a, b):
    """Benchmark with different input sizes"""
    result = benchmark(add, a, b)
    assert result == a + b
