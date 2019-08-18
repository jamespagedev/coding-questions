Given an array of negative and positive integers, find the contiguous sub-array with maximum sum.

### **write a function with arguments as follows:**
- getSubArraySum(Array arr, int arrLength)

**Function Arguments:**
- **arr**: an (unsorted) array of negative and positive integers
- **arrLength**: the length of the array

**Function Return Types:**
- `int` (sum, -1 if no sum greater than 0)

### **Constraints:**
- 1 <= arrLength <= 10^6
- -10^7 <= element max int <= 10^7

### **Example:**
***Input:***
- The first line of each testcase is `arrLength`
- The second line of each test case contains **integer elements**, within the `array`.
- *Testcase1*
  - 5
  - 1 2 3 -2 5
- *Testcase2*
  - 4
  - -1 -2 -3 -4

***Output:***
- 9
- -1

**Explanation:**
- Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
- Testcase 2: Returns -1: no sum exists greater than 0

problem originally received from: https://practice.geeksforgeeks.org/problems/count-the-triplets/0