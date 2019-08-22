const balancedBrackets = (string) => {
  const possibleBrackets = {
      "]": "[", 
      ")": "(",
      "}": "{"
  };
  let openBrackets = [];
  for (let i = 0; i < string.length; i++){
      if (openBrackets.length === 0 && string.charAt(i) === "|"){
          openBrackets.push(string.charAt(i));
      } else if (string.charAt(i) === "|" && openBrackets[openBrackets.length - 1] === ("|")){
          openBrackets.splice(-1, 1);
      } else if (string.charAt(i) === "|"){
        openBrackets.push(string.charAt(i));
      } else if (Object.values(possibleBrackets).indexOf(string.charAt(i)) > -1){
          openBrackets.push(string.charAt(i));
      } else if (string.charAt(i) in possibleBrackets && openBrackets[openBrackets.length - 1] === possibleBrackets[string.charAt(i)]){
          openBrackets.splice(-1, 1);
      } else if (string.charAt(i) in possibleBrackets){
          return false;
      }
  }

  if (openBrackets.length === 0){
      return true;
  }
  return false;
}

console.log(balancedBrackets("{{||[]||}}"));
