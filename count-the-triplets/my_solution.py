# runtime o(n log n)
'''
def get_triplets(arr, arr_length):
  triplets_found = 0
  num_counter = {}

  # keeps track of duplicate numbers, and used for matching sum with runtime of o(1)
  for num in arr:
    if num in num_counter:
      num_counter[num] += 1
    else:
      num_counter[num] = 1

  # do this to break out of 2nd nested for loop early
  arr.sort()
  max_num = arr[arr_length - 1]

  for left_index in range(arr_length - 1):
    if arr[left_index] + arr[left_index+1] > max_num:
      break
    for right_index in range(left_index+1, arr_length):
      temp_sum = arr[left_index] + arr[right_index]
      if temp_sum > max_num:
        break # exit only the 2nd for loop
      if temp_sum in num_counter:
        triplets_found += num_counter[temp_sum]

  if triplets_found == 0:
    return -1
  return triplets_found
'''

#Rich (my mentor's) Solution
def get_triplets(arr, arr_length):
  sums_found = 0
  arr.sort() # use o(n) sort for an array of just integers (not python's timsort)
  max_sum = arr[-1]

  # hash_table = {7: 2, 6: 5}
  hash_table = {}

  # o(n^?)
  for left_index in range(arr_length - 1):
    if arr[left_index] + arr[left_index+1] > max_sum:
        break
    for right_index in range(left_index+1, arr_length):
      temp_sum = arr[left_index] + arr[right_index]
      if temp_sum > max_sum:
        break
      elif temp_sum not in hash_table:
        hash_table[temp_sum] = 1
      else:
        hash_table[temp_sum] += 1

  print(hash_table)

  for num in arr:
    if num in hash_table:
      sums_found += hash_table[num]

  if sums_found == 0:
    return -1
  return sums_found

# classmates attempt using recursion (failing test cases)
'''
def get_triplets(ar, n):
  ar.sort()
  count = 0
  def recurse(sorted_ar, n):
    nonlocal count
    if n < 3: return count
    if sorted_ar[0] + sorted_ar[1] == sorted_ar[2]:
      count += 1
    return recurse(sorted_ar[1:], len(sorted_ar[1:]))
  recurse(ar, len(ar))

  if count == 0:
    return -1
  return count
'''
if __name__ == '__main__':
  arr = [1, 6, 5, 2, 7]
  print(get_triplets(arr, 4))