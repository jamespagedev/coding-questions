Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found in between any of the numbers of the array.

### **write a function with arguments as follows:**
- getArrayMissingNumber(Array arr)

**Function Arguments:**
- **Array**: array of integers

**Function Return Types:**
- `int` (number missing in array)

### **Constraints:**
- 1 ≤ T ≤ 200
- 1 ≤ N ≤ 107
- 1 ≤ C[i] ≤ 107
- Assume every array has one missing number

### **Example:**
***Input:***
- Each test case must have an array of contiguous numbers that count +1 with one missing number in the array
- *Testcase1*
  - example: [1, 2, 3, 5]
- *Testcase2*
  - example: [1, 2, 3, 4, 5, 6, 7, 8, 10]

***Output:***
- `int` 4
- `int` 9

**Explanation:**
- Testcase 1: returns 4, because 4 goes in between 3 and 5
- Testcase 2: returns 9, because 9 goes in between 8 and 10

problem originally received from: https://practice.geeksforgeeks.org/problems/missing-number-in-array/0