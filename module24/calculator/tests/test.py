import pytest

from module24.calculator.app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 6) == 30

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(self, 8, 6) == 2

    def test_adding(self):
        assert self.calc.adding(self, 5, 7) == 12
