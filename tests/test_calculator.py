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

    def test_multiply(self):
        assert self.calculator.multiply(2, 3) == 6
        assert self.calculator.multiply(-1, 1) == -1
        assert self.calculator.multiply(0, 5) == 0
        assert self.calculator.multiply(-5, -5) == 25
    
    def test_divide(self):
        assert self.calculator.divide(6, 3) == 2
        assert self.calculator.divide(-1, 1) == -1
        assert self.calculator.divide(0, 5) == 0
        assert self.calculator.divide(-5, -5) == 1
        with pytest.raises(ValueError):
            self.calculator.divide(5, 0)