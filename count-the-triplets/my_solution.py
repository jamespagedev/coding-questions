# runtime o(n log n)
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
    for right_index in range(left_index+1, arr_length):
      temp_sum = arr[left_index] + arr[right_index]
      if temp_sum > max_num:
        break # exit only the 2nd for loop
      if temp_sum in num_counter:
        triplets_found += num_counter[temp_sum]


  if triplets_found == 0:
    return -1
  return triplets_found

if __name__ == '__main__':
  arr = [1, 2, 1, 2]
  print(get_triplets(arr, 4))