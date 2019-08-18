import unittest
from my_solution import get_sub_array_sum

class Test(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 3, -2, 5]
        self.assertEqual(get_sub_array_sum(arr, 5), 9)

    def test_case_2(self):
        arr = [10, 8, -12, 5, -9, 100]
        self.assertEqual(get_sub_array_sum(arr, 6), 102)

    def test_case_3(self):
        arr = [2, 4, 6, -10, 5]
        self.assertEqual(get_sub_array_sum(arr, 5), 12)

    def test_case_no_triplets(self):
        arr = [-1, -2, -3, -4]
        self.assertEqual(get_sub_array_sum(arr, 4), -1)

if __name__ == '__main__':
    unittest.main()