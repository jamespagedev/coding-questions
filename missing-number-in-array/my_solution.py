def get_array_missing_number(arr):
  for i in range(len(arr) - 1):
    if arr[i+1] is not arr[i] + 1:
      return arr[i] + 1

  return -1 # default

if __name__ == '__main__':
  arr = [1, 2, 3, 5]
  print(get_array_missing_number(arr))