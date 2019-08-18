import unittest
from my_solution import get_triplets


class Test(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 5, 3, 2]
        self.assertEqual(get_triplets(arr, 4), 2)

    def test_case_2(self):
        arr = [1, 1, 2, 2]
        self.assertEqual(get_triplets(arr, 4), 2)

    def test_case_3(self):
        arr = [7, 2, 5, 4, 3, 6, 1, 9, 10, 12]
        self.assertEqual(get_triplets(arr, 10), 18)

    def test_case_no_triplets(self):
        arr = [3, 2, 7]
        self.assertEqual(get_triplets(arr, 3), -1)

if __name__ == '__main__':
    unittest.main()