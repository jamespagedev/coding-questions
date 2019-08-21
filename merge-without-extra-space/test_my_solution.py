import unittest
from my_solution import get_merged_array

class Test(unittest.TestCase):
  def test_case_1(self):
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    self.assertEqual(get_merged_array(arr1, arr2, len(arr1), len(arr2)), [0, 1, 2, 3, 5, 6, 7, 8, 9])

  def test_case_2(self):
    arr1 = [10, 12]
    arr2 = [5, 18, 20]
    self.assertEqual(get_merged_array(arr1, arr2, len(arr1), len(arr2)), [5, 10, 12, 18, 20])

  def test_case_3(self):
    arr1 = [10]
    arr2 = [2, 3]
    self.assertEqual(get_merged_array(arr1, arr2, len(arr1), len(arr2)), [2, 3, 10])

  def test_case_4(self):
    arr1 = [1, 5, 9, 10, 15, 20]
    arr2 = [2, 3, 8, 13]
    self.assertEqual(get_merged_array(arr1, arr2, len(arr1), len(arr2)), [1, 2, 3, 5, 8, 9, 10, 13, 15, 20])

if __name__ == '__main__':
  unittest.main()