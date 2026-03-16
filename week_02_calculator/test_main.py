"""Tests for Week 2 – Simple Calculator."""

import pytest
from week_02_calculator.main import add, subtract, multiply, divide, calculate


def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_calculate_dispatch():
    assert calculate(2, "+", 3) == 5
    assert calculate(10, "-", 4) == 6
    assert calculate(3, "*", 3) == 9
    assert calculate(9, "/", 3) == 3.0


def test_calculate_invalid_operator():
    with pytest.raises(ValueError):
        calculate(1, "^", 2)
