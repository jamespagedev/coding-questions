Given two sorted arrays `arr1` and `arr2` in non-decreasing order with size n and m. The first task is to re-arrange the numbers in both arrays, so the smaller numbers are in the first array (sorted), and the larger numbers are in the second array (sorted). The second task is to have the function return a single merged array with all numbers from both arrays sorted in the merged array(Hint: use concatination of both arrays on the return).

**Note:** Expected time complexity is O((n+m) log(n+m)). DO NOT use extra space (Hint: return a concatination of arr1+arr2).  We need to modify existing arrays as following.
```
Input: arr1 = [10]
       arr2 = [2, 3]
Output: arr1 = [2]
        arr2 = [3, 10]

Input: arr1 = [1, 5, 9, 10, 15, 20]
       arr2 = [2, 3, 8, 13]
Output: arr1 = [1, 2, 3, 5, 8, 9]
        arr2 = [10, 13, 15, 20]
```

### **write a function with arguments as follows:**
- getMergedArray(Array arr1, Array arr2, arr1Length, arr2Length)

**Function Arguments:**
- **arr1**: first sorted array of integers
- **arr2**: second sorted array of integers
- **arr1Length**: length of first array
- **arr2Length**: length of second array

**Function Return Types:**
- `Array` (single array of both input arrays combined with the numbers sorted in order)

### **Constraints:**
- 1 <= T <= 100
- 1 <= X, Y <= 5*104
- 0 <= arr1i, arr2i <= 109

### **Example:**
***Input:***
- Each test case...
- *Testcase1*
  - example: [1, 3, 5, 7], [0, 2, 6, 8, 9]
- *Testcase2*
  - example: [10, 12], [5, 18, 20]

***Output:***
- `Array` [0, 1, 2, 3, 5, 6, 7, 8, 9]
- `Array` [5, 10, 12, 18, 20]

**Explanation:**
- Testcases: returns the numbers from arr1 and arr2 as a single array with all numbers sorted

problem originally received from: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0/