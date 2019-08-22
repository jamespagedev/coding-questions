function getRotatedArrayIndex(arr) {
  console.log(arr.length)
  for (let i = 0; i < arr.length; i++){
      console.log(i)
      // if (arr[i] > arr[i+1]){
      //     return i+1
      // }
  }
  return -1;
}

function unRotateArrayIndexes(arr) {
  let arr1 = []
  let arr2 = []
  for (let i = 0; i < arr.length - 1; i++){
      if (arr[i] > arr[i+1]){
          arr1 = arr.splice(i+1)
          arr2 = arr.splice(0, i+1)
          return arr1.concat(arr2)
      }
  }
}

function shiftedBinarySearch(arr, target) {
  if (arr.length === 0 && arr[0] === target){
      return 0
  } else if (arr.length === 0 && arr[0] !== target){
      return -1
  }

  // sort array using o(n)
  var shiftedIndex = getRotatedArrayIndex(arr);
  const sortedArr = unRotateArrayIndexes(arr);
  if (target < sortedArr[0] || target > sortedArr[sortedArr.length - 1]){
      return -1;
  } else if (sortedArr.length)


  
  
  var currIndex = Math.floor(sortedArr.length / 2);
  console.log("currIndex =", currIndex);
  while (sortedArr[currIndex] !== target){
      if (currIndex === 0 && sortedArr[currIndex+1] > target){ // not found
          return -1
      } else if (currIndex === sortedArr.length-1 && sortedArr[currIndex-1] > target){ // not found
          return -1
      } else if (sortedArr[currIndex] < target && sortedArr[currIndex+1] > target){
          return -1
      } else if (sortedArr[currIndex] > target && sortedArr[currIndex-1] < target){
          return -1
      }

      // update index
      if (sortedArr[currIndex] > target){
          currIndex = Math.floor(currIndex / 2);
      } else if (sortedArr[currIndex] < target) {
          currIndex = Math.floor((currIndex + sortedArr.length) / 2)
      }
  }

  console.log("sortedArr", sortedArr)
  console.log("shiftedIndex =", shiftedIndex)
  if (currIndex > shiftedIndex){
      return currIndex - shiftedIndex;
  }
  return shiftedIndex + currIndex;
}

console.log(shiftedBinarySearch([19, 27, 28, 33, 39, 41, 46, 49, 2, 5, 6, 10, 13, 14, 15, 17], 33));