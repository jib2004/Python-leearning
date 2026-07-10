# import unittest
from calculator import square
import pytest

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()


# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squares did not equal 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squares did not equal 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squares did not equal 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squares did not equal 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squares did not equal 0")

# PyTest
# pip install pytest
# > pytest test_calculator.py
#Divide them into various func so you can test them on various cases
def test_positive():
   assert square(2) == 4
   assert square(3) == 9

def test_negative():
   assert square(-2) == 4
   assert square(-3) == 9

def zero():
   assert square(0) == 0

def test_str():
   with pytest.raises(TypeError):
       square("cat")




