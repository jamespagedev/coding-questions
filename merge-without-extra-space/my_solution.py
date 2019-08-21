def custom_binary_sort(arr):
  # if array only has 1 number in it, nothing needs to be done
  if len(arr) < 2:
    return
  elif arr[0] < arr[1]: # avoid binary sort if number is already sorted at index 0
    return

  # re-arrange num at index 0 into proper place
  insert_index = len(arr) // 2 # once found, always use to insert after this index
  index_found = False 
  while not index_found:
    if insert_index == len(arr) - 1:
      index_found = True
    elif arr[0] > arr[insert_index] and arr[0] < arr[insert_index+1]:
      index_found = True
    elif arr[0] > arr[insert_index]:
      insert_index = (insert_index + len(arr)) // 2
    else:
      insert_index = insert_index // 2
  arr.insert(insert_index+1, arr[0])
  del arr[0]



def sort_arrays_numbers(s_arr_nums, l_arr_nums):
  # for i in smaller array
  for i in range(len(s_arr_nums)):
    if s_arr_nums[i] > l_arr_nums[0]:
      s_arr_nums[i], l_arr_nums[0] = l_arr_nums[0], s_arr_nums[i] # swap
      custom_binary_sort(l_arr_nums)



def get_merged_array(arr1, arr2, arr1_length, arr2_length):
  # step1, re-arrange the numbers in both arrays... so the smaller numbers are in first array and larger numbers are in second array
  if arr1_length < arr2_length:
    sort_arrays_numbers(arr1, arr2)
  else:
    sort_arrays_numbers(arr2, arr1)

  if arr1_length < arr2_length:
    return arr1 + arr2
  return arr2 + arr1

if __name__ == '__main__':
  arr1 = [1, 3, 5, 7]
  arr2 = [0, 2, 6, 8, 9]
  print(get_merged_array(arr1, arr2, len(arr1), len(arr2)))