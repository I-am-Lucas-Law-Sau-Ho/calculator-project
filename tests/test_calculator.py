import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(2, 3) == 5
        assert self.calculator.add(-1, 1) == 0
        assert self.calculator.add(0, 0) == 0
        assert self.calculator.add(-5, -5) == -10

    def test_subtract(self):
        assert self.calculator.subtract(5, 2) == 3
        assert self.calculator.subtract(1, -1) == 2
        assert self.calculator.subtract(0, 0) == 0
        assert self.calculator.subtract(-5, -5) == 0