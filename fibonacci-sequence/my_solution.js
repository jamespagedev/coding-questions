function fibonacci(n) {
  result = []
  first = 1;
  second = 0;
  temp = 0;
  c = n-1;

  result.push(second);
  while (c > 0){
    temp = first;
    first = first + second;
    second = temp;
    result.push(second);
    c--;
  }

  return result;
}

console.log(fibonacci(4));