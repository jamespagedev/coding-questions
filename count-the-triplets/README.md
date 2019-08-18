Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

### **write a function with arguments as follows:**
- getTriplets(Array arr, int arrLength)

**Function Arguments:**
- **arr**: an (unsorted) array of non-negative integers and non-zero's
- **arrLength**: the length of the array

**Function Return Types:**
- `int` (int number of triplets found, -1 if none found)

### **Constraints:**
- 1 <= arrLength <= 10^5
- 1 <= element max int <= 10^6

### **Example:**
***Input:***
- The first line of each testcase is `arrLength`
- The second line of each test case contains **integer elements**, within the `array`.
- *Testcase1*
  - 4
  - 1 5 3 2
- *Testcase2*
  - 3
  - 3 2 7

***Output:***
- 2
- -1

**Explanation:**
- Testcase1: sum of elements from 2nd position to 4th position is 12
- Testcase2: sum of elements from 1st position to 5th position is 15
- Testcase3: no available sum to equal the target sum, therefor return -1

problem originally received from: https://practice.geeksforgeeks.org/problems/count-the-triplets/0