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