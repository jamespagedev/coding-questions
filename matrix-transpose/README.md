Write a function that receives an M x N matrix and return a new matrix that is the transpose of the one received. 

### **write a function with arguments as follows:**
- maxtrix_transpose(2d Array)

**Function Arguments:**
- **arr**: 2d array

**Function Return Types:**
- `2d Array` (a 2d array of ints)

### **Constraints:**
- dimensions: smallest array is 1,1
- dimensions: width and height can differ

### **Example:**
***Input:***
- Each test case...
  ```
  [
    [1,2,3], # coordinates [[0,0], [0,1], [0,2]]
    [4,5,6], # coordinates [[1,0], [1,1], [1,2]]
    [7,8,9]  # coordinates [[2,0], [2,1], [2,2]]
  ]
  ```

***Output:***
  ```
  `2d array` [
    [1,4,7], # coordinates [[0,0], [1,0], [2,0]]
    [2,5,8], # coordinates [[0,1], [1,1], [2,1]]
    [3,6,9]  # coordinates [[0,2], [1,2], [2,2]]
  ]
  ```

**Explanation:**
- Testcase: Each nested element in the matrix has an `[x, y]` coordinate. The output should flip the values for x and y for every coordinate.

problem originally received from: https://www.geeksforgeeks.org/program-to-find-transpose-of-a-matrix/