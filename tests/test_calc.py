import pytest

from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(2, 3) == 5
        assert self.calc.adding(-1, 1) == 0
        assert self.calc.adding(0, 0) == 0

    def test_subtraction_success(self):
        assert self.calc.subtraction(5, 3) == 2
        assert self.calc.subtraction(10, 10) == 0
        assert self.calc.subtraction(0, 5) == -5

    def test_multiply_success(self):
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(-2, 4) == -8

    def test_division_success(self):
        assert self.calc.division(10, 2) == 5
        assert self.calc.division(9, 3) == 3
        assert self.calc.division(1, 2) == 0.5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)