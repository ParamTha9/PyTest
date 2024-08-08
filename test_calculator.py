# import pytest
# from calculator import Calculator

# @pytest.fixture
# def calc():
#     return Calculator()

# def test_addition(calc):
#     assert calc.add(2, 3)==5

# def test_subtraction(calc):
#     assert calc.subtract(5, 3)==2

# def test_multiplication(calc):
#     assert calc.multiply(3, 4) == 12

# def test_division(calc):
#     assert calc.divide(8, 2)==4

# def test_division_by_zero(calc):
#     with pytest.raises(ValueError):
#         calc.divide(10, 0)
