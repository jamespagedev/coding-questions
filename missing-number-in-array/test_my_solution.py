import unittest
from my_solution import get_array_missing_number

class Test(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 3, 5]
        self.assertEqual(get_array_missing_number(arr), 4)

    def test_case_2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        self.assertEqual(get_array_missing_number(arr), 9)

    def test_case_3(self):
        arr = [3, 4, 5, 7, 8]
        self.assertEqual(get_array_missing_number(arr), 6)

if __name__ == '__main__':
    unittest.main()