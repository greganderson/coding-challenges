import pytest

from factorial import factorial


def test_factorial():
    """Calculates the factorial of a given integer"""
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(1) == 1
