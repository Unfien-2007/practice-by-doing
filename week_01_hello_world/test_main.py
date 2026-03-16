"""Tests for Week 1 – Hello World & Basic I/O."""

import datetime
from week_01_hello_world.main import calculate_birth_year, greet


def test_calculate_birth_year():
    current_year = datetime.date.today().year
    assert calculate_birth_year(20) == current_year - 20
    assert calculate_birth_year(0) == current_year


def test_greet_output(capsys):
    greet("Alice", 30)
    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "30" in captured.out
