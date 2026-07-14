# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
from solution import power_table

def power_table_test():
    assert power_table(2,5) == "2, 4, 8, 16, 32"