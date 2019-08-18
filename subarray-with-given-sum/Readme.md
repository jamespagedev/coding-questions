The purpose of this problem is to determine if you can find the create a contiguous `sub-array` by adding all the array elements between two specific indexes, to equal the `targetSum`. If this is possible, return a **string of both (index+1)** for the sub-array(see example output). If it's not possible, return a string of **-1**.

### **write a function with arguments as follows:**
- getSubArrayIndexesPlusOne(Array arr, int arrLength, int targetSum)

**Function Arguments:**
- **arr**: an (unsorted) array of non-negative integers and non-zero's
- **arrLength**: the length of the array
- **targetSum**: the target sum of the contiguous sub-array within the array.

**Function Return Types:**
- `"int, int"` (ints greater than 0)
- `"-1"` (default)

### **Constraints:**
- 1 <= arrLength <= 10^7
- 1 <= element max int <= 10^10

### **Example:**
***Input:***
- The first line of each testcase is `arrLength` and `targetSum`.
- The second line of each test case contains **integer elements**, within the `array`.
- *Testcase1*
  - 5 12
  - 1 2 3 7 5
- *Testcase2*
  - 10 15
  - 1 2 3 4 5 6 7 8 9 10
- *Testcase3*
  - 3 5
  - 9 4 7

***Output:***
- "2, 4"
- "1, 5"
- "-1"

**Explanation:**
- Testcase1: sum of elements from 2nd position to 4th position is 12
- Testcase2: sum of elements from 1st position to 5th position is 15
- Testcase3: no available sum to equal the target sum, therefor return -1

problem originally received from: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0