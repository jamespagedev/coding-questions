import unittest
from my_solution import maxtrix_transpose

class Test(unittest.TestCase):

    def test_case_1(self):
        matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
              ]
        self.assertEqual(maxtrix_transpose(matrix), [[1,4,7], [2,5,8], [3,6,9]])

if __name__ == '__main__':
    unittest.main()