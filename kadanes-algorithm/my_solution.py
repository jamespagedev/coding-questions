# first pass solution o(n^2)
'''
def get_sub_array_sum(arr, arr_length):
  # handle edge case array only 1 element
  if arr_length == 1:
    if arr[0] > 0:
      return arr[0]
    else:
      return -1

  max_sum = 0

  for left_index in range(arr_length):
    current_sum = 0
    for right_index in range(left_index, arr_length):
      current_sum += arr[right_index]
      if current_sum > max_sum:
        max_sum = current_sum

  if max_sum == 0:
    return -1
  return max_sum
'''

# optimal solution o(n)
def get_sub_array_sum(arr, arr_length):
  # handle edge case array only 1 element
  if arr_length == 1:
    if arr[0] > 0:
      return arr[0]
    else:
      return -1

  # initialize two different sums
  current_sum = arr[0]
  max_sum = current_sum

  # iterate through the array
  for i in range(1, arr_length):
    current_sum = max(arr[i], current_sum+arr[i])
    max_sum = max(current_sum, max_sum)

  if max_sum == 0:
    return -1
  return max_sum

if __name__ == '__main__':
  arr = [1, 2, 3, -2, 5]
  print(get_sub_array_sum(arr, 5))