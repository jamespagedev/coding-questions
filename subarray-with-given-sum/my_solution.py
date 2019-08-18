# first pass solution o(n^2) worst case
'''
def get_sub_array_indexes_plus_one(arr, arr_length, target_sum):
  for left_index in range(arr_length):
    current_sum = 0
    for right_index in range(left_index, arr_length):
      current_sum += arr[right_index]
      if current_sum == target_sum:
        return str(left_index+1) + ", " + str(right_index+1)
      if current_sum > target_sum:
        break

  return "-1"
'''

# second pass solution o(n)
def get_sub_array_indexes_plus_one(arr, arr_length, target_sum):
  in_check = True
  left_index = 0
  right_index = 0
  current_sum = arr[0]

  while in_check:
    if current_sum == target_sum:
      return str(left_index+1) + ", " + str(right_index+1)
    elif left_index == arr_length or right_index == arr_length:
      break
    elif current_sum > target_sum:
      current_sum -= arr[left_index]
      left_index += 1
    else:
      right_index += 1
      current_sum += arr[right_index]

  return "-1"

if __name__ == '__main__':
  arr = [1, 2, 3, 7, 5]
  print(get_sub_array_indexes_plus_one(arr, 5, 12))
